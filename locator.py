from selenium.webdriver.common.by import By
import datetime


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, "login-email")
    PASSWORD_FIELD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="new_member"]/div[4]/input')


class HomePageLocators(object):
    CLASSES_BUTTON = (By.CSS_SELECTOR, 'a[href="/my-classes"]')


class ClassesPageLocators(object):
    date_time = datetime.datetime.today()
    date_plus_one = (date_time + datetime.timedelta(days=1)).strftime("%A")
    time_minus_two = (date_time + datetime.timedelta(hours=-2)).strftime("%H")

    DAY_BUTTON = (By.CSS_SELECTOR, f"li[data-dayname='{date_plus_one}']")
    TIME_BUTTON = (
        By.XPATH, f"//p[contains(text(),'{time_minus_two}:00 EST')]"
    )
    RESERVE_BUTTON = (By.XPATH, "//span[contains(text(),'Reserve A Spot')]")
    CANCEL_BUTTON = (
        By.XPATH, "//span[contains(text(),'Update / Cancel Reservation')]"
    )
