import petitions_body_converter
import getopt, sys

def main(argv):
    pbc = petitions_body_converter.Body_Converter()

    opts, args = getopt.getopt(argv, "i:o:d:")

    for opt, arg in opts:

	if (opt == '-i'):

	    in_file_path = arg
	
        if (opt == '-o'):

	    out_file_path = arg

	if (opt == '-d'):

	    date = arg

    pbc.convert_multiple(date, in_file_path, out_file_path)

if __name__ =='__main__':

    main(sys.argv[1:])



