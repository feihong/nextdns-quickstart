# Feihong's NextDNS Quickstart

## Setup

See https://my.nextdns.io/setup > Setup Guide and click on your OS.

On ChromeOS, every app uses whatever is in System Settings.

On MacOS, most browsers need to be configured individually because they don't use the System Settings. Firefox seems to be the lone exception.

## Download logs

Click http://my.nextdns.io/ > Settings > Logs > Download logs.

Using API key:

```bash
curl -L -H "X-Api-Key: <api key>" https://api.nextdns.io/profiles/<profile>/logs/download -o logs.csv
```

## Links

- API key is viewable at bottom of [account page](https://my.nextdns.io/account)
- [API docs](https://nextdns.github.io/api/)

## Notes

It's totally possible to delete TLDs one by one:

```python
tld_ids = [e['id'] for e in security['tlds']]

for tld_id in tld_ids:
  hex_id = ''.join([f'{ord(c):0X}' for c in tld_id])
  print(f'Deleting {tld_id}, hex:{hex_id}')
  api.delete(f'profiles/{profile_id}/security/tlds/hex:{hex_id}')
```

But this is very slow. If you want to delete all TLDs, it's better to delete
them all at once by making a PATCH request to `/profiles/:profile/security` with
`{"tlds": []}` as the payload.
