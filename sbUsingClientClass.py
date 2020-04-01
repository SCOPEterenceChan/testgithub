import sys
from Client import Client
         
fileIn = open('datafile1.dat', 'r')

clientDT=['Name','Address','Balance']
clientDL=[]

line = fileIn.readline()

while line != '':
    clientRec=line.split('_')

    if Client.numClient == 0:
        if clientRec[2] == 'D':
            clientDL.append(Client(clientRec[0],
                                   clientRec[1],
                                   float(clientRec[3])))
        else:
            clientDL.append(Client(clientRec[0],
                                   clientRec[1],
                                   -float(clientRec[3])))           
    else: 
        i = 0
        while i < Client.numClient and clientDL[i].name != clientRec[0]:
            i += 1
    
        if i == Client.numClient:
            if clientRec[2] == 'D':   
                clientDL.append(Client(clientRec[0],
                                   clientRec[1],
                                   float(clientRec[3])))
            else:
                clientDL.append(Client(clientRec[0],
                                   clientRec[1],
                                   -float(clientRec[3])))                
        else:
            if clientRec[2] == 'D':
                clientDL[i].debit(float(clientRec[3]))
            else: clientDL[i].credit(float(clientRec[3])) 
        
    line = fileIn.readline()
        
if Client.numClient == 0:
    sys.stderr.write('empty or invalid data only : '+line+'\n')
else:                
    print('%-20s%-30s%10s'%(clientDT[0],clientDT[1],clientDT[2]))
    print('='*60)    
    for e in sorted(clientDL, key = lambda c: c.name):
        if e.getBalance() != 0:
            print(e) 
          
fileIn.close()
