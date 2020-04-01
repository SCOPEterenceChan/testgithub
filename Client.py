class Client(object):
    '''
    Client class to represent each customer object
    '''
    numClient = 0 # class variable to record number of client
    
    def __init__(self,name,address,balance ):
        '''
        constructor method
        
        Parameters:

        - name: name of customer
        - address: name of customer
        - balance: balance of customer
        '''
        Client.numClient += 1
        
        self.name = name
        self.address = address
        self.__balance = balance
    
    def debit(self,amount):
        '''
        debit method to increase balance of liability account
        
        Parameters:

        - amount: amount to bebit     
        '''
        self.__balance += amount
        
    def credit(self,amount):
        '''
        credit method to increase balance of liability account
        
        Parameters:

        - amount: amount to credit     
        '''
        self.__balance -= amount
        
    def getBalance(self):
        '''
        accessor method to get balance
        '''
        return self.__balance
        
    def __str__(self):
        '''
        String representation of client object
        '''
        return '%-20s%-30s%10.2f'%\
            (self.name,self.address,self.__balance)
