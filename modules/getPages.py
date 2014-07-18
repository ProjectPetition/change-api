import getSignatures
import getReasons

class GetPages:
    
    def get_pages(self, title, reasons):

	gs = getSignatures.GetSignatures()
	gr = getReasons.GetReasons()

	if (int(reasons) == 0):
	    
	    pages = gs.get_signatures(title, 'temp.tmp', '1', 1, 0)

	elif (int(reasons) == 1):

	    pages = gr.get_reasons(title, '.', 'temp.tmp', '1', '1')

	return pages
 
