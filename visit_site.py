from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
                        
driver.get("https://www.reddit.com")
driver.maximize_window()
login_link = driver.find_element(By.LINK_TEXT, "Log In")
login_link.click()
print(login_link)