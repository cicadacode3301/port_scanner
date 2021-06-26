#!/bin/python3
import socket
import sys
from datetime import datetime

# Define target

if len(sys.argv) == 2 :
	try:
		target = socket.gethostbyname(sys.argv[1])
	except socket.gaierror:
		print('Hostname unable to resolve')
		sys.exit()
	
else :
	print('Please provide input in format 1.1.1.1')
	sys.exit()

#Adding banner

print('#' * 50)
print('Scanning target {}'.format(target))
print(datetime.now())

#Scanning the target

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)	# to set the default timeout to connet to port as 1 sec
		c = s.connect_ex((target,port)) # to store the error indicator as 0 or 1, if error indicatior is 0 it was able to connect and its 1 then it was unable to connect
		if c == 0:
			print('Port {} is open'.format(port))
		s.close

except KeyboardInterrupt:
	print('\n Exiting program')
	sys.exit()

except socket.gaierror:
	print('Hostname unable to resolve')
	sys.exit()

except socket.timeout:
	print('Couldn\'t connect to target')
	sys.exit()
print(datetime.now())
