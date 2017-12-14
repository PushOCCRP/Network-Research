from scapy.all import *
from pprint import pprint

# To send a packet with custom layer 2, we have to use sendp() method.  Here we have to pass the interface to be used for sending the packet.  #  e can provide it with the iface parameter.  If this is not provided, it will used the default value from the conf,iface
ethernet = Ether()
network = IP(src='1.1.1.1.', dst = '192.168.1.1')
transport = ICMP()
packet = ethernet/network/transport
sendp(packet, iface="wlp3s0")