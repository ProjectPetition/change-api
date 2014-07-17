import csv

class Get_Topics:
    
    def get_topics(self, results_file):

	links = open(results_file, 'r')
	topics = open('topics.txt', 'ab')

	reader = csv.reader(links, delimiter= '/')

	for line in reader:

	    if ('topics' in line):

		topics.write(line[4] + '\n')

        links.close()


