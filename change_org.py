import change_org_collection, change_org_search
import getopt, sys

def main(argv):

    outfile = ''

    co = change_org_collection.Change_Org_Collection()
    sc = change_org_search.Change_Org_Search()

    opts, args = getopt.getopt(argv, "u:s:g:o:p:m:n:a:b:r")

    for opt, arg in opts:

	if opt == "-u":

	    title = arg
            co.get_petition_id(title)
	
	if opt == "-s":
            
	    search = arg
	    sc.search(search, outfile)

        if opt == "-n":

	    page = arg

        if opt == "-g":

	    title = arg
	    co.get_signatures(title, outfile, page)

        if opt == "-o":

	   outfile = arg

	if opt == "-p":

	    title = arg
	    co.get_petition_text(title, outfile)

        if opt == "-m":

	    f_parse = arg
	    co.results_parse(f_parse, outfile)

	if opt == "-b":

	    title = arg
	    co.get_pages(title)

	if opt == "-a":

	    title = arg
	    co.get_all_signatures(title)

        if opt == "-r":

	    sc.get_most_recent(outfile)


if __name__ =='__main__':

    main(sys.argv[1:])




