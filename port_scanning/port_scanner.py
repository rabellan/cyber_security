import socket
 
s = socket.socket()
 
# OUR_URL_HERE ex. https://www.myurl.com
result = s.connect_ex((YOUR_URL_HERE, 8090))
 
if(result == 0):
  print('Port is open')
else:
  print('Port is closed')