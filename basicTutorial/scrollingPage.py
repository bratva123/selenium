from selenium import webdriver
import time
class ScrollingPage():
    def test(self):
        driver = webdriver.Chrome();
        driver.maximize_window()
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(baseUrl)

        driver.implicitly_wait(3)


        #Scroll Down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)


        #Scroll Up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)

        #Scroll Element View
        element = driver.find_element_by_id("mousehover")
        js = "document.getElementById('mousehover').scrollIntoView(true);"
        driver.execute_script(js)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")


        #Native way to Scroll Element Into View
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view

        print("location : " +str(location))

ff = ScrollingPage()
ff.test()
