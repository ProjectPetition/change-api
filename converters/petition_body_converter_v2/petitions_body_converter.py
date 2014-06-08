import json
import os
import glob

class Body_Converter: 

    def converter(self, raw_body, outfile):

	in_file = open(raw_body, 'r')

	out_file = open(outfile, 'wb')

	targets = dict()

	out_file.write('Petition ID,Title,Status,URL,Overview,Targets,,Letter Body,Signature Count,Image URL,Category,Goal,Created At,End At,Creator Name,Creator URL,Organization Name,Organization URL\n')
	out_file.write(',,,,,Name,Type\n')

	data = json.load(in_file)

	targets.setdefault('name', [])
	targets.setdefault('type', [])

	for item in data['targets']:

	    targets['name'] = str(item['name'].encode('ascii', 'ignore'))
	    targets['type'] = str(item['type'].encode('ascii', 'ignore'))

        if (data['creator_name'] is None):

	    data['creator_name'] = "None"


	out_file.write(str(data['petition_id']) + ',' + str(data['title'].encode('ascii', 'ignore')) + ',' + str(data['status']) + ',' + str(data['url']) + ',' + str(data['overview'].encode('ascii', 'ignore').replace(',', " ").replace('\r', " ").replace('\n', " ")) + ',' + str(targets['name']) + ',' + str(targets['type']) + ',' + str(data['letter_body'].encode('ascii', 'ignore')).replace(',', " ") + ',' + str(data['signature_count']) + ',' + str(data['image_url']) + ',' + str(data['category']) + ',' + str(data['goal']) + ',' + str(data['created_at']) + ',' + str(data['end_at']) + ',' + str(data['creator_name'].encode('ascii', 'ignore')) + ',' + str(data['creator_url']) + ',' + str(data['organization_name']) + ',' + str(data['organization_url']))



        out_file.close()

    def convert_multiple(self, date, path_to_file_in, path_to_file_out):

	if not os.path.exists(path_to_file_out + date):
	    
	    os.makedirs(path_to_file_out + date)

	files = glob.glob(path_to_file_in + '/*')

	for f_in in files:

	    f_name = f_in.split('/')


            self.converter(f_in, path_to_file_out + date + '/' + f_name[4] + '_body.csv')












