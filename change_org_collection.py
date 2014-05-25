import urllib
import urllib2
import os
import glob
from datetime import date

class Change_Org_Collection:

    def get_petition_id(self, petition_name):

	config = open('api_key', 'r')
        api = config.read().replace('\n', '')
        config.close()

        petition_url = 'http://www.change.org/petitions/' + petition_name


        query_url = 'https://api.change.org/v1/petitions/get_id'


        parameters  = { 'api_key': api, 'petition_url': petition_url }

        result = urllib.urlencode(parameters)

        request = query_url + '?' + result

        response = urllib2.urlopen(request).read(1000)

        return response

    def get_signatures(self, petition_title, out_file, page_num):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	petition_id = self.get_petition_id(petition_title)
        
	pid_dict = {}

        key,value = petition_id.split(',')

	sec_val = value

        key, value = key.split(':')

	pid_dict[key] = value

	sec_key, sec_value = sec_val.split(':')

	pid_dict[sec_key] = sec_value

	pet_id =  pid_dict['"petition_id"'].split('}')
        
	pid = pet_id[0]
		
	sig_url = 'http://api.change.org/v1/petitions/' + pid + '/signatures'
        
	parameters  = { 'api_key': api }
	
	result = urllib.urlencode(parameters)

	query_parm = '&page_size=500&page=' + page_num

	fin_url = sig_url + '?' + result + query_parm

        print urllib.urlretrieve(fin_url, out_file)

    def get_all_signatures(self, title):

	pages = int(self.get_pages(title))

        pages += 1

	for i in range(1, pages):

	    sig_out = 'sig_pg_' + str(i) + '.sigtmp'

	    self.get_signatures(title, sig_out, str(i))

	self.concat_files('data/' + str(date.today()) + '/' + title.strip())


    def get_petition_text(self, petition_title, out_file):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	petition_id = self.get_petition_id(petition_title)
        
	pid_dict = {}

        key,value = petition_id.split(',')

	sec_val = value

        key, value = key.split(':')

	pid_dict[key] = value

	sec_key, sec_value = sec_val.split(':')

	pid_dict[sec_key] = sec_value

	pet_id =  pid_dict['"petition_id"'].split('}')
        
	pid = pet_id[0]
		
	sig_url = 'http://api.change.org/v1/petitions/' + pid

        parameters  = { 'api_key': api }

        result = urllib.urlencode(parameters)

	fin_url = sig_url + '?' + result
	
	print urllib.urlretrieve(fin_url, out_file.strip())

    def results_parse(self, text_file_in, text_file_out):

        in_file = open(text_file_in, 'r')
	out_file = open(text_file_out, 'w')

	line = in_file.read()

	text = line.split(',')


        for stuff in text:

	    if '"page":' in stuff:

		page = '\n\n' + stuff + '}\n\n'

		out_file.write(page)

	    if '"total_pages":' in stuff:

		total_pages = '{' + stuff + '}\n\n'
		
		out_file.write(total_pages)

	    if '"signature_count":' in stuff:

		signature_count = '{' + stuff + '}\n\n'
		out_file.write(signature_count)

	    if '"name":' in stuff:

		name = stuff + '}\n'

		out_file.write(name)

            if '"city":' in stuff:

		city = '\t{' + stuff + '}\n'
		out_file.write(city)

            if '"state_province":' in stuff:

		state_province = '\t{' + stuff + '}\n'
		out_file.write(state_province)

	    if '"country_code":' in stuff:

		country_code = '\t{' + stuff + '}\n'
		out_file.write(country_code)

	    if '"signed_at":' in stuff:

		signed_at = '\t{' + stuff + '}\n'
		out_file.write(signed_at)

      
    def get_pages(self, title):

	self.get_signatures(title, 'temp.tmp', '1')
       
        temporary = open('temp.tmp', 'r')

	line =  temporary.read()

	text = line.split(',')

	for string in text:

	    if '"total_pages":' in string:

	        pages = string

	pgs_parse = pages.split(':')

	tot_pgs =  pgs_parse[1]

	temporary.close()

	os.remove('temp.tmp')

	return tot_pgs

    def concat_files(self, file_out):

	files = glob.glob('*.sigtmp')

	output_file = open(file_out + '.sig', 'wb')

	for line in files:

	    input_files = open(line, 'r')

	    output_file.write(input_files.read())
	    input_files.close()

	for file_name in glob.glob('*.sigtmp'):
	
	    os.remove(file_name)

        file_parsed = file_out + '_parsed'

        self.results_parse(file_out, file_parsed) 



        



	


	

	






















