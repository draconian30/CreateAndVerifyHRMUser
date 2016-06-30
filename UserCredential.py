class UserCredential:
    
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password
        
    def getUserName(self):
        return self.userName
    def getPassword(self):
        return self.password;
    def setUserName(self,userName):
        self.userName = userName
    def setPassword(self,password):
        self.password = password