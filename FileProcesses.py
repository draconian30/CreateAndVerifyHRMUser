import csv
class FileProcesses:

    def __init__(self,userOperations):
        self.userOperations =userOperations
    def loginThroughFile(self,file):
        with open(file) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(512))
            csvfile.seek(0)
            userCredentials=csv.reader(csvfile,dialect)
            for userCredential in userCredentials:
                self.userOperations.login(userCredential[0], userCredential[1])
    
    def readFile(self,file):
        with open(file) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(512))
            csvfile.seek(0)
            fileData=list(csv.reader(csvfile,dialect))
            return fileData