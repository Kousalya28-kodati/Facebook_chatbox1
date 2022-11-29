from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--disable-notification")

chrome_option.add_argument("--disable-infobars")

chrome_option.add_argument("start-maximized")

chrome_option.add_argument("--disable-extensions")

chrome_option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})

chrome_option.add_argument("use-fake-ui-for-media-stream")

path = r'C:\Users\KOUSALYA\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path,options=chrome_option)
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#To enter the email to login
driver.find_element_by_name("email").send_keys("kousalyakodati1357@gmail.com")
#To enter the password to login
driver.find_element_by_id("pass").send_keys("Facebook@kous28")
time.sleep(2)
#Clicking on login button
driver.find_element_by_name("login").click()
time.sleep(3)
#Selecting the friend
driver.find_element("xpath","(//span[text()='Kousalya K'])[1]").click()
#sending the different messages
driver.find_element("xpath","//div[@aria-label='Message']").send_keys("hiiii")
time.sleep(2)
driver.find_element("xpath","//div[@aria-label='Press Enter to send']").click()
driver.find_element("xpath","//p[@class='xat24cr xdj266r']").send_keys("Hello123")
driver.find_element("xpath","//div[@aria-label='Press Enter to send']").click()
driver.find_element("xpath","//p[@class='xat24cr xdj266r']").send_keys("!@#$%^")
driver.find_element("xpath","//div[@aria-label='Press Enter to send']").click()
time.sleep(3)

#Sending the like
driver.find_element("xpath","//div[@aria-label='Send a Like']").click()
#choosing the sticker
driver.find_element("xpath","//div[@aria-label='Choose a sticker']").click()
#selecting the sticker
driver.find_element("xpath","(//img[@class=' _5r8c img'])[1]").click()
#sending the sticker
driver.find_element("xpath","//div[@aria-label='Moodies Animated yellow face emoji, grinning and moving its eyes left and right. sticker']").click()
#To click on more actions
# driver.find_element("xpath","//div[@aria-label='Open more actions']").click()
# #To create a room
# driver.find_element("xpath","//span[text()='Create a room']").click()
# time.sleep(3)
#To start a room
# driver.find_element("xpath","//span[text()='Start Now']").click()
# time.sleep(5)
# #To choose the emoji
driver.find_element("xpath","//div[@aria-label='Choose an emoji']").click()
#To select the emoji
driver.find_element("xpath","//img[@src='https://static.xx.fbcdn.net/images/emoji.php/v9/te2/1.5/30/1f603.png']").click()
#To send the emoji
driver.find_element("xpath","//div[@aria-label='Press Enter to send']").click()
# #To close the chatbox
driver.find_element("xpath","//div[@aria-label='Close chat']").click()
time.sleep(2)
# driver.find_element("xpath","//div[@aria-label='Your profile']").click()
#To click on the your profile
driver.find_element("xpath","(//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z'])[1]").click()
#To click on the the logout page
driver.find_element("xpath","//span[text()='Log Out']").click()
# #To enter the receiver's email
# driver.find_element("name","email").send_keys("n4054053@gmail.com")
# #To enter the receiver's password
# driver.find_element("id","pass").send_keys("Facebook@Geetha28")
# #To click on the Login button
# driver.find_element("name","login").click()
# #To click on messenger icon
# driver.find_element("xpath","(//div[@class='x9f619 x1n2onr6 x1ja2u2z'])[3]").click()
#To click on the received messages account
# driver.find_element("xpath","(//span[text()='Kousalya Devi Kodati'])[1]").click()