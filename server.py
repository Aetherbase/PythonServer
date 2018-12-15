
# first of all import the socket library 
import socket
import cv2
import serial

serialw = serial.Serial('COM3')
               
  
# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port =  1755

#get IP ADRESS
hostname = socket.getfqdn()    
IPAddr = socket.getaddrinfo(hostname,port)               
print("IP ADDRESS: ",IPAddr[-1][-1][0])
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening" )           
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   #print ('Got connection from', addr )
   data = str(c.recv(1024))
   index = data.find(',')
   data=data[index-1:-1]
   if(data==0): continue
   print(data)
   serialw.write(data.encode())
   
   
   

   
   
   
