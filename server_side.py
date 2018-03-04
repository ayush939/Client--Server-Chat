# __author__= 'Ayush Mittal'


# you only need one library for this. Thanks to Python :p
import socket

#define port for the socket
#host ip is left blank to allow all IP to get connected
host=''
port=1238


#define a function to setup the server
def setupServer():
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    print "Server setup complete"
    return s

# define a function to start your server so you can listen to the clients
def startServer(s):
    try:
        s.listen(1)
        print "Server Initialised"
        print "waiting for client..."
        conn, add= s.accept()
    except:
        s.close()
        print "Restart the program with different port"
    print "Connected to a Socket:"
    print add
    #print "\nDont worry about the above stuff and start chatting!"
    print "\nWaiting for client to initiate the chat"
    return conn

#function to send the message to the client
def sendMessage(conn):
    data= raw_input("YOU: ")
    conn.send(data)
    return data

#function to recieve the message from the client
def recvMessage(conn):
    data= conn.recv(1024)
    print "STRANGER: " +data
    return data


s=setupServer()
conn=startServer(s)

#the main code 
try:
 while True:
      r=recvMessage(conn)
      sen=sendMessage(conn)
      
      #both of them have to write "Exit" to exit the chat
      if r== 'Exit':
         if sen=='Exit':
             print "disconnecting..."
             s.close()
             conn.close()
             break
         else:
             continue
      elif sen=='Exit':
          r=recvMessage(conn)
          if r=='Exit':
              
             print "disconnecting..."
             s.close()
             conn.close()
             break
          else:
              continue
      else:
          print "waiting for reply from the other side...."


#if anything goes wrong          
except:
    s.close()
    conn.close()
    
print "Disconnected"
