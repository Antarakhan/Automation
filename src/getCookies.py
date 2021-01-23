from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#for wait till page loads
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#action chains
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\prod\Automate\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#action chain cookie clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)] #reverseorder for bigger ones first

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <=count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()