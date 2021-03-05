#!/usr/local/bin/python3

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page
import config
import pause
import datetime
import time


class ReserveSpot(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        prefs = {}
        options.experimental_options["prefs"] = prefs
        prefs["profile.default_content_settings"] = {"images": 2}

        self.driver = webdriver.Chrome(
            "/usr/local/bin/chromedriver", options=options
        )

        self.driver.get("https://members.crunchfitness.ca/members/sign_in")

    def test_reserve(self):
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches(), "Title does not match"
        login_page.input_username_element = config.Config.USERNAME
        login_page.input_password_element = config.Config.PASSWORD
        login_page.click_login_button()
        now = datetime.datetime.now()
        pause.until(datetime.datetime(
            now.year, now.month, now.day, now.hour + 1, 0
        ))
        home_page = page.HomePage(self.driver)
        assert home_page.is_classes_found(), "Classes are not found"
        home_page.click_classes_button()
        classes_page = page.ClassesPage(self.driver)
        assert classes_page.is_day_found(), "Day is not found"
        classes_page.click_day_button()
        assert classes_page.is_time_found(), "Time is not found"
        classes_page.click_time_button()
        assert classes_page.is_reserve_found(), "Reservation is not found"
        classes_page.click_reserve_button()
        time.sleep(120)
        self.driver.refresh()
        assert classes_page.is_cancel_found(), "Reservation is full"

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
