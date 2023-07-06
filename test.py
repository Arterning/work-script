from selenium import webdriver
import time

def wait():
    time.sleep(3)


def scrollSlowly():
    scheight = 9.9
    while scheight > .1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight -= .002

searchEngine = "https://cn.bing.com/"

driver = webdriver.Chrome()
driver.get(searchEngine)

excludeSomething = "nodejs -CSDN"
inUrl = "java inurl:stackoverflow"
searchText = "nodejs -CSDN"
driver.find_element("id", "sb_form_q").send_keys(searchText)
driver.find_element("id", "search_icon").click()
scrollSlowly()

while True:
    driver.find_element("xpath", "/html/body/div[1]/main/ol/li[14]/nav/ul/li[6]/a").click()
    scrollSlowly()
    time.sleep(10)
