import dryscrape
import time

class ChangeSearch:


    def search(self, keyword, file_out):

	href = open(file_out, 'ab')

        sess = dryscrape.Session(base_url = 'http://api.change.org')

        sess.set_attribute('auto_load_images', False)

        sess.visit('')
        q = sess.at_xpath('//*[@name="q"]')
        q.set(keyword)
        q.form().submit()

        time.sleep(3)

        for link in sess.xpath('//*[@href]'):

               href.write(link['href'] + '\n')

        href.close()

        self.get_titles(file_out, 'titles.txt')
	self.get_next_page(file_out)

