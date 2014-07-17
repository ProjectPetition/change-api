import requests

class GetTargRec:
    
    def get_target_record(self, pid):

	config = open('config/api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	org_url = 'https://api.change.org/v1/petitions/' + str(pid) + '/targets'

        parameters  = { 'api_key': api }

	org_req = requests.get(org_url, params=parameters)

	org_res = org_req.json()

	return org_res


