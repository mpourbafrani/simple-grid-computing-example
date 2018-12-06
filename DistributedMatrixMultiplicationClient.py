import socket
import sys
import numpy as np
import time
from time import sleep
#server get data port number
ServerPort=10000
#server send data port number
ServerSPort=20000
sleepTime=2
#server ip Address
ServerAddress="127.0.0.1"
try:
    #get data while server has data for calculate
    while True:
        #Try to connect to server and get calculation values
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('try to get data')
        sock.connect ((ServerAddress, ServerPort))
        inf=sock.recv(1024).decode("utf-8")
        item=inf.split('-')
        M1=np.matrix(item[1])
        M2=np.ndarray.transpose( np.matrix(item[2]))
        #print(M1)
        #print(M2)
        #multiply values
        X= np.matmul(M1,M2)
        sock.close()
        #try to sleep for undrestanding distributed computing
        time.sleep(sleepTime)
        #send resault to 20000 port 
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print('starting up on {} port {}'.format(*ServerAddress))
        sock2.connect ((ServerAddress, ServerSPort))
        sock2.sendall((item[0]+"_"+str(X[0,0])).encode('utf-8'))
        sock2.close()
except:
    print("Finished")