class GetPages:
    
    def get_pages(self, title, reasons):

	if (int(reasons) == 0):
	    
	    pages = self.get_signatures(title, 'temp.tmp', '1', 1, 0)

	elif (int(reasons) == 1):

	    pages = self.get_reasons(title, '.', 'temp.tmp', '1', '1')

	return pages
 
