from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://avgle.com/video/kLsNgNqcVNN/animal-and-girls'


chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--proxy-server=127.0.0.1:8080")
# chromeOptions.add_argument("--ignore-certificate-errors")
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(chrome_options = chromeOptions)
# browser = webdriver.Czhrome()
wait = WebDriverWait(browser, 60)
browser.get(URL)

submit = wait.until(
            # 页码输入框的确认
            EC.element_to_be_clickable((By.XPATH, '//i[@class="glyphicon glyphicon-remove-circle"]')))
submit.click()
print(browser.current_url)