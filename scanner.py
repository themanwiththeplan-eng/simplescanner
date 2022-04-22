#!/bin/python3

import sys 
import socket as sck
from datetime import datetime as dt

#Define our target
if len(sys.argv) == 2:
        target = sck.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
        print("Invalid amount of arguments")
        print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(dt.now()))

try: 
        for port in range(1,65535):
                s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
                sck.setdefaulttimeout(1)
                result = s.connect_ex((target, port)) #returns an error indicator 
                if result == 0:
                        print("Port {} is open".format(port))
                s.close()
except KeyboardInterrupt:
        print("\n Exiting program.")
        sys.exit()
except sck.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
except sck.error:
        print("Couldn't connect to server.")
        sys.exit()

