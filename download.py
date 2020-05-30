#!/usr/bin/env python
import requests
def download(url):
    get_response=requests.get(url)
    print(get_response.content)#displays all the jebbrish binary we use to see in raw header. now write this content to a file so it is downloaded
    file_name=url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)
download("https://www.dsds.com/dcdcs/dcdc/dipen.jpeg")    