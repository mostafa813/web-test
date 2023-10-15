import os
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
os.environ['PATH'] += r"C:\chromedriver-win64"
driver = webdriver.Chrome()
actions = ActionChains(driver)

def login_user(phoneNumber,userName):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400,1050)
    sleep(3)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(7)
    phone_input = driver.find_element("tag name","input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='ادامه']").click()
    sleep(2)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(8)
    dom = driver.page_source
    assert userName in dom



def login_tashakol(phoneNumber,userName):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400,1050)
    sleep(3)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(7)
    tashakol_select_btn = driver.find_element("xpath","//button[text()='مجموعه']")
    tashakol_select_btn.click()
    sleep(1)
    phone_input = driver.find_element("tag name","input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='ادامه']").click()
    sleep(2)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(6)
    dom = driver.page_source
    assert userName in dom


def sign_in_user(phoneNumber,userName):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400, 1050)
    sleep(3)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(7)
    phone_input = driver.find_element("tag name", "input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='ادامه']").click()
    sleep(2)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(8)
    display_name_input = driver.find_element("xpath", "//input[contains(@class,'w-full rounded-lg')]")
    display_name_input.send_keys(userName)
    driver.find_element("xpath","//h6[text()='تایید']").click()
    sleep(5)
    dom = driver.page_source
    assert userName in dom



def sign_in_tashakol(phoneNumber,userName):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400, 1050)
    sleep(3)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(7)
    tashakol_select_btn = driver.find_element("xpath","//button[text()='مجموعه']")
    tashakol_select_btn.click()
    sleep(1)
    phone_input = driver.find_element("tag name", "input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='ادامه']").click()
    sleep(2)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(8)
    display_name_input = driver.find_element("xpath", "//input[contains(@class,'w-full rounded-lg')]")
    display_name_input.send_keys(userName)
    sleep(1)
    driver.find_element("xpath","//h6[text()='تایید']").click()
    sleep(5)
    dom = driver.page_source
    assert userName in dom

