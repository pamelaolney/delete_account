from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
                        
driver.get("https://www.reddit.com")
driver.maximize_window()
login_link = driver.find_element(By.LINK_TEXT, "Log In")
login_link.click()
driver.switch_to.new_window()
time.sleep(3)


driver.close()

# find_google = driver.find_elements(By.CSS_SELECTOR, 'span:contains("Continue with Google")').click()
# find_google
# print(find_google)