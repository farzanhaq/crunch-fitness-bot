from selenium.webdriver.support.ui import WebDriverWait


class InputElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_id(self.locator)
        )
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 300).until(
            lambda driver: driver.find_element_by_id(self.locator)
        )
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")
