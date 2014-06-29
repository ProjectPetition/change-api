import sys

sys.path.append('/home/tim/Philosophy/Computer_Science/We_The_People_Project')
import changeDB


class Users_DB: 

    def insert(self, raw_user, u_url):


	pet_users = changeDB.Users()

	pet_users.create( state_province = raw_user['state_province'], 
   	    city = raw_user['city'], 
	    user = raw_user['user_id'], 
	    name = raw_user['name'],
	    location = raw_user['location'],
	    country_code = raw_user['country_code'],
	    country_name = raw_user['country_name'],
	    user_url = u_url)



