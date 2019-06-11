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
        self.base_url = 'https://www.instagram.com'

        self.driver = webdriver.Chrome('./chromedriver')
        # self.login()

    # navigating to insta login
    def login(self):
        self.driver.get('{}/accounts/login'.format(self.base_url))
        self.driver.find_element_by_name('username').send_keys(self.unsername)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()

    # navigates to an IG user
    def nav_user(self, user): 
        self.driver.get('{}/{}/'.format(self.base_url, user))
        self.driver.find_element_by_name('username').send_keys(self.unsername)

# kinda like main function
if __name__ == '__main__': 
    ig_bot = InstagramBot('temp_username', 'temp_password')

    ig_bot.nav_user('garyvee')
    
