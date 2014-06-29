import time
import sys

sys.path.append('/home/tim/Philosophy/Computer_Science/We_The_People_Project')
import change_org_collection
import changeDB

sys.path.append('change_org_db_interface/organizations_db')
import pet_org_db

sys.path.append('change_org_db_interface/targets_db')
import pet_targ_db

sys.path.append('change_org_db_interface/users_db')
import pet_users_db


class Body_DB: 

    def insert(self, raw_body):

	pet_body = changeDB.Petitions()
        ptdb = pet_targ_db.Targ_DB()	
	coc = change_org_collection.Change_Org_Collection()
	podb = pet_org_db.Org_DB()
	pet_targ = changeDB.Target()
	pet_users = pet_users_db.Users_DB()

	date_time = raw_body['created_at'].replace('T', ' ').replace('Z', '')
	date_time_two = raw_body['end_at'].replace('T', ' ').replace('Z', '')

        try:
            
	    org_id = coc.get_organization_id(raw_body['organization_url'])['organization_id']

	except:

	    org_id = 0

	dt = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")
	dt_two = time.strptime(date_time_two, "%Y-%m-%d %H:%M:%S")

	pet_body.create( category = raw_body['category'], 
		created_at = time.strftime('%Y-%m-%d %H:%M:%S', dt), 
		end_at = time.strftime('%Y-%m-%d %H:%M:%S', dt_two), 
		goal = raw_body['goal'], image_url = raw_body['image_url'], overview = raw_body['overview'],
		letter_body = raw_body['letter_body'], petition = raw_body['petition_id'], 
		signature_count = raw_body['signature_count'], status_petition = raw_body['status'], title = raw_body['title'],
		url = raw_body['url'], organization = org_id)

	try:
	    
	    podb.insert(coc.get_organization_record(str(org_id)))
	
	except:

	    print "No Organization Listed\n"


	try:
	    
	    targ_rec =  coc.get_target_record(raw_body['petition_id'])

	except:

	    print "No Target Listed\n"

	try:
	    
	    ptdb.insert(targ_rec, raw_body['petition_id'])

	    targ_id = pet_targ.get(changeDB.Target.petition == raw_body['petition_id'])
            body_query = pet_body.get(changeDB.Petitions.petition == raw_body['petition_id'])
	    body_query.target = targ_id.id
	    body_query.save()

	except:

	    print "No Target Record to insert\n"

	try:

	    end_url = raw_body['creator_url'].split('/')[4]

	    if (self.is_number(end_url) != False):

		pet_users.insert( coc.get_user_record(end_url), raw_body['creator_url'])

	    else:

		uid = coc.get_user_id(raw_body['creator_url'])
		pet_users.insert( coc.get_user_record(uid), raw_body['creator_url'])


	except:

	    print "No User Record to create\n"

    def is_number(self, number):

	try:

	    float(number)
	    
	except:

	    return False










