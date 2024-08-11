import api
import pprint

data = api.get('profiles')
pprint.pprint(data)
