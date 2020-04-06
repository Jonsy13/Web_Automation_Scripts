from selenium import webdriver

User_ID = "ENTER UR EMAIL ID IN DOUBLE QUOTES"
Password = "ENTER UR PASSWORD IN DOUBLE QOUTES"
chrome_browser  = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.hackerrank.com/auth/login?h_l=body_middle_left_button&h_r=login')

assert 'HackerRank' in chrome_browser.title
user_id = chrome_browser.find_element_by_id('input-1')
password = chrome_browser.find_element_by_id('input-2')
button = chrome_browser.find_element_by_class_name('auth-button')
user_id.clear()
password.clear()
user_id.send_keys(User_ID)
password.send_keys(Password)
button.click()



