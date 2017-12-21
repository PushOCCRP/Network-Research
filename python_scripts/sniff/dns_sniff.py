from scapy.all import *

def dnssniff(pkt):
    if pkt.haslayer(DNS):
        pkt.show()
        #pkt[UDP].dport = 10000
        #send(pkt)
sniff(filter="host 192.168.0.105", prn=dnssniff, store=0, iface="wlp3s0")
