from selenium import webdriver
import  time

class CalenderSelection():
    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window();
        driver.implicitly_wait(3)

        #click Fligt tab
        flightTab = driver.find_element_by_id('tab-flight-tab-hp')
        flightTab.click()

        #click departing Field
        departBtn = driver.find_element_by_id('flight-departing-hp-flight')
        departBtn.click()

        #select date 31
        selectDate = driver.find_element_by_xpath("//div[@class= 'datepicker-cal-month'][position()=1]//tbody//tr[6]//button")
        selectDate.click();

        time.sleep(3)

ff = CalenderSelection()
ff.test1();





