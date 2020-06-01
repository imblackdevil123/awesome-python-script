#!/usr/bin/env python
#program to get all the links of website
import requests,urlparse
import re
 
target_url="http://udemy.com/"
target_links=[]
def extract_links_from(url):
    response=requests.get(url)   
    # print(response.content)#previously displayed binery content of file downloaded and in here will display html content
    #response.content gives html content and from that we can use re to get a tag links
    return re.findall('(?:href=")(.*?)"',response.content)#?:for not inccluding(different group) and? for not greedy as to find first " not last"

def crawl(url):
    href_links=extract_links_from(url)
    # print(href_links)#same method can be used to extract any part of page eg img etc.[it prints list of that webpage list]
    for link in href_links:#during recursion,from this will be stored in stack for later execution
        link=urlparse.urljoin(url,link)#it has knowledge not to modify for full url
        if "#" in link:#here some link has # in it indicate more content of same page(url) rather than different url
            link=link.split("#")[0]
        if target_url in link and link not in target_links:#only provide link of that website not of others like fb.com
            target_links.append(link)
            print(link)#some url are not proper full url(relative url ) so  need to fix so use library urlparse
            crawl(link)
crawl(target_url) 
