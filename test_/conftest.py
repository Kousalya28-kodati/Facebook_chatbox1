import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from library.config import Config
from selenium.webdriver.firefox.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions



@pytest.fixture(params=["Chrome"])
def init_driver(request):
    global driver
    if request.param == "Chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-notification")

        chrome_option.add_argument("--disable-infobars")

        chrome_option.add_argument("start-maximized")

        chrome_option.add_argument("--disable-extensions")

        chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

        chrome_option.add_argument("use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH, options=chrome_option)
    #
    # elif request.param == "Firefox":
    #     options = Options()
    #     options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    #     driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH,options=options)



    # elif request.param == "Edge" :
    #     # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    #     option = EdgeOptions()
    #     option.use_chromium = True
    #     driver = webdriver.Edge(executable_path=Config.EDGE_PATH)


    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    # driver.close()



