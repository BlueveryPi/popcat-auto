from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading


def run():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--mute-audio")
    driver = webdriver.Chrome('D:/anaconda3/envs/py39/codes/assets/chromedriver.exe', options=options)
    driver.implicitly_wait(15)
    driver.get('https://popcat.click/')
    actions = ActionChains(driver)
    body=driver.find_element_by_tag_name('body')
    actions.move_to_element_with_offset(body, 400,250)
    h=actions.move_by_offset(400, 250)
    while True:
        h.click().perform()

for i in range(5):
    t = threading.Thread(target=run)
    t.start()