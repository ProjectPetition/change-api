import json
import requests
import modules



class GetSignatures:


    def get_signatures(self, petition_title, out_file, page_num, page_size, temp):

	config = open('config/api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	psdb = modules.petition_signatures_db() 

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

	sc = modules.sig_conv()

	pages = int(self.get_pages(title, 0))

        pages += 1

	for i in range(1, pages):

	    sig_out = 'sig_pg_' + str(i) + '.sigtmp'

	    self.get_signatures(title, sig_out, str(i), page_size, 1)

	    if (page_size > 1):
	    
		sc.converter(date, sig_out, path_to_file_out + '/', title + '-' + 'page_' + str(i) + '.sig')

        if (page_size > 1):
	
	    self.concat_files('sig', path_to_file_out + '/' + date + '/', path_to_file_out + '/' + date + '/' + title )

