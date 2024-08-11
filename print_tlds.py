import sys
import api
import pprint

profile_id = sys.argv[1]
data = api.get(f'profiles/{profile_id}/security')
# pprint.pprint(data)

security = data['data']

tld_ids = [e['id'] for e in security['tlds']]
for i, tld_ids in enumerate(tld_ids, 1):
  print(f'{i}. {tld_ids}')

# # Delete all TLDs:
# api.patch(f'profiles/{profile_id}/security', {'tlds': []})
