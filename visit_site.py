import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") 
options.add_argument("--disable-web-security") 
options.add_argument("--allow-running-insecure-content") 
options.add_argument('--disable-blink-features=AutomationControlled')

email = ""
password = ""

driver = webdriver.Chrome(service=service, options=options)
                        
driver.get("https://www.reddit.com")
driver.maximize_window()
login_link = driver.find_element(By.LINK_TEXT, "Log In")
login_link.click()
driver.switch_to.new_window()
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-184264444%3A1686612412741342&continue=https%3A%2F%2Faccounts.google.com%2Fgsi%2Fselect%3Fclient_id%3D705819728788-b2c1kcs7tst3b7ghv7at0hkqmtc68ckl.apps.googleusercontent.com%26auto_select%3Dfalse%26ux_mode%3Dpopup%26ui_mode%3Dcard%26as%3DuhUjzf6QjAG1lq1e%252BiQAZQ%26channel_id%3Dfdc9361ff05f5619fa98fed76035d280943da1e4ae9659a8126722a26081d1ca%26origin%3Dhttps%3A%2F%2Fwww.reddit.com&faa=1&ffgf=1&ifkv=Af_xneG7clWNaVHdLfs6exhAF6RQtFOnwrtPM7MnSgX4rBS8NepTRP2oeqT-g22kEvBPKe3LGFuJeA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
find_input_login = driver.find_element("id", "identifierId")
find_input_login.send_keys(email)
find_input_login.send_keys(Keys.RETURN)
time.sleep(5)
input_password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
input_password.send_keys(password)
driver.find_element(By.ID, "passwordNext").click()
# driver.find_element(By.CSS_SELECTOR, "#passwordNext > div > button > span").click()


# driver.close()

# find_google
# print(find_google)