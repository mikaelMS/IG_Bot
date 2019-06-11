from selenium import webdriver 
import os
import time

class InstagramBot: 
    
    # Constructor
    def __init__(self, unsername, password): 
        self.unsername = unsername
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.instagram.com')

    


# kinda like main function
if __name__ == '__main__': 
    ig_bot = InstagramBot('temp_username', 'temp_password')

    print(ig_bot.unsername)