from selenium import webdriver

class ChromeDriverLinux():
    def test(self):
        # driver = webdriver.Chrome(executable_path="/home/global/Desktop/tutorial/driver/chromedriver")
        driver = webdriver.Chrome()
        driver.get("http://www.google.com")

cc = ChromeDriverLinux()
cc.test()