import csv

class Get_Titles:

    def get_titles(self, file_in, file_out):

	f_in = open(file_in, 'r')
        f_out = open(file_out, 'ab')
        reader = csv.reader(f_in, delimiter = '/')
	lines_seen = set()

	for line in reader:

	    if (len(line) > 4 and line[3] == 'petitions' and line[4] not in lines_seen):

		f_out.write(line[4] + '\n')
		lines_seen.add(line[4])

        f_in.close()
	f_out.close()

