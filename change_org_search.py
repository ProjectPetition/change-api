import dryscrape
import time
import csv
import os
import change_org_collection
from datetime import date
import random

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

	f_in.close()
	pages.close()

	os.remove('pages.txt')

    def get_topics(self, results_file):

	links = open(results_file, 'r')
	topics = open('topics.txt', 'ab')

	reader = csv.reader(links, delimiter= '/')

	for line in reader:

	    if ('topics' in line):

		topics.write(line[4] + '\n')

        links.close()

    def get_most_recent(self, f_out):

	pgs = 30 
        href = open(f_out, 'w')


        sess = dryscrape.Session(base_url = 'http://api.change.org')

	sess.set_header("User-Agent", 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0')

        sess.set_attribute('auto_load_images', False)

	sess.visit('/petitions#most-recent')

        time.sleep(5)
     
        for i in range(pgs):

	    time_sec = random.uniform(0, 20)

	    print time_sec

	    pages = "page_" + str(i)

	    print pages
	    sess.render(pages + '.png')

	    for link in sess.xpath('//*[@href]'):

		href.write(link['href'] + '\n')
	    
	    next_page = sess.at_xpath('//*[@class="next button"]')
	    
	    time.sleep(time_sec)
	    
	    next_page.click()
	
            time.sleep(5)

	href.close()

	self.get_most_recent_titles(f_out)

    def get_most_recent_titles(self, most_recent):

	recent = open(most_recent, 'r')

	output = open('recent_titles_rough.txt', 'ab')

        reader = csv.reader(recent, delimiter = '/')
	lines_seen = set()

	for line in reader:

	    if (len(line) > 5 and line[3] == 'en-CA' and line[4] == 'petitions' and line[5] not in lines_seen):

		output.write(line[5] + '\n')
		lines_seen.add(line[5])

        recent.close()
	output.close()


        self.remove_duplicates('recent_titles_rough.txt', 'recent_titles.txt')
	self.collect_pet_and_sig('recent_titles.txt')

    def collect_pet_and_sig(self, path_to_file_out, recent_file):

	titles = open(recent_file, 'r')
	coc = change_org_collection.Change_Org_Collection()

	if not os.path.exists(path_to_file_out + '/' + str(date.today())):
	    
	    os.makedirs(path_to_file_out + '/' + str(date.today()))

	for line in titles:

	    wo_newline = line.strip()

	    coc.get_petition_text(wo_newline, path_to_file_out + '/' + str(date.today()) + '/' + line)
            coc.get_all_signatures(str(date.today()), path_to_file_out, wo_newline)

        titles.close()

	coc.get_all_reasons(path_to_file_out, recent_file)

    def remove_duplicates(self, in_file, out_file):

	i_file = open(in_file, 'r')
	o_file = open(out_file, 'w')

	lines = set()

	for line in i_file:

	    if (line not in lines):

		o_file.write(line)
		lines.add(line)

        i_file.close()
	o_file.close()





	    

	









    

