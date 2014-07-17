import json
import os
import glob

class Reason_Converter: 

    def converter(self, date, raw_reasons, out_path, outfile):

	if not os.path.exists(out_path):

	    os.makedirs(out_path)
	
	    if not os.path.exists(out_path + date):
	    
	        os.makedirs(out_path + '/' + date)


	in_file = open(raw_reasons, 'r')

	out_file = open(out_path + '/' + date + '/' + outfile, 'wb')


	data = []

        data = json.load(in_file)


	out_file.write(str(data['page']) + ',' + str(data['total_pages']) + '\n')

	for reasons in data['reasons']:

		out_file.write(',,')
		out_file.write( str(reasons['created_at'].encode('ascii', 'ignore')) + ',' + str(reasons['content'].encode('ascii', 'ignore').replace(',', ' ').replace('\r\n', ' ').replace('"', ' ')) + ',' + str(str(reasons['like_count']).encode('ascii', 'ignore')) + ',' + str(reasons['author_name'].encode('ascii', 'ignore')) + ',' + str(reasons['author_url'].encode('ascii', 'ignore')) + '\n')


    def convert_multiple(self, current_date, path_to_file_in, path_to_file_out):

	if not os.path.exists(path_to_file_out + '/' + current_date):
	    
	    os.makedirs(path_to_file_out + '/' + current_date)

	files = glob.glob(path_to_file_in + '/*.reasonstmp')

	print files

#	for f_in in files:

#	    f_name = f_in.split('/')

#           self.converter(f_in, path_to_file_out + '/' + current_date + '/' + f_name[4] + '_reasons.csv')












