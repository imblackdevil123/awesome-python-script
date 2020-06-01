#!/usr/bin/env python
#this program is subdomain.
#program to get all subdomain of certain domain use wordlist
import requests
target_url="google.com"
def request(url):
    try:
        return requests.get("http://"+ url)#get request
    except requests.exceptions.ConnectionError:
        pass
with open("subdomains_wodlist.txt","r") as wordlist_file:
    for line in wordlist_file:#how to read a file one line at a time
        # print(list)   
        word=line.strip()
        test_url = word + "." + target_url
        response = requests(test_url)
        if response:#return null if there is no such domain as it go through exception
            print("[+] discovered subdomain------>"+test_url)
