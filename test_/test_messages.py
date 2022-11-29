import datetime
import time

from library.config import Config
from library import Reading_objects
from POM.Chats import Messenger

class TestChats:
    def test_send_msg(self,init_driver):
        # try:

        msg1=Messenger(init_driver)
        msg1.enter_email("kousalyakodati1357@gmail.com")
        msg1.enter_pwd("Facebook@kous28")
        msg1.click_login()
        time.sleep(3)
        msg1.select_friend()
        msg1.enter_msg("HELLO")
        msg1.profile_logout()
        # except AssertionError as msg:
        #    td = datetime.datetime.now()
        # raise msg
class TestChats2:
    def test_send_like(self,init_driver):

            msg1=Messenger(init_driver)
            msg1.enter_email("kousalyakodati1357@gmail.com")
            msg1.enter_pwd("Facebook@kous28")
            msg1.click_login()
            msg1.select_friend()
            msg1.enter_msg("123!@#$")
            msg1.profile_logout()
#
class TestChats3:
    def test_send_emoji(self,init_driver):

            msg1=Messenger(init_driver)
            msg1.enter_email("kousalyakodati1357@gmail.com")
            msg1.enter_pwd("Facebook@kous28")
            msg1.click_login()
            msg1.select_friend()
            msg1.send_emoji()
            msg1.profile_logout()
class TestChats4:
    def test_send_sticker(self,init_driver):

            msg1=Messenger(init_driver)
            msg1.enter_email("kousalyakodati1357@gmail.com")
            msg1.enter_pwd("Facebook@kous28")
            msg1.click_login()
            msg1.select_friend()
            msg1.send_sticker()
            msg1.profile_logout()
class TestChats5:
    def test_chats(self,init_driver):
        msg1 = Messenger(init_driver)
        msg1.enter_email("prathyusha@gmail.com")
        msg1.enter_pwd("Facebook@28")
        msg1.click_login()
        time.sleep(2)
        path=r"C:\Users\KOUSALYA\facebook_msg\Screenshots\\"
        init_driver.save_screenshot(path+"screenshot.png")
        msg1.select_friend()
        msg1.enter_msg(" ")
        msg1.select_friend()
        msg1.profile_logout()




