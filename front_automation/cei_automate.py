import unittest
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains


class TestCei(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        # chromedriver_path = CHROME_PATH2
        # service = Service(chromedriver_path)
        # cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def clear_field(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

    def test_01_auth(self):
        self.driver.get("http://portal-auth.dev.crystal.ge:3001/")
        time.sleep(3)
        username = self.driver.find_element(By.ID, "_r_0_")
        username.send_keys("bitara@posta.ge")
        time.sleep(3)
        password = self.driver.find_element(By.ID, "_r_1_")
        password.send_keys("Bank123@")
        time.sleep(3)
        verify_method = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > form > fieldset > div > label:nth-child(2) > span.MuiButtonBase-root.MuiRadio-root.MuiRadio-colorPrimary.PrivateSwitchBase-root.MuiRadio-root.MuiRadio-colorPrimary.MuiRadio-root.MuiRadio-colorPrimary.css-6m95b7 > input")
        verify_method.click()
        time.sleep(3)
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > form > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-fullWidth.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-fullWidth.css-mtp4t3")
        login_button.click()
        time.sleep(5)
        otp_input = self.driver.find_element(By.ID, "_r_6_")
        otp_input.send_keys("0000")
        time.sleep(3)
        submit_otp = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > form > button")
        submit_otp.click()
        time.sleep(5)

    def test_02_credit_info(self):
        self.driver.get("http://cei.dev.crystal.ge:3001/")
        time.sleep(3)

    def test_03_personal_id_search(self):
        personal_id = self.driver.find_element(By.ID, "client-id")
        personal_id.send_keys("01017036846")
        time.sleep(1.5)
        search_button = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.container-fluid.search-div > div > div.col-lg-1.col-md-4.col-sm-12.col-xs-12.no-padding > div > button")
        search_button.click()
        time.sleep(5)

    def test_04_full_name_search(self):
        self.driver.refresh()
        time.sleep(3)
        name = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.container-fluid.search-div > div > div:nth-child(3) > div > input")
        name.send_keys("ბედისა")
        time.sleep(1.5)
        lastname = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.container-fluid.search-div > div > div:nth-child(4) > div > input")
        lastname.send_keys("მაჭარაძე")
        time.sleep(1.5)
        search_button = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#root > div > div.container-fluid.search-div > div > div.col-lg-1.col-md-4.col-sm-12.col-xs-12.no-padding > div > button")
        search_button.click()
        time.sleep(5)
        client_container = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.container-fluid.client-cards-div > div > div")
        assert client_container.is_displayed()
        client_list = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.container-fluid.client-cards-div > div > div > div > div > div > div.card-body > table > tbody > tr")
        client_list.click()
        time.sleep(5)

    def test_05_inside_information(self):
        for _ in range(8):
            bodytag = self.driver.find_element(By.TAG_NAME, "body")
            bodytag.send_keys(Keys.DOWN)
        time.sleep(2)
        current_loan_tab = self.driver.find_element(By.ID, "current-loans-tab")
        current_loan_tab.click()
        time.sleep(2)
        closed_loan_tab = self.driver.find_element(By.ID, "closed-loans-tab")
        closed_loan_tab.click()
        time.sleep(2)
        problem_loan_tab = self.driver.find_element(By.ID, "problem-loans-tab")
        problem_loan_tab.click()
        time.sleep(2)
        administrative_offense_tab = self.driver.find_element(By.ID, "administrative-offense-tab")
        administrative_offense_tab.click()
        time.sleep(2)
        debtors_register_tab = self.driver.find_element(By.ID, "debtors-register-tab")
        debtors_register_tab.click()
        time.sleep(2)
        for _ in range(8):
            bodytag = self.driver.find_element(By.TAG_NAME, "body")
            bodytag.send_keys(Keys.UP)
        time.sleep(2)

    def test_06_change_clicks(self):
        select_date = self.driver.find_element(By.ID, "selectDate")
        select_date.click()
        time.sleep(2)
        for _ in range(7):
            select_date.send_keys(Keys.DOWN)
        time.sleep(2)
        select_date.send_keys(Keys.ENTER)
        time.sleep(2)
        search_button = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#root > div > div.container-fluid.search-div > div > div.col-lg-1.col-md-4.col-sm-12.col-xs-12.no-padding > div > button")
        search_button.click()
        time.sleep(3)