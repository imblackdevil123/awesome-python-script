#!/usr/bin/env python
#gatherinf file ,subdomain,directories of website
#this program is subdomain or domain tester
import requests
url="eferfwec.google.com"#go to exception for bad subdomain
try:
    get_response=requests.get(url)#get request
    print(get_response)
except requests.exceptions.ConnectionError:
    pass
