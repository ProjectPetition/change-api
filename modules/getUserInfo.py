import requests

class GetUserInfo:
    
    def get_user_id(self, url):

	config = open('config/api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

        parameters  = { 'api_key': api }

	user_req = requests.get('https://api.change.org/v1/users/get_id?user_url=' + url, params=parameters)

	user_id = user_req.json()

	return user_id

    def get_user_record(self, uid):

	config = open('api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

        parameters  = { 'api_key': api }

	user_rec_req = requests.get('https://api.change.org/v1/users/' + uid, params=parameters)

	user_rec = user_rec_req.json()

	return user_rec


