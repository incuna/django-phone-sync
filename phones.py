import requests
import re
import time

f = file('FILENAME')

cookies = {'key': 'LOGGEDINCOOKIE'}

r = requests.post(
        'http://domain/settings_phonebook_transfer.html',
        data={'hs_phonebook_transf_radio': '2'},
        files={'tdt_file': f},
        cookies=cookies,
    )

print 'POST'
print r
print r.headers

while True:
    try:
        r = requests.get('http://domain/status.html', cookies=cookies)
    except requests.exceptions.ConnectionError:
        print 'Connection error'
        time.sleep(0.5)
        continue

    print 'GET'
    print r
    print r.headers

    status = filter(lambda ln: re.search('var status', ln), r.content.split('\n'))
    print status[0]
    status = re.search(r'(\d+)', status[0]).groups()
    print status[0]

    time.sleep(0.5)

    if status[0] == '18':
        break

r = requests.get('http://domain/stoptdt.html', cookies=cookies)
print 'GET STOP'
print r
print r.headers
