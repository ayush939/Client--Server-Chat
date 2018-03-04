#__author__='Ayush Mittal'


import socket

#get the server IP as input 
temp=raw_input("Type the IP of server: ")
server_ip= "'" + temp + "'"


#the port number should be same in both the programmes
port=1238

#function to connnect the server with the defined socket 
def connect2Server():
    
    s=socket.socket()
    s.connect((server_ip,port))
    print "Connected to IP:" + server_ip
    print "Start chatting!"
    return s
    
#function to send a message to server
def sendMessage(s):
    data=raw_input("YOU: ")
    s.send(data)
    return data

#function to recieve a message from the server
def recvMessage(s):
    reply= s.recv(1024)
    print "STRANGER: " + reply
    return reply

#initialize the process
s=connect2Server()
print "Initiate the chat"

#main fucntion
while True:
    sen= sendMessage(s)
    print "waiting for reply from the other side...."
    r=recvMessage(s)

    #the next few lines are responsible for exiting the chat when both
    #(server and client) type 'Exit'
    if sen=='Exit' and r=='Exit':
        print "disconnecting..."
        s.close()
        break
    elif r=='Exit':
         sen1=sendMessage(s)
         if sen1=='Exit':
             print "disconnecting..."
             s.close()
             break
         else:
             continue
            
print "Disconnected"            