def create_request(phoneNumber,requestTitle):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400, 1050)
    sleep(3)
    profile_page = driver.find_element("xpath", "(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(7)
    phone_input = driver.find_element("tag name", "input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='استمر']").click()
    sleep(3)
    driver.find_element("xpath", "(//h6[text()='حاليا لا'])").click()
    sleep(1)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(5)
    create_request_page = driver.find_element("xpath","//a[@href='/ar/create-form']")
    create_request_page.click()
    sleep(5)
    title = driver.find_element("xpath", "//input[@placeholder='اكتب']")
    title.send_keys(requestTitle)
    sleep(1)
    driver.find_element("tag name","textarea").send_keys("لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ")
    sleep(1)
    driver.find_element("id","map").click()
    sleep(3)
    driver.find_element("xpath","//h6[text()='تأييد المكان المختار']").click()
    sleep(1)
    driver.find_element("xpath","//span[text()='تفاصيل أكثر']").click()
    sleep(30)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    driver.find_element("xpath","//p[@class='text-gray4']").click()
    sleep(1)
    driver.find_element("xpath","(//input[@id='radio'])[2]").click()
    driver.find_element("xpath","(//input[@id='radio'])[4]").click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element("xpath","(//input[@id='radio'])[15]").click()
    sleep(1)
    driver.find_element("xpath","(//textarea[@placeholder='اكتب'])[2]").send_keys("موضوع تستی")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تأييد'])[2]").click()
    sleep(1)
    driver.find_element("id","requirementsList").click()
    sleep(1)
    driver.find_element("xpath","//button[contains(@class,'mb-[19px] w-[52px]')]").click()
    sleep(1)
    driver.find_element("id", "react-select-requirementSelect-placeholder").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='المالية']").click()
    sleep(1)
    driver.find_element("id", "input").send_keys("8460")
    sleep(1)
    driver.find_element("xpath", "(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath", "//button[contains(@class,'mb-[19px] w-[52px]')]").click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='اختيار الاحتياجات']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='المعنوية']").click()
    sleep(1)
    driver.find_element("xpath", "(//textarea[@rows='5'])[2]").send_keys("توضیحات معنوی")
    driver.find_element("xpath", "(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath", "//button[contains(@class,'mb-[19px] w-[52px]')]").click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='اختيار الاحتياجات']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='الفكرة']").click()
    sleep(1)
    driver.find_element("xpath", "(//textarea[@rows='5'])[2]").send_keys("توضیحات ایده")
    driver.find_element("xpath", "(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath", "//button[contains(@class,'mb-[19px] w-[52px]')]").click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='اختيار الاحتياجات']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='الحضورية']").click()
    sleep(1)
    driver.find_element("xpath", "(//textarea[@rows='5'])[2]").send_keys("توضیحات حضور")
    driver.find_element("xpath", "(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath", "//button[contains(@class,'mb-[19px] w-[52px]')]").click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='اختيار الاحتياجات']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='المساعدات']").click()
    sleep(1)
    driver.find_element("xpath", "(//textarea[@rows='5'])[2]").send_keys("توضیحات ظرفیت")
    driver.find_element("xpath", "(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath", "//button[contains(@class,'mb-[19px] w-[52px]')]").click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='اختيار الاحتياجات']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='التخصصات']").click()
    sleep(1)
    driver.find_element("xpath", "(//textarea[@rows='5'])[2]").send_keys("توضیحات تخصصی")
    driver.find_element("xpath", "(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='تأييد']").click()
    sleep(1)
    driver.find_element("xpath", "(//input[@placeholder='اكتب'])[2]").send_keys("تیموری، خ. حبیب الله جنوبی، نرسیده به خ. آزادی، خ. حبیب زادگان.")
    sleep(1)
    driver.find_element("xpath","//input[@id='calendar']").click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath","(//input[@id='calendar'])[2]").click()
    sleep(1)
    driver.find_element("xpath","(//div[text()='02'])[2]").click()
    driver.find_element("xpath","//div[text()='11']").click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath","//div[contains(@class,'my-[25px] lg:mt-[35px]')]//div").click()
    sleep(1)
    driver.find_element("xpath","//label[@class='flex items-center  ']/following-sibling::input[1]").send_keys("تگ 1")
    driver.find_element("xpath","(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("xpath","//label[@class='flex items-center  ']/following-sibling::input[1]").send_keys("تگ 2")
    driver.find_element("xpath","(//h6[text()='تأييد'])[3]").click()
    sleep(1)
    driver.find_element("class name","react-modal-sheet-backdrop").click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element("xpath","(//h6[text()='تأييد'])[2]").click()
    sleep(5)
    driver.find_element("xpath","//p[text()='حساب الطلب']").click()
    sleep(5)
    dom = driver.page_source
    assert requestTitle in dom




def create_project(phoneNumber,projectTitle):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/")
    driver.set_window_size(400,1050)
    sleep(3)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(7)
    tashakol_select_btn = driver.find_element("xpath","//button[text()='مجموعه']")
    tashakol_select_btn.click()
    sleep(1)
    phone_input = driver.find_element("tag name","input")
    phone_input.click()
    sleep(1)
    phone_input.send_keys(Keys.BACKSPACE)
    phone_input.send_keys(Keys.BACKSPACE)
    sleep(2)
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='ادامه']").click()
    sleep(3)
    driver.find_element("xpath", "(//h6[text()='فعلا نه'])").click()
    sleep(1)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(6)
    create_project_page = driver.find_element("xpath","//a[@href='/fa/create-form']")
    create_project_page.click()
    sleep(5)
    title = driver.find_element("xpath", "//input[@placeholder='بنویسید']")
    title.send_keys(projectTitle)
    sleep(1)
    description = driver.find_element("tag name","textarea")
    description.send_keys("لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ")
    sleep(1)
    map = driver.find_element("id","map")
    map.click()
    sleep(3)
    driver.find_element("xpath","//h6[text()='تایید محل انتخاب شده']").click()
    sleep(1)
    more_detailes = driver.find_element("xpath","//span[text()='جزئیات بیشتر']")
    more_detailes.click()
    sleep(30)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    subject_section = driver.find_element("xpath","//p[@class='text-gray4']")
    subject_section.click()
    sleep(1)
    driver.find_element("xpath","(//input[@id='radio'])[2]").click()
    driver.find_element("xpath","(//input[@id='radio'])[4]").click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    other_subject = driver.find_element("xpath","(//input[@id='radio'])[16]")
    other_subject.click()
    sleep(1)
    other_subject_description = driver.find_element("xpath","(//textarea[@placeholder='بنویسید'])[2]")
    other_subject_description.send_keys("موضوع تستی")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید و ثبت'])[2]").click()
    sleep(1)
    requirement_section = driver.find_element("xpath","(//p[@class='text-gray4'])[1]")
    requirement_section.click()
    sleep(1)
    add_requirement_btn = driver.find_element("xpath","//button[contains(@class,'mb-[19px] w-[52px]')]")
    add_requirement_btn.click()
    sleep(1)
    # import pdb; pdb.set_trace()
    driver.find_element("xpath","//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    driver.find_element("xpath","//*[text()='مالی']").click()
    sleep(1)
    financial_amount = driver.find_element("id","input")
    financial_amount.send_keys("8460")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(4)
    # import pdb; pdb.set_trace()
    # driver.find_element("xpath", "//span[text()='معنوی']").click()
    moral_description = driver.find_element("xpath","(//textarea[@rows='5'])[2]")
    moral_description.send_keys("توضیحات معنوی")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='ایده']").click()
    sleep(1)
    idea_description = driver.find_element("xpath","(//textarea[@rows='5'])[2]")
    idea_description.send_keys("توضیحات ایده")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='حضور در رویداد']").click()
    sleep(1)
    in_person_description = driver.find_element("xpath", "(//textarea[@rows='5'])[2]")
    in_person_description.send_keys("توضیحات حضور")
    sleep(1)
    driver.find_element("xpath", "(//h6[text()='تایید'])").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='ظرفیت']").click()
    sleep(1)
    valency_description = driver.find_element("xpath", "(//textarea[@rows='5'])[2]")
    valency_description.send_keys("توضیحات ظرفیت")
    sleep(1)
    driver.find_element("xpath", "(//h6[text()='تایید'])").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='تخصصی']").click()
    sleep(1)
    professional_description = driver.find_element("xpath", "(//textarea[@rows='5'])[2]")
    professional_description.send_keys("توضیحات تخصصی")
    sleep(1)
    driver.find_element("xpath", "(//h6[text()='تایید'])").click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='تایید و ثبت']").click()
    sleep(1)
    address = driver.find_element("xpath","(//input[@placeholder='بنویسید'])[2]")
    address.send_keys("تیموری، خ. حبیب الله جنوبی، نرسیده به خ. آزادی، خ. حبیب زادگان.")
    sleep(1)
    date = driver.find_element("id","calendar")
    date.click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])").click()
    sleep(1)
    start_time = driver.find_element("xpath","(//input[@id='calendar'])[2]")
    start_time.click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])").click()
    sleep(1)
    end_time = driver.find_element("xpath", "(//input[@id='calendar'])[3]")
    end_time.click()
    sleep(1)
    driver.find_element("xpath","//div[text()='10']").click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])").click()
    sleep(1)
    audience = driver.find_element("id","audience")
    audience.click()
    sleep(1)
    start_age = driver.find_element("xpath","//input[@min='0']")
    start_age.send_keys("10")
    end_age = driver.find_element("xpath","(//input[@type='tel'])[2]")
    end_age.send_keys("42")
    sleep(1)
    gender_section = driver.find_element("xpath", "//h6[text()='جنسیت']")
    gender_section.click()
    driver.find_element("id","3").click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید و ثبت'])[3]").click()
    sleep(1)
    tags_section = driver.find_element("xpath","//div[contains(@class,'my-[25px] lg:mt-[35px]')]//div")
    tags_section.click()
    sleep(1)
    tag_input = driver.find_element("xpath","//label[@class='flex items-center  ']/following-sibling::input[1]")
    tag_input.send_keys("تگ 1")
    driver.find_element("xpath","(//h6[text()='تایید و ثبت'])[3]").click()
    sleep(1)
    tag_input.send_keys("تگ 2")
    driver.find_element("xpath","(//h6[text()='تایید و ثبت'])[3]").click()
    sleep(1)
    driver.find_element("class name","react-modal-sheet-backdrop").click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element("xpath","(//h6[text()='تایید و ثبت'])[2]").click()
    sleep(5)
    project_profile_page = driver.find_element("xpath","//p[text()='حساب پروژه']")
    project_profile_page.click()
    sleep(5)
    dom = driver.page_source
    assert projectTitle in dom

create_project("89196549835","پروژه تست وب 23 مهر")