import os
import requests
from datetime import date
import converters
import changeOrgDBInterface



class GetReasons:
    
    def get_reasons(self, petition_title, path_to_file_out, file_out, page, page_size):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()
	prdb = changeOrgDBInterface.petition_reasons_db() 

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

	sc = converters.reasons_conv()

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

