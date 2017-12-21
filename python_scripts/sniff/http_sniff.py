from scapy.all import *

'''
Capture print details of packet on:
	- port 80
	- interface wlp3s0
Sniff() - collects packet and dumps them to callback function
	- store=0 - dont store packets in memory from capture
	- prn=callback - sniff will place the packets it captures into the callback function
'''
def allpacket(pkt):
	if pkt.haslayer(TCP):
		print pkt.summary()
		print pkt.show()
		print pkt[TCP]
sniff(filter="port 80", prn=allpacket, store=0, iface='wlp3s0')
