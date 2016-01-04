# ch15_01.py
# hello socket

import socket


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print('hostname:', hostname)
print('ip address:', ip)

