from selenium import webdriver

class FindByIdName():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("radio-btn-example")

        if elementById is not None:
            print("we found an element by id")

        elementByName = driver.find_element_by_name("cars")
        driver.find_by_x

        if elementByName is not None:
            print("we found an element by Name")


ff = FindByIdName()
ff.test()
