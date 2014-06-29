import sys

sys.path.append('/home/tim/Philosophy/Computer_Science/We_The_People_Project')
import changeDB


class Org_DB: 

    def insert(self, raw_org):


	pet_org = changeDB.Organizations()
	
	pet_org.create( address = raw_org['address'], 
		city = raw_org['city'], 
		country_code = raw_org['country_code'], 
		country_name = raw_org['country_name'], location = raw_org['location'], mission = raw_org['mission'],
		name = raw_org['name'], organization = raw_org['organization_id'], 
		organization_url = raw_org['organization_url'], postal_code = raw_org['postal_code'], 
		state_province = raw_org['state_province'], website = raw_org['website'])



