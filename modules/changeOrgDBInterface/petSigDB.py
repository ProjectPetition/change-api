import sys

sys.path.append('/home/tim/Philosophy/Computer_Science/We_The_People_Project')
import changeDB 

class Signature_DB: 

    def insert(self, pid, raw_sig):

	sigs = changeDB.Signatures()

	for sig in raw_sig['signatures']:

	    if (sig['city'] is None):

		sig['city'] = 'None'

	    if (sig['state_province'] is None):

		sig['state_province'] = 'None'

	    if (sig['country_code'] is None):

		sig['country_code'] = 'None'

            if (sig['country_name'] is None):

		sig['country_name'] = 'None'
		

	sigs.create(name = sig['name'], city = sig['city'], state = sig['state_province'], country = sig['country_name'], country_code = sig['country_code'], signed_on = sig['signed_at'], petition = pid)

	    


