import peewee
import csv
import getopt, sys

class DBConnector:

    def connectdb(self, config):

	conf = open(config, 'r')

	conf_parser = csv.reader(conf, delimiter=',')


	for item in conf_parser:

	    user_name = item[0]
	    password = item[1]
	
	change_database = peewee.MySQLDatabase('changeDB', user=user_name, passwd=password)

	change_database.connect()

	return change_database

def main(argv):

    connect = DBConnector()

    f_in = ''

    opts, args = getopt.getopt(argv, "i:")

    for opt, arg in opts:

        if (opt == "-i"):

	   f_in = arg

    return connect.connectdb(f_in)

if __name__ =='__main__':

    main(sys.argv[1:])






