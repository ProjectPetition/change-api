import modules
import getopt, sys

def main(argv):

    outfile = ''
    infile = ''

    gpid = modules.get_pet_id()
    search = modules.change_search()
    gsig = modules.get_signatures()
    gpettxt = modules.pet_text()
    gpgs = modules.get_pgs()
    gmr = modules.most_recent()
    gar = modules.get_reasons() 
    cps = modules.collect_pet_sig()

    opts, args = getopt.getopt(argv, "i:k:u:s:g:o:p:n:a:b:rcd:ef:h:j:")

    for opt, arg in opts:

	if (opt == "-k"):

	    sig_or_reason = arg

	if (opt == "-j"):

	    page_size = arg		

        if (opt == "-d"):

	    date = arg

        if opt == "-u":

	    title = arg
            gpid.get_petition_id(title)
	
	if opt == "-s":
            
	    search = arg
	    search.search(search, outfile)

        if opt == "-n":

	    page = arg

        if opt == "-g":

	    title = arg
	    gsig.get_signatures(title, outfile, page, page_size)

	if opt == "-h":

	    path_to_file_out = arg

        if opt == "-o":

	   outfile = arg

	if opt == "-p":

	    title = arg
	    gpettxt.get_petition_text(title, outfile)

	if opt == "-b":

	    title = arg
	    gpgs.get_pages(title, sig_or_reason)

	if opt == "-a":

#	    title = arg
#	    gsig.get_all_signatures(date, path_to_file_out, title, page_size)
 
            cps.collect_pet_and_sig(date, infile, page_size)
            gar.get_all_reasons(path_to_file_out, infile, page_size)


        if opt == "-r":

	    gmr.get_most_recent(outfile)
	   
	if opt == "-c":  

	    gar.get_all_reasons(path_to_file_out, infile, page_size)

	if opt =="-i":

	    infile = arg


        if opt == "-e":

            cps.collect_pet_and_sig(date, infile, page_size)



if __name__ =='__main__':

    main(sys.argv[1:])




