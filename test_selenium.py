from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://google.com')
browser.quit()
