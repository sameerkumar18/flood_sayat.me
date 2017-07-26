# -*- coding: utf-8 -*-

import requests
def checkID(uid):
    base = "https://sayat.me/"
    url = base + str(uid)

    r = requests.get(url,timeout=15)
    print r
    if "200" in str(r):
        return True
    else:
        return False

def checkText(text):
    if len(str(text)) <= 200 :
        return True

    else:
        return False

def check_n(n):
    if n < 200 and n>0:
        return True
    else:
        return False

def checkAll(uid,n,text):
    if check_n(n) and checkID(uid) and checkText(text):
        return True
    else:
        return False
#
# if checkAll(uid="tansersaji",n=5,text="Shimla features a subtropical highland climate town received 63.6 centimetres (25.0 in) of snow.[27]"):
#     print "OK"
# else:
#     print "err?"

# checkText('''Shimla features a subtropical highland climate town received 63.6 centimetres (25.0 in) of snow.[27]''')
# if checkID("tanseersaji"):
#     print "hey"
# else:print "err"