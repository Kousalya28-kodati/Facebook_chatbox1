from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from library.config import Config
from library.Reading_objects import Reading_Excel
msg_objects=Reading_Excel.read_locators(Config.DATA_PATH_TITLE)


class Messenger:
    def __init__(self,driver):
        self.driver=driver
    def enter_email(self,email):
        self.driver.find_element(*msg_objects['text_mail']).send_keys(email)
    def enter_pwd(self,pwd):
        self.driver.find_element(*msg_objects['text_pwd']).send_keys(pwd)
    def click_login(self):
        self.driver.find_element(*msg_objects['text_login']).click()
    def select_friend(self):
        self.driver.find_element(*msg_objects["text_friend"]).click()
    def enter_msg(self,msg_):
        self.driver.find_element(*msg_objects['enter_msg']).send_keys(msg_)
        self.driver.find_element(*msg_objects['text_send_msg']).click()
    def send_like(self):
        self.driver.find_element(*msg_objects["text_send_like"]).click()
    def send_sticker(self):
        self.driver.find_element(*msg_objects["text_choose_sticker"]).click()
        self.driver.find_element(*msg_objects["text_select_sticker"]).click()
        self.driver.find_element(*msg_objects["text_send_sticker"]).click()

    def send_emoji(self):
        self.driver.find_element(*msg_objects["text_emoji"]).click()
        self.driver.find_element(*msg_objects["text_select_emoji"]).click()
        self.driver.find_element(*msg_objects["text_send_emoji"]).click()
    def profile_logout(self):
        self.driver.find_element(*msg_objects["text_closechat"]).click()
        self.driver.find_element(*msg_objects["text_profile"]).click()
        self.driver.find_element(*msg_objects["text_logout"]).click()







# msg1=Messenger(driver)
# msg1.enter_email()
# msg1.enter_pwd()
# msg1.click_login()
# msg1.select_friend()
# msg1.enter_msg()
# msg1.send_like()
# msg1.send_sticker()
# msg1.send_emoji()
# msg1.join_room()






