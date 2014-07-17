import dryscrape
import time
import random
import csv

class GetMostRecent:


    def get_most_recent(self, f_out):

	pgs = 15 
        href = open(f_out, 'w')


        sess = dryscrape.Session(base_url = 'http://api.change.org')

	sess.set_header("User-Agent", 'Mozilla/5.0 (X11; Linux x86; rv:12.0) Gecko/20100101 Firefox/21.0')

        sess.set_attribute('auto_load_images', False)

	sess.visit('/petitions#most-recent')

        time.sleep(5)
     
        for i in range(pgs):

	    i += 1

	    time_sec = random.uniform(0, 20)

	    print time_sec

	    pages = "page_" + str(i)

	    print pages
	    sess.render(pages + '.png')

	    for link in sess.xpath('//*[@href]'):

		href.write(link['href'] + '\n')
	    
#	    next_page = sess.at_xpath('//*[@class="next button"]')
	    
	    time.sleep(time_sec)

	    if (i == 3):

		sess = dryscrape.Session(base_url = 'http://api.change.org')

	    next_link = '/petitions#most-recent/' + str(i) 

	    sess.visit(next_link)
	    
#	    next_page.click()
	
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
	self.collect_pet_and_sig('', 'recent_titles.txt', 1)


