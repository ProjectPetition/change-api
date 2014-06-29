import os,sys
import glob
from datetime import date
import json
import requests

sys.path.append('converters/signature_converter_v2/')
import petitions_signature_converter

sys.path.append('converters/reasons_converter_v2/')
import petition_reasons_converter

sys.path.append('change_org_db_interface/signature_db/')
import pet_sig_db 

sys.path.append('change_org_db_interface/petitions_db/')
import pet_body_db

sys.path.append('change_org_db_interface/reasons.db/')
import pet_res_db

class Change_Org_Collection:

    def get_petition_id(self, petition_name):

	config = open('api_key', 'r')
        api = config.read().replace('\n', '')
        config.close()

        petition_url = 'http://www.change.org/petitions/' + petition_name
        
	query_url = 'https://api.change.org/v1/petitions/get_id'

        parameters  = { 'api_key': api, 'petition_url': petition_url }

	r = requests.get(query_url, params=parameters)

	response = r.json()

	pet_id = response['petition_id']

        return pet_id

    def get_signatures(self, petition_title, out_file, page_num, page_size, temp):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	psdb = pet_sig_db.Signature_DB() 

	if (out_file != ''):
	    
	    o_file = open(out_file, 'wb')

	petition_id = str(self.get_petition_id(petition_title))
        
	sig_url = 'http://api.change.org/v1/petitions/' + petition_id + '/signatures'
        
	parameters  = { 'api_key': api , 'page_size': page_size, 'page': page_num}

	sig_req = requests.get(sig_url, params=parameters)

	sig_res = sig_req.json()

	if (int(page_size) == 1 and int(temp) == 1):

	    psdb.insert(petition_id, sig_res)


	else: 
	    
	    o_file.write((json.dumps(sig_res)))

        return sig_res['total_pages']


    def get_all_signatures(self, date, path_to_file_out, title, page_size):

	sc = petitions_signature_converter.Signature_Converter()

	pages = int(self.get_pages(title, 0))

        pages += 1

	for i in range(1, pages):

	    sig_out = 'sig_pg_' + str(i) + '.sigtmp'

	    self.get_signatures(title, sig_out, str(i), page_size, 1)

	    if (page_size > 1):
	    
		sc.converter(date, sig_out, path_to_file_out + '/', title + '-' + 'page_' + str(i) + '.sig')

        if (page_size > 1):
	
	    self.concat_files('sig', path_to_file_out + '/' + date + '/', path_to_file_out + '/' + date + '/' + title )


    def get_petition_text(self, petition_title, out_file):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

        pbdb = pet_body_db.Body_DB() 

	o_file = open(out_file, 'wb')

	pid = str(self.get_petition_id(petition_title))
		
	body_url = 'http://api.change.org/v1/petitions/' + pid

        parameters  = { 'api_key': api }

	body_req = requests.get(body_url, params=parameters)

	body_res = body_req.json()

	pbdb.insert(body_res)

	
        #o_file.write(json.dumps(body_res))


      
    def get_pages(self, title, reasons):

	if (int(reasons) == 0):
	    
	    pages = self.get_signatures(title, 'temp.tmp', '1', 1, 0)

	elif (int(reasons) == 1):

	    pages = self.get_reasons(title, '.', 'temp.tmp', '1', '1')

	return pages
       

    def concat_files(self, file_ext, path_to_file_in, file_out):

	if (file_ext == 'sig'):

	    ext_tmp = '*.sigtmp'
	    ext = '.sig'

	elif (file_ext == 'reasons'):

	    ext_tmp = '*.reasonstmp'
	    ext = '.reasons'

	files = glob.glob(path_to_file_in + '*' + ext)

	output_file = open(file_out.strip('reasons') + ext + '.cat', 'wb')

	if (file_ext == 'sig'):
	    
	    output_file.write('Page,Total Pages,Signature Count,Signatures\n,,,Name,City,State/Province,Country Code,Country Name,Signed At\n')

	elif (file_ext == 'reasons'):

	    output_file.write('Page,Total Pages,Reasons\n,,Created At,Content,Like Count,Author Name,Author URL\n')

	for line in files:

	    input_files = open(line, 'r')

	    output_file.write(input_files.read())
	    output_file.write('\n')
	    input_files.close()

	for file_name in glob.glob(path_to_file_in + '/' + ext_tmp):
	
	    os.remove(file_name)

	output_file.close()

    def get_reasons(self, petition_title, path_to_file_out, file_out, page, page_size):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()
	prdb = pet_res_db.Reasons_DB() 

	if not os.path.exists(path_to_file_out) and page_size > 1:
	    
	    os.makedirs(path_to_file_out)

	pid = str(self.get_petition_id(petition_title))

	reasons_url = 'http://api.change.org/v1/petitions/' + pid + '/reasons'

	parameters  = { 'api_key': api, 'page_size': page_size, 'page': str(page)}

        reasons_req = requests.get(reasons_url, params=parameters)

	o_file = open(path_to_file_out + '/' + file_out, 'w')
	
	reasons_res = reasons_req.json()

	prdb.insert(reasons_res, pid)


	return reasons_res['total_pages']

#	o_file.write(json.dumps(reasons_res))


    def get_all_reasons(self, path_to_file_out, in_file, page_size):

        i_file = open(in_file, 'r')

	sc = petition_reasons_converter.Reason_Converter()

	for title in i_file:

	    pages = int(self.get_pages(title, 1))

            pages += 1

	    for i in range(1, pages):

		reasons_out = 'reasons_pg_' + str(i) + '.reasonstmp'

		self.get_reasons(title, path_to_file_out + '/' + str(date.today()), reasons_out, str(i), page_size)

		if (int(page_size) > 1):
		    
		    sc.converter( str(date.today()), path_to_file_out + '/' + str(date.today()) + '/' + 
			    reasons_out, path_to_file_out + '/' , title.strip() + '-' + 'page_' + str(i) + '.reasons')


        if (int(page_size) > 1):
	    
	    self.concat_files('reasons', path_to_file_out + '/' + str(date.today()) + '/', path_to_file_out + 
		    '/' + str(date.today()) + '/' + title.strip() )


    def get_organization_id(self, url):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	if (url is not None):
	    
	    org_id_url = 'https://api.change.org/v1/organizations/get_id?organization_url=' + url

            parameters  = { 'api_key': api }

	    org_id_req = requests.get(org_id_url, params=parameters)

	    org_id_res = org_id_req.json()

	else:

	    org_id_res = 'None Given'

	return org_id_res


    def get_organization_record(self, org_id):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	org_url = 'https://api.change.org/v1/organizations/' + org_id

        parameters  = { 'api_key': api }

	org_req = requests.get(org_url, params=parameters)

	org_res = org_req.json()

	return org_res

    def get_target_record(self, pid):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	org_url = 'https://api.change.org/v1/petitions/' + str(pid) + '/targets'

        parameters  = { 'api_key': api }

	org_req = requests.get(org_url, params=parameters)

	org_res = org_req.json()

	return org_res


    def get_user_id(self, url):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

        parameters  = { 'api_key': api }

	user_req = requests.get('https://api.change.org/v1/users/get_id?user_url=' + url, params=parameters)

	user_id = user_req.json()

	return user_id

    def get_user_record(self, uid):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

        parameters  = { 'api_key': api }

	user_rec_req = requests.get('https://api.change.org/v1/users/' + uid, params=parameters)

	user_rec = user_rec_req.json()

	return user_rec










