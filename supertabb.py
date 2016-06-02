from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://www.truthandbeautybombs.com/bb2/")

element = browser.find_elements_by_xpath("//a[contains(@href, './ucp.php?mode=login&sid=31e479abcc6da05a25fc90135e1eef92')]")
element[0].click()
element = browser.find_elements_by_xpath('@href="./ucp.php?i=pm&folder=inbox"')
element[0].click()