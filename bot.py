from selenium import webdriver 
import os
import time

class InstagramBot: 
    
    # Constructor
    def __init__(self, unsername, password): 
        """
        Initilizes an instance of the InstagramBot class.
        Calls the login method.

        Args: 
            username: str: 
            password: str: 

        Attributes:
            driver: Selenium.webdriver.Chrome

        """
        

        self.unsername = unsername
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver')
        self.login()

    def login(self):
        # navigating to insta login
        self.driver.get('https://www.instagram.com/accounts/login')
        self.driver.find_element_by_name('username').send_keys(self.unsername)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()

    
# kinda like main function
if __name__ == '__main__': 
    ig_bot = InstagramBot('temp_username', 'temp_password')

    
