from selenium import webdriver
import time
class SwitchWindow():

    def __init__(self,driver,baseUrl):
        self.driver = driver
        self.baseUrl = baseUrl
        self.parrentHandle = self.driver.current_window_handle

    def basicSetup(self):
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(4)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def cancelLogin(self):
        self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()

    def login(self, username, psw):
        emailInput = self.driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']")
        emailInput.send_keys("XYZ")

        pswInput = self.driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
        pswInput.send_keys("XYZ")
        time.sleep(3)
        loginBtn = self.driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']")
        loginBtn.click()

    def search(self, keyword):
        searchBox = self.driver.find_element_by_xpath("//div[@class='O8ZS_U']//input")
        searchBox.send_keys(keyword)

        searchBtn = self.driver.find_element_by_xpath("//button[@class='vh79eN']")
        searchBtn.click()

    def filter(self):
        chkBox = self.driver.find_element_by_xpath("//div[contains(text(),'In the Ear')]")
        chkBox.click()

    def opeartion(self):
        allItems = self.driver.find_elements_by_xpath("//div[@class='_1HmYoV _35HD7C'][position()=2]//div[@class='_3O0U0u']//div[@class='_3liAhj']")
        for item in allItems:
            item.click()
            time.sleep(5)
            handles = self.driver.window_handles
            if handles[1] not in self.parrentHandle:
                self.driver.switch_to_window(handles[1])
                pinInput = self.driver.find_element_by_id("pincodeInputId")
                pinInput.send_keys("201304")
                time.sleep(2)
                check = self.driver.find_element_by_class_name("_2aK_gu")
                check.click()
                time.sleep(7)

                msg = self.driver.find_element_by_xpath("//div[@class='_13J5uS']").text

                if msg == "Currently out of stock in this area.":
                    print("cant order")
                    self.driver.close()
                    self.driver.switch_to_window(self.parrentHandle)
                    time.sleep(3)



driver = webdriver.Chrome()
baseUrl = "https://flipkart.com"

sw = SwitchWindow(driver, baseUrl)

sw.basicSetup()

sw.cancelLogin()
time.sleep(5)

sw.search("headphone")
time.sleep(20)


sw.filter()
time.sleep(10)

sw.opeartion()
time.sleep(3)


        
