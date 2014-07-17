import requests

class GetOrgInfo:
    
    def get_organization_id(self, url):

	config = open('config/api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	if (url is not None):
	    
	    org_id_url = 'https://api.change.org/v1/organizations/get_id?organization_url=' + url

            parameters  = { 'api_key': api }

	    org_id_req = requests.get(org_id_url, params=parameters)

	    org_id_res = org_id_req.json()

	else:

	    org_id_res = 'None Given'

	return org_id_res


    def get_organization_record(self, org_id):

	config = open('config/api_key', 'r')
	api = config.read().replace('\n', '')
	config.close()

	org_url = 'https://api.change.org/v1/organizations/' + org_id

        parameters  = { 'api_key': api }

	org_req = requests.get(org_url, params=parameters)

	org_res = org_req.json()

	return org_res

