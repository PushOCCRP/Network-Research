from scapy.all import *

def callback(pkt):
    if pkt.haslayer(DNS):
        pkt[UDP].dport = 10000
        send(pkt)
sniff(filter="host 192.168.0.105", prn=callback, store=0, iface="wlp3s0")
