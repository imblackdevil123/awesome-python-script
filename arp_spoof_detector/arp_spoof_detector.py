#!/usr/bin/env python
# to run arp_spoof in window require py interpret and scapy
# python -m pip install scapy then run that script
import scapy.all as scapy
#code copied from packet sniffer and converted that
def get_mac(ip):#copied fron network1_scanner.py
    arp_request=scapy.ARP(pdst=ip) 
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast=broadcast/arp_request 
    answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0] 
    return answered_list[0][1].hwsrc#being there is only one ip so 0 index

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet )
     
def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op==2:#check packet is response packet and it is ARP
        # print(packet.show())#it will display content if someone spoof to become mimf making us target
        try:
            real_mac=get_mac(packet[scapy.ARP].psrc)#using get_mac function to get actual mac of router
            response_mac=packet[scapy.ARP].hwsrc#mac corresponding to psrc(ip) as response
            if real_mac!=response_mac:                                                              ##########################
                print("[+] You are in trouble bro " + str(response_mac) + " Trying to spoof on ")#srt part added may cause error
        except IndexError:
            pass        
    
sniff("eth0")    
 