# -*- coding: utf-8 -*-

import requests
import time
#
# def getTime(n):
#     return 2*n
def fayat(userid, n,text):
    k = requests.get(
        ('https://sayat.me/' + userid))

    cf = ''
    php = ''
    csam = ''
    guid = ''

    last_a = ''

    for x in k.cookies:
        # print x.name, x.value
        if x.name == '__cfduid':
            cf = x.value
        elif x.name == 'PHPSESSID':
            php = x.value
        elif x.name == 'csam':
            csam = x.value
        elif x.name == 'guid':
            guid = x.value
        elif x.name == 'last_activity':
            last_a = x.value
        else:
            pass
    for loop in range(0, n):
        # print cf, php, csam, guid, last_a
        headers = {
            'origin': 'https://sayat.me',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8,la;q=0.6,hi;q=0.4',
            'cookie': '__cfduid=' + str(
                cf) + '; PHPSESSID=' + php + '; language=en; guid=' + guid + '; csam=' + csam + '; last_activity=' + last_a + '',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cache-control': 'max-age=0',
            'authority': 'sayat.me',
            'referer': str('https://sayat.me/' + userid),
            'dnt': '1',
        }

        data = [
            ('write', str(text)),
            ('more_feedback_input', ''),
            ('foo', 'C8MQzISSm05kdk8'),
            ('bar', 'aCtQJTkSITs7BVhdAwwDUA=='),
            ('full_name', ''),
            ('password', ''),
            ('password_confirm', ''),
            ('url', ''),
            ('birth_Day', ''),
            ('birth_Month', ''),
            ('birth_Year', ''),
            ('csam', str(csam)),
        ]

        r = requests.post(('https://sayat.me/' + userid), headers=headers, data=data)
        print r
        time.sleep(0.4)



# fayat(userid="tanseersaji", n=5,text="hey man!")
