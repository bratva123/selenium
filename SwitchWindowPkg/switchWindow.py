from selenium import webdriver
import time
class SwitchWindow():
    def test(self):
        driver = webdriver.Chrome();
        driver.maximize_window()
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(4)

        #find the parent handle -> main  Wiindow
        parentHandle = driver.current_window_handle
        print(parentHandle)

        #find open window and click
        openWindow = driver.find_element_by_id("openwindow")
        openWindow.click()
        time.sleep(3)

        #find all the handles , there should two hna=dle after clicking open window button
        handles = driver.window_handles
        for handle in handles:
            print("handle : "+ handle)
            if handle not in parentHandle:
                driver.switch_to_window(handle)
                print("switched to windows : "+handle)
                inputBox = driver.find_element_by_id("search-courses")
                inputBox.send_keys("python")
                time.sleep(3)
                driver.close()




        # inputBox = driver.find_element_by_id("search-courses")
        # inputBox.send_keys("python")

sw = SwitchWindow()
sw.test()