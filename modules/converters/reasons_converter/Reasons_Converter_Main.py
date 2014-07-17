import getopt, sys
import reasons_converter

def main(argv):

    rc = reasons_converter.Reasons_Converter()

    opts, args = getopt.getopt(argv, "i:o:")

    for opt, arg in opts:

	if (opt == '-i'):

	    in_file = arg
	
        if (opt == '-o'):

	    out_file = arg

    rc.convert(in_file, out_file)

if __name__ =='__main__':

    main(sys.argv[1:])



	


