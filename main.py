import os
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
os.environ['PATH'] += r"C:\chromedriver-win64"
driver = webdriver.Chrome()
actions = ActionChains(driver)

def login():
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400,890)
    sleep(3)
    driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]").click()
    sleep(7)
    phone_input = driver.find_element("tag name","input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys("89155608051")
    sleep(1)
    driver.find_element("tag name","h6").click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='استمر']").click()
    sleep(2)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(6)
    dom = driver.page_source
    assert "یوزر تست وب ۲۷ شهریور" in dom

def sign_in():
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400, 890)
    sleep(3)
    driver.find_element("xpath", "(//p[@class='title2 pt-1 '])[3]").click()
    sleep(7)
    phone_input = driver.find_element("tag name", "input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys("89155608052")
    sleep(1)
    driver.find_element("tag name", "h6").click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='استمر']").click()
    sleep(2)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(10)
    driver.find_element("xpath","//input[contains(@class,'w-full rounded-lg')]").send_keys("یوزر تست وب 28 شهریور")
    driver.find_element("xpath","//h6[text()='تأييد']").click()
    sleep(5)
    dom = driver.page_source
    assert "یوزر تست وب 28 شهریور" in dom



def create_request():
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400, 920)
    sleep(3)
    driver.find_element("xpath", "(//p[@class='title2 pt-1 '])[3]").click()
    sleep(7)
    phone_input = driver.find_element("tag name", "input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys("89155608052")
    sleep(1)
    driver.find_element("tag name", "h6").click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='استمر']").click()
    sleep(2)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(13)
    driver.find_element("xpath","//a[@href='/ar/create-form']").click()
    sleep(5)
    driver.find_element("xpath","//input[@placeholder='اكتب']").send_keys("درخواست تست وب 28 شهریور")
    sleep(1)
    driver.find_element("tag name","textarea").send_keys("لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ")
    sleep(1)
    driver.find_element("id","map").click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='تأييد المكان المختار']").click()
    sleep(1)
    driver.find_element("xpath","//span[text()='تفاصيل أكثر']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    driver.find_element("xpath","//p[@class='text-gray4']").click()
    sleep(1)
    driver.find_element("xpath","(//input[@id='radio'])[2]").click()
    driver.find_element("xpath","(//input[@id='radio'])[4]").click()


    sleep(5)




create_request()

