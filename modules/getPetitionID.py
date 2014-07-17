import requests

class GetPetitionID:


    def get_petition_id(self, petition_name):

	config = open('config/api_key', 'r')
        api = config.read().replace('\n', '')
        config.close()

        petition_url = 'http://www.change.org/petitions/' + petition_name
        
	query_url = 'https://api.change.org/v1/petitions/get_id'

        parameters  = { 'api_key': api, 'petition_url': petition_url }

	r = requests.get(query_url, params=parameters)

	response = r.json()

	pet_id = response['petition_id']

        return pet_id


