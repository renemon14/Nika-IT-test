from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import logging, os
from functions.GeneralFunctions import General_Functions

### HOOKS ###

### Before Tests ###

def before_feature(self, feature):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                   chrome_options=chrome_options)
    General_Functions.driver = self.driver


### After Tests ###

def after_feature(self, feature):
    self.driver.quit()
