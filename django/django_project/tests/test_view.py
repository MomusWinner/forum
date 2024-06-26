"""View tests."""
from os import getenv

from django.test import LiveServerTestCase
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

auth_user_name: str = 'test_user_name'
auth_user_password: str = 'test_user_password'

VIEW_HOST = getenv('TEST_REACT_HOST')
LIVE_SERVER_HOST = getenv('TEST_SERVER_HOST')
LIVE_SERVER_PORT = int(getenv('TEST_SERVER_PORT'))

REGISTRATION = 'registration'
THREAD = 'thread'
PROFILE = 'profile'
LOGIN = 'login'
FORUM = 'forum'


def _authorize(driver: WebDriver) -> None:
    driver.get(VIEW_HOST + LOGIN)
    input_username = driver.find_element(By.NAME, 'username')
    input_userpassword = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.NAME, 'submit')
    input_username.send_keys(auth_user_name)
    input_userpassword.send_keys(auth_user_password)
    login_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url == VIEW_HOST)


def _registrate(driver: WebDriver) -> None:
    reqistration_url = VIEW_HOST + REGISTRATION
    driver.get(reqistration_url)
    input_username = driver.find_element(By.NAME, 'username')
    input_email = driver.find_element(By.NAME, 'email')
    input_password = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.NAME, 'submit')
    input_username.send_keys(auth_user_name)
    input_email.send_keys('test@test.test')
    input_password.send_keys(auth_user_password)
    login_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url == VIEW_HOST + LOGIN)


def _get_driver():
    options = Options()
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class RegistrationAuthorizationTest(LiveServerTestCase):
    """Test registration and authorization."""

    host = LIVE_SERVER_HOST
    port = LIVE_SERVER_PORT

    def setUp(self):
        """Init test."""
        self.driver = _get_driver()

    def test_registration_authorization(self):
        """Test registration and authorization."""
        _registrate(self.driver)
        _authorize(self.driver)


class UnauthorizedTest(LiveServerTestCase):
    """Test unauthorized pages."""

    host = LIVE_SERVER_HOST
    port = LIVE_SERVER_PORT

    authorization_required_pages = (FORUM, THREAD, PROFILE)

    def setUp(self):
        """Init test."""
        self.driver = _get_driver()

    def test_anauthorized_pages(self):
        """Anauthorized page should redirect to login page."""
        for page in self.authorization_required_pages:
            self._check_authorization_required_page(page)

    def _check_authorization_required_page(self, page: str):
        self.driver.get(VIEW_HOST + page)
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.current_url == VIEW_HOST + LOGIN)


class CreateThreadAndMessageTest(LiveServerTestCase):
    """Test thread and message creation."""

    host = LIVE_SERVER_HOST
    port = LIVE_SERVER_PORT

    def setUp(self) -> None:
        """Init test."""
        self.driver = _get_driver()

    def test_create_thread_and_message(self) -> None:
        """Test thread and message creation."""
        _registrate(self.driver)
        _authorize(self.driver)

        thread_title = 'some_thread_title'
        message_body = 'some_message'

        self._create_thread(thread_title)

        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda _: self._find_element_by_text(thread_title) is not None)
        self._find_element_by_text(thread_title).click()

        self._create_message(message_body)

    def _find_element_by_text(self, text) -> None | WebElement:
        return self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")

    def _create_thread(self, thread_title: str) -> None:
        self.driver.get(VIEW_HOST + FORUM)
        create_thread_button = self.driver.find_element(By.ID, 'create-thread-button')
        create_thread_button.click()
        title = self.driver.find_element(By.ID, 'title')
        create_thread_modal_button = self.driver.find_element(
            By.ID, 'create-thread-modal-button',
        )
        title.send_keys(thread_title)
        create_thread_modal_button.click()

    def _create_message(self, message_body):
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.find_element(By.ID, 'create-message-button')).click()
        self.driver.find_element(By.CLASS_NAME, 'w-md-editor-text-input').send_keys(message_body)
        self.driver.find_element(By.ID, 'create-message-modal-button').click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda _: self._find_element_by_text(message_body) is not None)
