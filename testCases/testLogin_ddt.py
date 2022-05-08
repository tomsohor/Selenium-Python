from time import sleep
from pageObjects.loginPage import Login
from utils.readProperties import readConfig
from utils.customLogger import logGen
from utils import XLUtils

class Test_002_DDT_login:
    adminURL = readConfig.getAppAdminUrl()
    path = './/testData/loginData.xlsx'
    userId = readConfig.getAdminUserId()
    pwd = readConfig.getAdminPwd()
    loggedUserIdPath = "Admin__Landing__LoggedInUserId_txtcnt"

    logger = logGen.loggen() #store log
    
    
    def test_login_ddt(self,setUp):
        self.logger.info('***********login_test_ddt***********')
        self.logger.info('***********login_ddt_test***********')

        
        self.driver = setUp
        self.driver.get(self.adminURL)
        sleep(7)

        self.logPage = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of row i a Excel:', self.rows)

        for r in range(2,self.rows+1):
            self.userId = XLUtils.readData(self.path,'Sheet1', r,1)
            self.pwd = XLUtils.readData(self.path,'Sheet1', r,2)
            self.logPage.setUserId(self.userId)
            self.logPage.setPwd(self.pwd)
            self.logPage.clickLogin()
            logged_user = "User : " + self.userId
            sleep(5)

            userLanded = self.driver.find_element_by_id(self.loggedUserIdPath).text
            print(userLanded)
            
            if userLanded == logged_user:
                self.logger.info('***********login_test: Passed***********')
                self.logPage.burgurIcon()
                self.logPage.signOut()
                sleep(1)
                # self.driver.close()
               
                assert True
            else:
                self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
                # self.driver.close()
                self.logger.error('***********login_test: Failed***********')
                assert False
            
        


