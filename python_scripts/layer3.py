from scapy.all import *
from pprint import pprint

# send() function to send packets at layers 3, scapy will handle the routing and layer 2 within it.
network = IP(dst = '192.168.1.1')
transport = ICMP()
packet = network/transport
send(IP(packet))

# This will send an ICMP packet