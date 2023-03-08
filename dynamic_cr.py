from selenium import webdriver
import time

browser = webdriver.Chrome("C:/Users/sby04/chromedriver_win32/chromedriver")
browser.get("http://www.naver.com")
time.sleep(10)
browser.close()