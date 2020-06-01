#!/usr/bin/env python
#python code to communicate with ip field 
#can be used to submit forms automatically
# can do dictionary attack using list of password as well as  username and get user info
import requests
target_url="http://10.0.2.20/dvwa/login.php"#use fb url to automate login
data_dict={"username":"admin","password":"password","login":"submit"}
response=requests.post(target_url,data=data_dict)
print(response.content) 