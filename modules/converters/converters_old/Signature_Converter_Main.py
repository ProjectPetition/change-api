import getopt, sys
import signature_converter

def main(argv):

    jtc = signature_converter.Json_To_Csv()

    opts, args = getopt.getopt(argv, "i:o:d:")

    for opt, arg in opts:

	if (opt == '-i'):

	    in_file = arg
	
        if (opt == '-o'):

	    out_file = arg

	if (opt == '-d'):

	    date = arg

    jtc.convert_me(date)

if __name__ =='__main__':

    main(sys.argv[1:])



	


