import socket
import sys
import numpy as np
import threading
MatrixSize=3
#initialize 2 matrixs
M1=np.random.randint(10, size=(MatrixSize,MatrixSize))
M2=np.random.randint(10, size=(MatrixSize,MatrixSize))
#initialize Resault Matrix as zero Value
M=np.zeros((MatrixSize,MatrixSize),dtype=np.int)
#Send Data--> the function that send row and column to Clients for calculation
def SendData():
    #Bind socket on server with port number 10000 for sending data
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (socket.gethostname(), 10000)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(1)
    for i in range(0,np.size(M1,0)):
        for j in range(np.size(M2,1)):
            #wait for recieve request from client to get value to calculation
            connection, client_address = sock.accept()
            #generate Data
            #Send Row and column number of resault Matrix in row_col format
            data=str(i)+'_'+str(j)+"-"
            #add all rows from Matrix1 to data
            for item in np.nditer(M1[i]):
                data=data+str(item)+" "
            #set "-" spliter between rows and columns
            data=data+"-"
            #add all columns from Matrix2 to data
            for item in np.nditer(M2[:,j]):
                data=data+str(item)+" "
            print(data)
            #send all generated Data to client
            connection.sendall(data.encode())

#Run sender function on a thread in parallel of recieving calculations
THSendInf=threading.Thread(target=SendData,args=())
THSendInf.start()
#Count number of resault should recieve
CountItem=MatrixSize*MatrixSize
#Initialize Socket for Recieve Data
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address2 = (socket.gethostname(), 20000)
sock1.bind(server_address2)
sock1.listen(1)
while(CountItem>0):
    print(CountItem)
    connection, client_address = sock1.accept()
    #recieve data from Client and set on specific position of destination matrix
    x=connection.recv(1024).decode()
    print(x)
    inf=x.split('_')
    M[int(inf[0]),int(inf[1])]=int(inf[2])
    CountItem=CountItem-1
print("\n\n\n\nAnswer is:")
print(M)