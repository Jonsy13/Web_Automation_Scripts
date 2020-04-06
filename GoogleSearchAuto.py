from selenium import webdriver
from selenium.webdriver.common.keys import Keys


Text = "ENTER HERE THE TEXT U WANT TO SEARCH"
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()

chrome_browser.get('https://www.google.co.in/')
text = chrome_browser.find_element_by_class_name('gLFyf')

text.send_keys(Text)
text.send_keys(Keys.RETURN)