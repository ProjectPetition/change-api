import sys
import time

sys.path.append('/home/tim/Philosophy/Computer_Science/We_The_People_Project')
import changeDB


class Reasons_DB: 

    def insert(self, raw_res, pid):


	pet_res = changeDB.Reasons()

	for reason in raw_res['reasons']:

            date_time = reason['created_at'].replace('T', ' ').replace('Z', '')
	    
            dt = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")

	
	    pet_res.create(created_on = time.strftime('%Y-%m-%d %H:%M:%S', dt),
		    content = reason['content'],
		    like_count = reason['like_count'],
		    author_name = reason['author_name'],
		    author_url = reason['author_url'],
		    petition = int(pid))




