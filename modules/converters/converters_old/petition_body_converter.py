import csv
import glob
from itertools import izip
import os

class Petition_Body_Converter:

    def convert(self, json_file, csv_file):


	in_file = open(json_file, 'r')
	out_file = open(csv_file, 'ab')

	write_csv = csv.writer(out_file, delimiter=',')

	out_file.write('petition id,title,status,url,overview,targets,,letter body,signature count,image url,category,goal,created at,end at,creator name,,creator url,organization name,organization url\n,,,,,name,type,,,,,,,,First,Last\n\n')

        inc_line = in_file.read()

	text = inc_line.split(',')

	final = dict()
	final_two = dict()

	for line in text:


	    if ('"petition_id":' in line):

		petition_id = line.split(':')

	        
		out_file.write(petition_id[1])

	    if ('"title":' in line):

		title = line.split(':')

                if (len(title) > 2):
		
		    out_file.write(',' + title[1] + title[2])
		else:
		    out_file.write(',' + title[1])

	    if ('"status":' in line):

		status = line.split(':')

		out_file.write(',' + status[1])

            if ('"url":' in line):

		url =  line.split(':')

		if (len(url) > 2):

		    out_file.write(',' + url[1] + ':' + url[2])
		else:

		    out_file.write(',' + url[1])


	    if ('"overview":' in line):

		overview = line.split(':')

		out_file.write(',' + overview[1])


            if ('"targets":' in line):

		targets = line.split(':')


		final.setdefault(targets[0].strip('[{"'), [])

		if (len(targets) > 2):
		


		    final[targets[0].strip('{"')].append(str(targets[1].strip('"')))
		else:
		    
		    final[targets[0].strip('{"')].append('none entered')

            if ('"letter_body":' in line):

	        letter_body = line.split(':')

		out_file.write(',,,' + letter_body[1])


            if ('"signature_count":' in line):

		signature_count = line.split(':')

		out_file.write(',' + signature_count[1])


	    if ('"image_url":' in line):

		image_url = line.split(':')


		if (len(image_url) > 2):

		    out_file.write(',' + image_url[1] + ':' + image_url[2])

		else:

		    out_file.write(',' + image_url[1])

            if ('"category":' in line):

		category = line.split(':')

                out_file.write(',' + category[1])

            if ('"goal":' in line):

		goal = line.split(':')

		out_file.write(',' + goal[1])

	    if ('"created_at":' in line):

		created_at = line.split(':')

		out_file.write(',' + created_at[1].strip('"'))

            if ('"end_at":' in line):

		end_at = line.split(':')

		out_file.write(',' + end_at[1].strip('"'))

 	    if ('"creator_name":' in line):

	       name = line.split(':')


	       if (len(name) > 2):

		    first_last = str(name[2]).split(' ')

		    final_two.setdefault('first', [])
		    final_two.setdefault('last', [])

		    if (len(first_last) > 1):
			
			final_two['first'].append(str(first_last[0].strip('"')))
		        final_two['last'].append(str(first_last[1].strip('"')))

		    else:

			final_two['first'].append('Unknown')
			final_two['last'].append('Unknown')


	       else:

		    first_last = str(name[1]).split(' ')
                    final_two.setdefault('first', [])
		    final_two.setdefault('last', [])



		    if (len(first_last) > 1):
			
			
			final_two['first'].append(str(first_last[0].strip('"')))
		        final_two['last'].append(str(first_last[1].strip('"')))

		    else:

			final_two['first'].append('Unknown')
			final_two['last'].append('Unknown')

	    if ('"creator_url":' in line):

		creator_url = line.split(':')

		final_two.setdefault('creator_url', [])

		if (len(creator_url) > 2):

		    final_two['creator_url'].append(creator_url[1] + ':' + creator_url[2])
		else:

		    final_two['creator_url'].append(creator_url[1])

            if ('"organization_name":' in line):

		organization_name = line.split(':')
		
		final_two.setdefault('organization_name', [])

		final_two['organization_name'].append(organization_name[1])

	    if ('"organization_url":' in line):

	        organization_url = line.split(':')

		final_two.setdefault('organization_url', [])


		if (len(organization_url) > 2):

		    final_two['organization_url'].append(organization_url[1].strip('}') + ':' + organization_url[2])
		else:

		    final_two['organization_url'].append(organization_url[1].strip('}'))



#        out_file.write('\n')

#        for i in izip(final['name'], final['type']):

#	    out_file.write(',,,,')
#	    write_csv.writerow(i)

	for i in izip(final_two['first'], final_two['last'], final_two['creator_url'], final_two['organization_name'], final_two['organization_url']):

	    out_file.write(',')
	    write_csv.writerow(i)


	in_file.close()
	out_file.close()

    def convert_me(self, date):

	if not os.path.exists('data/petition_text/' + date):
	    
	    os.makedirs('data/petition_text/' + date)

	files = glob.glob('data/petition_text_raw/' + date + '/*')

	for f_in in files:

	    f_name = f_in.split('/')

            self.convert(f_in, 'data/petition_text/' + date + '/' + f_name[3] + '_body.csv')



