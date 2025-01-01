#!/usr/bin/env python3

import socket
import sys

try:
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
	print("Error occured while creating socket. Error code: " + str(e[0]) + ':' + e[1])

print('Success!')
print(tcp_socket)
sys.exit();
