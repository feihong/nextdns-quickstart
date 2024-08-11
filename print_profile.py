import sys
import api
import pprint

id = sys.argv[1]
data = api.get(f'profiles/{id}')
pprint.pprint(data)
