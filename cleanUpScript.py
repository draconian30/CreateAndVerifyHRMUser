import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


print 'Cleanup script started'
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://127.0.0.1/orangehrm-3.0.1/symfony/web/index.php/auth/')
print 'User cleanup started'
search_userid=driver.find_element_by_id("txtUsername")
search_userid.clear()
search_userid.send_keys('adminoh')
search_password=driver.find_element_by_id("txtPassword")
search_password.clear()
search_password.send_keys('adminoh')
btnLogin=driver.find_element_by_id("btnLogin")
btnLogin.click()
time.sleep(2)



for i in range(10):
    try:
        chkSelectAll=driver.find_element_by_xpath('//*[@id="ohrmList_chkSelectAll"]').click()
        break
    except NoSuchElementException as e:
        print('retry in 1s.')
        time.sleep(1)
else:
    raise e
print 'All user has been selected'


    
btnDelete=driver.find_element_by_id('btnDelete').click()
    

dialogDeleteBtn=driver.find_element_by_id('dialogDeleteBtn').click()

print 'All User deleted'

welcome = driver.find_element_by_id('welcome')
welcome.click()

logoutt = driver.find_element_by_xpath(".//*[@id='welcome-menu']/ul/li[2]/a")
logoutt.click()
print 'User cleanup is done'
driver.quit()
print'browser exit'




