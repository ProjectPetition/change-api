import petitions_signature_converter
import getopt, sys

def main(argv):
    pbc = petitions_signature_converter.Signature_Converter()

    opts, args = getopt.getopt(argv, "i:o:d:a:")

    for opt, arg in opts:

	if (opt == '-i'):

	    in_file_path = arg
	
        if (opt == '-o'):

	    out_file_path = arg

	if (opt == '-d'):

	    date = arg

	if (opt == '-a'):

	    out_file = arg

    pbc.converter(date, in_file_path, out_file_path, out_file)

if __name__ =='__main__':

    main(sys.argv[1:])



