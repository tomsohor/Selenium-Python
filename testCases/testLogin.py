from time import sleep
from pageObjects.loginPage import Login
from utils.readProperties import readConfig
from utils.customLogger import logGen

class Test_001_login:
    adminURL = readConfig.getAppAdminUrl()
    userId = readConfig.getAdminUserId()
    pwd = readConfig.getAdminPwd()
    loggedUserIdPath = "Admin__Landing__LoggedInUserId_txtcnt"

    logger = logGen.loggen() #store log
    
    
    def test_login(self,setUp):

        self.logger.info('***********login_test***********')

        logged_user = "User : " + self.userId
        self.driver = setUp
        self.driver.get(self.adminURL)
        sleep(4)

        self.logPage = Login(self.driver)
        self.logPage.setUserId(self.userId)
        self.logPage.setPwd(self.pwd)
        self.logPage.clickLogin()
        sleep(3)

        userLanded = self.driver.find_element_by_id(self.loggedUserIdPath).text
        print(userLanded)
        
        if userLanded == logged_user:
            assert True
            self.driver.close()
            self.logger.info('***********login_test: Passed***********')
            
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error('***********login_test: Failed***********')
            assert False


