import requests
import changeOrgDBInterface

pbdb = changeOrgDBInterface.pet_Body_DB()


class GetPetText:


    def get_petition_text(self, petition_title, out_file):

	config = open('config/api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

#        pbdb = pet_body_db.Body_DB() 

	o_file = open(out_file, 'wb')

	pid = str(self.get_petition_id(petition_title))
		
	body_url = 'http://api.change.org/v1/petitions/' + pid

        parameters  = { 'api_key': api }

	body_req = requests.get(body_url, params=parameters)

	body_res = body_req.json()

	pbdb.insert(body_res)

	
        #o_file.write(json.dumps(body_res))


