from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from utils.readProperties import readConfig
import pytest

@pytest.fixture
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('--------------- lauching chrome -------------------')
    elif browser == 'firefox':
        options = Options()
        options.binary_location = readConfig.getFirefox()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) 
        print('--------------- lauching firefox -------------------')
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser): #get value from CLI/hook
    parser.addoption('--browser')

@pytest.fixture
def browser(request): #will parse value to setup method
    return request.config.getoption('--browser')


############ Pytest html report ################
# it is hook for adding environment info to html report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Test Automation'
#     config._metadata['Module Name'] = 'Exploration'
#     config._metadata['Tester'] = 'Kanya'

# # it is hook for delete/modify environment info to Html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME', None)
#     metadata.pop('Plugins', None)

# ### add --html=reports\report.html into running code
