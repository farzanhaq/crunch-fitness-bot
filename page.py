from locator import *
from element import InputElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOCATOR_VAL_IDX = 1


class InputUsernameElement(InputElement):
    locator = LoginPageLocators.USERNAME_FIELD[LOCATOR_VAL_IDX]


class InputPasswordElement(InputElement):
    locator = LoginPageLocators.PASSWORD_FIELD[LOCATOR_VAL_IDX]


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    input_username_element = InputUsernameElement()
    input_password_element = InputPasswordElement()

    def is_title_matches(self):
        return "Sign-in" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()


class HomePage(BasePage):

    def is_classes_found(self):
        return "My Classes" in self.driver.page_source

    def click_classes_button(self):
        element = self.driver.find_element(*HomePageLocators.CLASSES_BUTTON)
        element.click()


class ClassesPage(BasePage):

    def is_day_found(self):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(ClassesPageLocators.DAY_BUTTON)
        )

    def is_time_found(self):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(ClassesPageLocators.TIME_BUTTON)
        )

    def is_reserve_found(self):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(ClassesPageLocators.RESERVE_BUTTON)
        )

    def is_cancel_found(self):
        return WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located(ClassesPageLocators.CANCEL_BUTTON)
        )

    def click_day_button(self):
        element = self.driver.find_element(*ClassesPageLocators.DAY_BUTTON)
        element.click()

    def click_time_button(self):
        element = self.driver.find_element(*ClassesPageLocators.TIME_BUTTON)
        element.click()

    def click_reserve_button(self):
        element = self.driver.find_element(*ClassesPageLocators.RESERVE_BUTTON)
        element.click()
