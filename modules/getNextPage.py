import os

class Get_Next_Page:

    def get_next_page(self, file_in):

	f_in = open(file_in, 'r')
        pages = open('pages.txt', 'w')

        for line in f_in:

            if ('search' in line):

	        pages.write(line)

        pages.close()

        pages = open('pages.txt', 'r')

        line = pages.readline()


        self.scrape_page(line, 'links.txt')

        f_in.close()
        pages.close()

        os.remove('pages.txt')

