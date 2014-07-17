import getopt, sys
import petition_body_converter

def main(argv):

    pbc = petition_body_converter.Petition_Body_Converter()

    opts, args = getopt.getopt(argv, "i:o:d:")

    for opt, arg in opts:

	if (opt == '-i'):

	    in_file = arg
	
        if (opt == '-o'):

	    out_file = arg

	if (opt == '-d'):

	    date = arg

    pbc.convert_me(date)

if __name__ =='__main__':

    main(sys.argv[1:])



	


