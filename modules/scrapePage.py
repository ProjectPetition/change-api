import dryscrape
import time

class Scrape_Page:

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

