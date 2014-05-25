import dryscrape
import time
import csv
import os
import change_org_collection
from datetime import date

class Change_Org_Search:

    def search(self, keyword, file_out):

	href = open(file_out, 'ab')

# set up a web scraping session
        sess = dryscrape.Session(base_url = 'http://api.change.org')

#we don't need images
        sess.set_attribute('auto_load_images', False)

# visit homepage and search for a term
        sess.visit('')
        q = sess.at_xpath('//*[@name="q"]')
        q.set(keyword)
        q.form().submit()

        time.sleep(3)

#extract all links
        for link in sess.xpath('//*[@href]'):

               href.write(link['href'] + '\n')

        href.close()

        self.get_titles(file_out, 'titles.txt')
	self.get_next_page(file_out)

    def scrape_page(self, url, file_out):

	href = open(file_out, 'ab')
	href_tmp = open('lnks.tmp', 'w')

	sess = dryscrape.Session(base_url = url)

	sess.visit('')

	time.sleep(15)

	for link in sess.xpath('//*[@href]'):

	    href.write(link['href'] + '\n')
	    href_tmp.write(link['href'] + '\n')

	href.close()
	href_tmp.close()

#	self.get_titles(file_out, 'titles.txt')
#	self.get_next_page('lnks.tmp')
#	os.remove('lnks.tmp')

        sess.render('change_org.png')

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

    def get_next_page(self, file_in):

	f_in = open(file_in, 'r')
	pages = open('pages.txt', 'w')

	for line in f_in:

	    if ('search' in line):

		print line
                #pages.write(line)

        pages.close()

	pages = open('pages.txt', 'r')

	line = pages.readline()

	print line

	self.scrape_page(line, 'links.txt')

	pages.close()

	os.remove('pages.txt')

    def get_topics(self, results_file):

	links = open(results_file, 'r')
	topics = open('topics.txt', 'ab')

	reader = csv.reader(links, delimiter= '/')

	for line in reader:

	    if ('topics' in line):

		topics.write(line[4] + '\n')

    def get_most_recent(self, f_out):

	pgs = 1 
        href = open(f_out, 'w')


        sess = dryscrape.Session(base_url = 'http://api.change.org')
        
        sess.set_attribute('auto_load_images', False)

	sess.visit('/petitions#most-recent')

        time.sleep(5)
     
        for i in range(pgs):

	    pages = "page_" + str(i)

	    print pages

	    for link in sess.xpath('//*[@href]'):

		href.write(link['href'] + '\n')
	    
	    next_page = sess.at_xpath('//*[@class="next button"]')
	    next_page.click()
	
            time.sleep(5)

	href.close()

	self.get_most_recent_titles(f_out)

    def get_most_recent_titles(self, most_recent):

	recent = open(most_recent, 'r')

	output = open('recent_titles.txt', 'ab')

        reader = csv.reader(recent, delimiter = '/')
	lines_seen = set()

	for line in reader:

	    if (len(line) > 5 and line[3] == 'en-CA' and line[4] == 'petitions' and line[5] not in lines_seen):

		output.write(line[5] + '\n')
		lines_seen.add(line[5])

        recent.close()
	output.close()

	self.collect_pet_and_sig('recent_titles.txt')

    def collect_pet_and_sig(self, recent_file):

	titles = open(recent_file, 'r')
	coc = change_org_collection.Change_Org_Collection()

	if not os.path.exists('data/' + str(date.today())):
	    
	    os.makedirs('data/' + str(date.today()))

	for line in titles:

	    wo_newline = line.strip()

	    coc.get_petition_text(wo_newline, 'data/' + str(date.today()) + '/' + line)
            coc.get_all_signatures(wo_newline)





	    

	









    

