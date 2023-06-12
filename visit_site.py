from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
                        
driver.get("https://www.reddit.com")
driver.maximize_window()
# driver.find

