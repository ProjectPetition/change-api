import json
import os
import glob

class Signature_Converter: 

    def converter(self, date, raw_sig, out_path, outfile):

	if not os.path.exists(out_path):

	    os.makedirs(out_path)
	
	    if not os.path.exists(out_path + date):
	    
	        os.makedirs(out_path + '/' + date)


	in_file = open(raw_sig, 'r')

	out_file = open(out_path + '/' + date + '/' + outfile, 'wb')


	data = []

        data = json.load(in_file)


	out_file.write(str(data['page']) + ',' + str(data['total_pages']) + ',' + str(data['signature_count']) + '\n')



	for sig in data['signatures']:

	    if (sig['city'] is None):

		sig['city'] = 'None'

	    if (sig['state_province'] is None):

		sig['state_province'] = 'None'

	    if (sig['country_code'] is None):

		sig['country_code'] = 'None'

            if (sig['country_name'] is None):

		sig['country_name'] = 'None'

	    out_file.write(',,,')
	    out_file.write(str(sig['name'].encode('ascii', 'ignore')) + ',' + str(sig['city'].encode('ascii', 'ignore').replace(',', ' ')) + ','  + str(sig['state_province'].encode('ascii', 'ignore')) + ',' + str(sig['country_code'].encode('ascii', 'ignore')) + ',' + str(sig['country_name'].encode('ascii', 'ignore')) + ',' + str(sig['signed_at']))
	    out_file.write('\n')


        out_file.close()

    def convert_multiple(self, date, path_to_file_in, path_to_file_out):

	if not os.path.exists(path_to_file_out + date):
	    
	    os.makedirs(path_to_file_out + date)

	files = glob.glob(path_to_file_in + '/*.sig')

	for f_in in files:

	    f_name = f_in.split('/')

            self.converter(f_in, path_to_file_out + date + '/' + f_name[4] + '_sig.csv')












