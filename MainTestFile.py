import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from FileProcesses import FileProcesses
from UserOperations import UserOperations


adminFile = 'adminLoginDetails.csv'
userBasicDetailsFile = 'userBasicDetailsFile.csv'
userCredentialFile = 'userCredentialFile.csv'

print 'Automation Test  Started'
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://127.0.0.1/orangehrm-3.0.1/symfony/web/index.php/auth/')

userOperations = UserOperations(driver, Select,time)

fileProcesses = FileProcesses(userOperations)

adminCredential = fileProcesses.readFile(adminFile)[0]

userOperations.login(adminCredential[0], adminCredential[1])
print 'Admin login'

userBasicData = fileProcesses.readFile(userBasicDetailsFile)[0]

userCredentialData = fileProcesses.readFile(userCredentialFile)[0]

userOperations.create(userBasicData[0], userBasicData[1])
print 'User created.'

userOperations.createLoginCredentials(userCredentialData[0], userCredentialData[1])
print 'User login credentials generated.'

userOperations.logout()
print 'Admin logout.'
 
isLogined = userOperations.login(userCredentialData[0], userCredentialData[1])
print 'User logged in '

userOperations.login(adminCredential[0], adminCredential[1])
print 'Admin login'

userOperations.enable(userCredentialData[0])
print 'User set to enable'

time.sleep(2)

userOperations.logout()
 
print "User again login",userCredentialData
isLogined = userOperations.login(userCredentialData[0], userCredentialData[1])

time.sleep(5)
 
userOperations.logout()
print 'user logout'

driver.quit()
print 'Browser logout'
