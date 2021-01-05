import requests
import json
host = "https://www.virustotal.com/gui/"  # example URL
res = requests.get(host)
res
res.url
res.status_code
res.raise_for_status()
my_params = {'id': '@', 'pass': '@'}
requests.get(host, params=my_params)
my_data = json.dumps({'id': '@', 'pass': '@'})
my_data
my_header = {'my_header': 'value'}
my_cookies = {'session_id': 'cookie'}
res = requests.get(host, headers=my_header, cookies=my_cookies)
res
