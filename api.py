import requests
import settings

base = 'https://api.nextdns.io'
headers = {'X-Api-Key': settings.api_key}


def get(path):
  res = requests.get(f'{base}/{path}', headers=headers)
  return res.json()

def delete(path):
  url = f'{base}/{path}'
  print(f'DELETE {url}')
  res = requests.delete(url, headers=headers)
  try:
    return res.json()
  except:
    return res.text

def patch(path, data):
  url = f'{base}/{path}'
  print(f'PATCH {url}')
  res = requests.patch(url, headers=headers, json=data)
  try:
    return res.json()
  except:
    return res.text
