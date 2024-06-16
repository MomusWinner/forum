"""View tests."""
from os import getenv

from django.test import LiveServerTestCase
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

auth_user_name: str = 'test_user_name'
auth_user_password: str = 'test_user_password'

VIEW_HOST = getenv('TEST_REACT_HOST')
LIVE_SERVER_HOST = getenv('TEST_SERVER_HOST')
LIVE_SERVER_PORT = int(getenv('TEST_SERVER_PORT'))

REGISTRATION = 'registration'
LOGIN = 'login'
FORUM = 'forum'


def get_driver():
    options = Options()
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class RegistrationAuthorizationTest(LiveServerTestCase):
    host = LIVE_SERVER_HOST
    port = LIVE_SERVER_PORT

    def setUp(self):
        self.driver = get_driver()

    def authtorization(self):
        self.driver.get(VIEW_HOST + LOGIN)
        input_username = self.driver.find_element(By.NAME, 'username')
        input_userpassword = self.driver.find_element(By.NAME, 'password')
        login_button = self.driver.find_element(By.NAME, 'submit')
        input_username.send_keys(auth_user_name)
        input_userpassword.send_keys(auth_user_password)
        login_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.current_url == VIEW_HOST)

    def registrate(self):
        reqistration_url = VIEW_HOST + REGISTRATION
        self.driver.get(reqistration_url)
        input_username = self.driver.find_element(By.NAME, 'username')
        input_email = self.driver.find_element(By.NAME, 'email')
        input_password = self.driver.find_element(By.NAME, 'password')
        login_button = self.driver.find_element(By.NAME, 'submit')
        input_username.send_keys(auth_user_name)
        input_email.send_keys('test@test.test')
        input_password.send_keys(auth_user_password)
        login_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.current_url == VIEW_HOST + LOGIN)

    def test_registration(self):
        self.registrate()
        self.authtorization()

    def tearDown(self):
        self.driver.quit()


class UnauthorizedTest(LiveServerTestCase):
    host = LIVE_SERVER_HOST
    port = LIVE_SERVER_PORT

    authorization_required_pages = (FORUM,)

    def setUp(self):
        self.driver = get_driver()

    def check_authorization_required_page(self, page: str):
        self.driver.get(VIEW_HOST + page)
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.current_url == VIEW_HOST + LOGIN)

    def test_anauthorized_pages(self):
        for page in self.authorization_required_pages:
            self.check_authorization_required_page(page)
