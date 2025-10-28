#!/usr/bin/env python3
from scapy.all import *

pcapfile=filename

# load in packets from pcap file
packets = rdpcap(pcapfile)
for packet in packets:
	print(packet.summary())
	
	if TCP in packet:
		print(packet[TCP].payload)
		print(bytes_hex(packet[TCP].payload))
		#print(p)
	#print(packet.src)
	#print(packet.show())
