import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

base_url = "https://demo.owasp-juice.shop/"

@pytest.fixture
def load_driver(Autouse=True,scope="session"):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if(driver is None):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()