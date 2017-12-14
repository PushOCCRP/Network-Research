from scapy.all import * 
from pprint import pprint

ethernet = Ether()
network = IP(dst = ['rejahrehim.com']) 
transport = TCP(dport=[(80)], flags = 'S') 
packet = ethernet/network/transport  
for pkt in packet: 
          pkt.show() 