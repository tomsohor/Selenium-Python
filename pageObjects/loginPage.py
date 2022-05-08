class Login:
    textbox_userid="Admin__Login__userId"
    textbox_pwdid="Admin__Login__pswd"
    btn_login_xpath='//*[@id="Admin__Login__element_button_1"]' 
    btn_burgur_icon = "btn_icon_icon-burger-sv"
    link_signout="Admin__Landing__signOutLink"


    def __init__(self,driver):
       self.driver = driver
       
    def setUserId(self,userid):
        self.driver.find_element_by_id(self.textbox_userid).clear()
        self.driver.find_element_by_id(self.textbox_userid).send_keys(userid)

    def setPwd(self,pwd):
        self.driver.find_element_by_id(self.textbox_pwdid).clear()
        self.driver.find_element_by_id(self.textbox_pwdid).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()
    
    def burgurIcon(self):
        self.driver.find_element_by_id(self.btn_burgur_icon).click()

    def signOut(self):
        self.driver.find_element_by_id(self.link_signout).click()