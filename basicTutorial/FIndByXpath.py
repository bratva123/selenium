from selenium import webdriver

class FindByXpathCss():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//div[@class='left-align']//table[@id='product']//tr[3]//td[2]").text
        elementsByXpath = driver.find_element_by_xpath("//td[contains(text(),'Python Programming Language')]//following-sibling::td")
        # for j in elementsByXpath:
        print(elementsByXpath.text)
        driver.close()


ff = FindByXpathCss()
ff.test()
