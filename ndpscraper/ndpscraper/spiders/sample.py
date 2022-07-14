from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

options = Options()
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path="D:/chromedriver")
driver.get("https://data.gov.in/catalogs?page=2")

card_link = driver.find_element(By.CLASS_NAME, "card-header")
n = driver.find_element(By.CSS_SELECTOR, ".card-header")
print(n.get_attribute())
print(n.accessible_name)
#print(str) #"class","card-header"
print("******", card_link)
print(driver.page_source)
driver.close()
