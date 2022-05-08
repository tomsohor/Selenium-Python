import configparser
from os import stat

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class readConfig:
    @staticmethod
    def getAppAdminUrl():
        url = config.get("common info","adminURL")
        return url

    @staticmethod
    def getAdminUserId():
        userid = config.get("common info","userId")
        return userid

    @staticmethod
    def getAdminPwd():
        pwd = config.get("common info","pwd")
        return pwd

    @staticmethod
    def getFirefox():
        firefox = config.get('firefox location','firefox')
        return firefox


