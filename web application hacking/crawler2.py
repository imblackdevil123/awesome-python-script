#!/usr/bin/env python
#this program is subdomain.
#program to get all subdomain of certain domain use wordlist
#get files and dirs of domain/subdomain
import requests
target_url="10.0.2.16/mutillidae"#website of metaspoitable
def request(url):
    try:
        return requests.get("http://" + url)#get request
    except requests.exceptions.ConnectionError:
        pass
with open("files_dirs_wordlist.txt","r") as wordlist_file:
    for line in wordlist_file:#how to read a file one line at a time
        # print(list)   
        word=line.strip()
        test_url = target_url + "/" + word
        response = requests(test_url)
        if response:#return null if there is no such domain as it go through exception
            print("[+] discovered URL------>"+test_url)
