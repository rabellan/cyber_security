import binascii

#this is for training purposes only!
 
f = open('exploit.bin','wb')
 
f.write(b'\x0a\x0b\x0c' * 10)
 
f.close
 
f = open('exploit.bin','rb')
 
bytes = f.read()
 
print(binascii.b2a_uu(bytes))