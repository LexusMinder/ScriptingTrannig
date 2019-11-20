#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
type(browser)
browser.get("https://play2048.co/")

htmlElem = browser.find_element_by_tag_name("html")


while True:
    if htmlElem.send_keys(Keys.DOWN):
        continue
    elif htmlElem.send_keys(Keys.LEFT):
        continue
    elif htmlElem.send_keys(Keys.RIGHT):
        continue
    else:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
