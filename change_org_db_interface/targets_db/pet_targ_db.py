import sys

sys.path.append('/home/tim/Philosophy/Computer_Science/We_The_People_Project')
import changeDB


class Targ_DB: 

    def insert(self, raw_org, pid):


	pet_targ = changeDB.Target()

	for rec in raw_org:

	    pet_targ.create( petition = pid, 
	   	    name = rec['name'], 
#		    target_area = rec['target_area'], 
		    title = rec['title'], 
		    type = rec['type'])



