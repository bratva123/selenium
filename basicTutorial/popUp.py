from selenium import webdriver
import time
class PopUpAlert():
    def test(self):
        driver = webdriver.Chrome();
        # driver.maximize_window()
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        inputBox = driver.find_element_by_id("name")
        inputBox.send_keys("Nishikant Singh")

        alertBtn = driver.find_element_by_id("alertbtn")
        alertBtn.click()
        time.sleep(2)
        alert1 = driver.switch_to_alert()
        alert1.accept()
        time.sleep(2)

        confirmBtn = driver.find_element_by_id("confirmbtn")
        confirmBtn.click()
        time.sleep(2)
        alert2 = driver.switch_to_alert()
        alert2.dismiss()


pa = PopUpAlert()
pa.test()






