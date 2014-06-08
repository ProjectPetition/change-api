import csv
import glob
from itertools import izip
import os

class Json_To_Csv:

    def convert(self, json_file, csv_file):


	in_file = open(json_file, 'r')
	out_file = open(csv_file, 'ab')

	write_csv = csv.writer(out_file, delimiter=',')

	out_file.write('page,total pages,signature count,signatures\n,,,name,,city,state/province,country code,country name,signed at\n,,,First,Last\n\n')

        inc_line = in_file.read()

	text = inc_line.split(',')

	final = dict()

	for line in text:

	    if ('"page":' in line):

		page_no = line.split(':')
	        
		out_file.write(page_no[1])

	    if ('"total_pages":' in line):

		pages = line.split(':')

                out_file.write(',' + pages[1])

	    if ('"signature_count":' in line):

		sig_cnt = line.split(':')

		out_file.write(',' + sig_cnt[1])

            if ('"name":' in line):

		name =  line.split(':')


		if (len(name) > 2):

		    first_last = str(name[2]).split(' ')



		    final.setdefault('first', [])
		    final.setdefault('last', [])

		    if (len(first_last) > 1):
			
			final['first'].append(str(first_last[0].strip('"')))
		        final['last'].append(str(first_last[1].strip('"')))

		    else:

			final['first'].append('Unknown')
			final['last'].append('Unknown')


	        else:

		    first_last = str(name[1]).split(' ')


		    if (len(first_last) > 1):
			
			final['first'].append(str(first_last[0].strip('"')))
		        final['last'].append(str(first_last[1].strip('"')))

		    else:

			final['first'].append('Unknown')
			final['last'].append('Unknown')
                   

	    if ('"city":' in line):

		city = line.split(':')

		final.setdefault(city[0].strip('[{"'), [])

		final[city[0].strip('{"')].append(str(city[1].strip('"')))

            if ('"state_province":' in line):

		state_province = line.split(':')

		final.setdefault(state_province[0].strip('[{"'), [])

		final[state_province[0].strip('{"')].append(str(state_province[1].strip('"')))

            if ('"country_code":' in line):

		country_code = line.split(':')

		final.setdefault(country_code[0].strip('[{"'), [])

		final[country_code[0].strip('{"')].append(str(country_code[1].strip('"')))

            if ('"country_name":' in line):

		country_name = line.split(':')

		final.setdefault(country_name[0].strip('[{"'), [])

		final[country_name[0].strip('{"')].append(str(country_name[1].strip('"')))

	    if ('"signed_at":' in line):

		signed_at = line.split(':')

		final.setdefault(signed_at[0].strip('[{"'), [])

		final[signed_at[0].strip('{"')].append(str(signed_at[1].strip('"')))

        out_file.write('\n')

        for i in izip(final['first'], final['last'], final['city'], final['state_province'], final['country_code'], final['country_name'], final['signed_at']):

	    out_file.write(',,,')
	    write_csv.writerow(i)
	    out_file.write('\n')


	in_file.close()
	out_file.close()

    def convert_me(self, date):

	if not os.path.exists('data/sig_csv/' + date):
	    
	    os.makedirs('data/sig_csv/' + date)

	
	files = glob.glob('data/sig_csv_raw/' + date + '/' + '*.sig.cat')

	for f_in in files:


	    f_name =  f_in.split('/')

            self.convert(f_in, 'data/sig_csv/' + date + '/' + f_name[3] + '.csv')



