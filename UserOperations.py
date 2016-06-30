from selenium.common.exceptions import NoSuchElementException  
class UserOperations:
    
        driver = none
        select = none
        time =none
    
    def login(self,userName,userPass):
        search_userid=self.driver.find_element_by_id("txtUsername")
        search_userid.clear()
        search_userid.send_keys(userName)
        search_password=self.driver.find_element_by_id("txtPassword")
        search_password.clear()
        search_password.send_keys(userPass)
        btnLogin=self.driver.find_element_by_id("btnLogin")
        btnLogin.click()
        try:
            spanMessage = self.driver.find_element_by_xpath('//*[@id="spanMessage"]')
            message = spanMessage.text      
            return message != 'Account disabled'
        except NoSuchElementException:
            return True;
        print 'login method has been executed'
        
    def logout(self):
        welcome = self.driver.find_element_by_id('welcome')
        welcome.click()
        logoutt = self.driver.find_element_by_xpath(".//*[@id='welcome-menu']/ul/li[2]/a")
        logoutt.click()
        print 'Logout method has been executed'
        
    def create(self,firstUName,lastUName):
        btnAdd=self.driver.find_element_by_id("btnAdd")
        btnAdd.click()
        firstName=self.driver.find_element_by_id("firstName")
        firstName.clear()
        firstName.send_keys(firstUName)
        lastName = self.driver.find_element_by_id("lastName")
        lastName.clear()
        lastName.send_keys(lastUName)
        print 'User has been created'
        
    def createLoginCredentials(self,userName,userPassword,):
        chkLogin=self.driver.find_element_by_id("chkLogin")
        chkLogin.click()
        user_name=self.driver.find_element_by_id("user_name")
        user_name.clear()
        user_name.send_keys(userName)
        user_password=self.driver.find_element_by_id("user_password")
        user_password.clear()
        user_password.send_keys(userPassword)
        re_password=self.driver.find_element_by_id("re_password")
        re_password.clear()
        re_password.send_keys(userPassword)                        
        status = self.select(self.driver.find_element_by_id('status'))
        status.select_by_value('Disabled')
        btnSave=self.driver.find_element_by_id("btnSave")
        btnSave.click();
        print' User credentials created.'
        
    def enable(self,userId):
        print userId
        adminTab = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]') 
        adminTab.click()
        userManagementTab = self.driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]') 
        userManagementTab.click()
        usersTab = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
        usersTab.click()
        searchUserId = self.driver.find_element_by_id("searchSystemUser_userName")
        searchUserId.clear()
        searchUserId.send_keys(userId)
        searchBtn = self.driver.find_element_by_id("searchBtn")
        searchBtn.click()
        userLink = self.driver.find_element_by_xpath(".//a[contains(text(), '"+userId+"')]")
        userLink.click()
        btnSave = self.driver.find_element_by_id("btnSave")
        btnSave.click()
        status = self.select(self.driver.find_element_by_id('systemUser_status'))
        status.select_by_value('1')
        btnSave.click()
        print 'User has been enabeled.'
    
         
