import csv
import glob
from itertools import izip

class Reasons_Converter:

    def convert(self, json_file, csv_file):


	in_file = open(json_file, 'r')
	out_file = open(csv_file, 'ab')

	write_csv = csv.writer(out_file, delimiter=',')

	out_file.write('reasons\ncreated at,content,like count,author first name,author last name,author url\n\n')

        inc_line = in_file.read()

	text = inc_line.split('\n')

	nl_text = str(text).split(',')

	header = dict()
	reasons = dict()

	for line in nl_text:

	    if ('"page":' in line):

		page = line.split(':')

		header.setdefault('page', [])

		header['page'].append(page[1])

	    if ('"prev_page_endpoint":' in line):

		prev_page = line.split(':')

		header.setdefault('prev_page', [])

		if (len(prev_page) > 2):

		    header['prev_page'].append(prev_page[1] + ':' + prev_page[2])

	        else:

		    header['prev_page'].append('NULL')

            if ('"next_page_endpoint":' in line):

	       next_page = line.split(':')

	       header.setdefault('next_page', [])

	       if (len(next_page) > 2):

		   header['next_page'].append(next_page[1] + ':' + next_page[2])

	       else:

		   header['next_page'].append("NULL")

            if ('"total_pages":' in line):

		total_pages = line.split(':')

		header.setdefault('total_pages', [])

		header['total_pages'].append(total_pages[1])

	    if ('"created_at":' in line):

		created_at = line.split(':')

		reasons.setdefault('created_at', [])

		reasons['created_at'].append(created_at[1].strip('"'))
            
	    if ('"content":' in line):

		content = line.split(':')

		reasons.setdefault('content', [])

		reasons['content'].append(content[1].strip('"'))

	    if ('"like_count":' in line):

		like_count = line.split(':')

		reasons.setdefault('like_count', [])

		reasons['like_count'].append(like_count[1])

            if ('"author_name":' in line):

		name =  line.split(':')

		reasons.setdefault('first', [])
		reasons.setdefault('last', [])

		if (len(name) > 2):

		    first_last = str(name[2]).split(' ')


		    if (len(first_last) > 1):
			
			reasons['first'].append(str(first_last[0].strip('"')))
		        reasons['last'].append(str(first_last[1].strip('"')))

		    else:

			reasons['first'].append('Unknown')
			reasons['last'].append('Unknown')


	        else:

		    first_last = str(name[1]).split(' ')


		    if (len(first_last) > 1):
			
			reasons['first'].append(str(first_last[0].strip('"')))
		        reasons['last'].append(str(first_last[1].strip('"')))

		    else:

			reasons['first'].append('Unknown')
			reasons['last'].append('Unknown')

	    if ('"author_url":' in line):

		author_url = line.split(':')

                reasons.setdefault('author_url', [])

		reasons['author_url'].append(author_url[1].strip('"') + ':' + author_url[2].strip('"}]')) 

 

        reasons['created_at'].pop(0)
        out_file.write('\n')

	for i in izip(reasons['created_at'], reasons['content'], reasons['like_count'], reasons['first'], reasons['last'], reasons['author_url']):

	    write_csv.writerow(i)
	    out_file.write('\n')



    def convert_me(self):

	files = glob.glob('data/*.sig')

	for f_in in files:

            self.convert(f_in, 'data/csv/' + f_in.strip('data/') + '.csv')



