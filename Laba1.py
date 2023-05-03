import socket
import uuid
#Program is asking for your name
print ("What's your name?")
#Input of your name
name = input ()
#Printing of your name
print ("Hello, " +name)
#Search of name of PC
hostname = socket.gethostname()
#Printing the name of PC
print (hostname)
#Search of IP of PC
IPaddress = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IPaddress.connect(('77.88.8.8', 80))
#Printing of IP of PC
print ("IP addres of your pc: " +IPaddress.getsockname()[0])
#Search and print of MAC of PC
print ("MAC address of your pc: ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
