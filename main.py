import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
os.environ['PATH'] += r"C:\chromedriver-win64"
driver = webdriver.Chrome()
actions = ActionChains(driver)
alert = Alert(driver)

def login_user(phoneNumber):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/fa")
    driver.set_window_size(400,1050)
    sleep(1)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(5)
    phone_input = driver.find_element("tag name","input")
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='ادامه دادن']").click()
    sleep(4)
    driver.find_element("xpath", "(//h6[text()='فعلا نه'])").click()
    sleep(1)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(5)
    # dom = driver.page_source
    # assert userName in dom



def login_tashakol(phoneNumber):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/fa")
    driver.set_window_size(400,1050)
    sleep(1)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(5)
    tashakol_select_btn = driver.find_element("xpath","//button[text()='مجموعه']")
    tashakol_select_btn.click()
    sleep(1)
    phone_input = driver.find_element("tag name","input")
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='ادامه دادن']").click()
    sleep(4)
    driver.find_element("xpath", "(//h6[text()='فعلا نه'])").click()
    sleep(1)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(5)
    # dom = driver.page_source
    # assert userName in dom


def sign_in_user(phoneNumber,userName):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/fa")
    driver.set_window_size(400, 1050)
    sleep(1)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(5)
    phone_input = driver.find_element("tag name", "input")
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='ادامه دادن']").click()
    sleep(4)
    driver.find_element("xpath", "(//h6[text()='فعلا نه'])").click()
    sleep(1)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(5)
    display_name_input = driver.find_element("xpath", "//input[contains(@class,'w-full rounded-lg')]")
    display_name_input.send_keys(userName)
    sleep(1)
    driver.find_element("xpath","//h6[text()='تایید']").click()
    sleep(3)
    dom = driver.page_source
    assert userName in dom



def sign_in_tashakol(phoneNumber,userName):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/fa")
    driver.set_window_size(400, 1050)
    sleep(1)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(5)
    tashakol_select_btn = driver.find_element("xpath","//button[text()='مجموعه']")
    tashakol_select_btn.click()
    sleep(1)
    phone_input = driver.find_element("tag name", "input")
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath", "//h6[text()='ادامه دادن']").click()
    sleep(4)
    driver.find_element("xpath", "(//h6[text()='فعلا نه'])").click()
    sleep(1)
    driver.find_element("xpath", "//input[@type='tel']").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath", "(//input[@type='tel'])[4]").send_keys("1")
    sleep(5)
    display_name_input = driver.find_element("xpath", "//input[contains(@class,'w-full rounded-lg')]")
    display_name_input.send_keys(userName)
    sleep(1)
    driver.find_element("xpath","//h6[text()='تایید']").click()
    sleep(5)
    dom = driver.page_source
    assert userName in dom

def create_request(phoneNumber,requestTitle):
    driver.implicitly_wait(5)
    driver.get("https://hnaya.ir/fa")
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
    driver.get("https://hnaya.ir/fa")
    driver.set_window_size(400,1050)
    sleep(3)
    profile_page = driver.find_element("xpath","(//p[@class='title2 pt-1 '])[3]")
    profile_page.click()
    sleep(4)
    tashakol_select_btn = driver.find_element("xpath","//button[text()='مجموعه']")
    tashakol_select_btn.click()
    sleep(1)
    phone_input = driver.find_element("tag name","input")
    phone_input.send_keys(phoneNumber)
    sleep(1)
    send_code_btn = driver.find_element("tag name","h6")
    send_code_btn.click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='ادامه دادن']").click()
    sleep(4)
    driver.find_element("xpath", "(//h6[text()='فعلا نه'])").click()
    sleep(1)
    driver.find_element("xpath","//input[@type='tel']").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    sleep(3)
    create_project_page = driver.find_element("xpath","//a[@href='/fa/create-form']")
    create_project_page.click()
    sleep(3)
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
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    picture = driver.find_element("xpath","//div[contains(@class,'relative w-[70px]')]")
    picture.click()
    driver.find_element("xpath","//button[text()='از گالری']").click()
    sleep(15)
    subject_section = driver.find_element("xpath","//p[@class='text-gray4']")
    subject_section.click()
    sleep(1)
    driver.find_element("xpath","(//input[@type='checkbox'])[2]").click()
    sleep(1)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # other_subject = driver.find_element("xpath","(//input[@type='checkbox'])[16]")
    # other_subject.click()
    # sleep(1)
    # other_subject_description = driver.find_element("xpath","(//textarea[@placeholder='بنویسید'])[2]")
    # other_subject_description.send_keys("موضوع تستی")
    # sleep(1)
    driver.find_element("xpath","(//button[@type='button'])[3]").click()
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
    financial_amount.send_keys("8460000")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])[3]").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    # import pdb; pdb.set_trace()
    driver.find_element("xpath", "//*[text()='معنوی']").click()
    sleep(1)
    moral_description = driver.find_element("xpath","(//textarea[@rows='5'])[2]")
    moral_description.send_keys("توضیحات معنوی")
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])[3]").click()
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
    driver.find_element("xpath","(//h6[text()='تایید'])[3]").click()
    sleep(1)
    add_requirement_btn.click()
    sleep(1)
    driver.find_element("xpath", "//div[text()='انتخاب نیازمندی']").click()
    sleep(1)
    driver.find_element("xpath", "//*[text()='حضوری']").click()
    sleep(1)
    in_person_description = driver.find_element("xpath", "(//textarea[@rows='5'])[2]")
    in_person_description.send_keys("توضیحات حضور")
    sleep(1)
    driver.find_element("xpath", "(//h6[text()='تایید'])[3]").click()
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
    driver.find_element("xpath", "(//h6[text()='تایید'])[3]").click()
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
    driver.find_element("xpath", "(//h6[text()='تایید'])[3]").click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='تایید']").click()
    sleep(1)
    address = driver.find_element("xpath","(//input[@placeholder='بنویسید'])[2]")
    address.send_keys("تیموری، خ. حبیب الله جنوبی، نرسیده به خ. آزادی، خ. حبیب زادگان.")
    sleep(1)
    date = driver.find_element("id","calendar")
    date.click()
    sleep(1)
    start_date = driver.find_element("xpath","//span[text()='۱۳']")
    start_date.click()
    sleep(0.5)
    next_month = driver.find_element("xpath","(//i[@class='rmdp-arrow'])[2]")
    next_month.click()
    sleep(0.5)
    end_date = driver.find_element("xpath","//span[text()='۲۳']")
    end_date.click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])[2]").click()
    sleep(1)
    time = driver.find_element("xpath","(//input[@id='calendar'])[2]")
    time.click()
    sleep(1)
    start_time = driver.find_element("xpath","//div[text()='10']")
    start_time.click()
    sleep(1)
    end_time = driver.find_element("xpath", "(//div[text()='11'])[3]")
    end_time.click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])[2]").click()
    sleep(1)
    audience = driver.find_element("id","audience")
    audience.click()
    sleep(1)
    start_age = driver.find_element("xpath","//input[@min='0']")
    start_age.send_keys("4")
    end_age = driver.find_element("xpath","(//input[@inputmode='numeric'])[2]")
    end_age.send_keys("44")
    sleep(1)
    gender_section = driver.find_element("xpath", "//h6[text()='جنسیت']")
    gender_section.click()
    driver.find_element("xpath","(//input[@name='item'])[3]").click()
    sleep(1)
    driver.find_element("xpath","(//h6[text()='تایید'])[2]").click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
    tags_section = driver.find_element("xpath","//p[text()='انتخاب کنید']")
    tags_section.click()
    sleep(1)
    tag_input = driver.find_element("xpath","//label[@class='flex items-center  ']/following-sibling::input[1]")
    tag_input.send_keys("تگ 1")
    driver.find_element("xpath","(//h6[text()='تایید'])[2]").click()
    sleep(1)
    tag_input.send_keys("تگ 2")
    driver.find_element("xpath","(//h6[text()='تایید'])[2]").click()
    sleep(1)
    driver.find_element("class name","react-modal-sheet-backdrop").click()
    sleep(1)
    driver.find_element("xpath","//h6[text()='تایید']").click()
    sleep(3)
    project_profile_page = driver.find_element("xpath","//p[text()=' مشاهده پروفایل پروژه']")
    project_profile_page.click()
    sleep(5)
    dom = driver.page_source
    assert projectTitle in dom


def create_project_setad(phoneNumber,projectTitle):
    driver.implicitly_wait(5)
    driver.get("https://dashboard.hnaya.ir/login")
    driver.set_window_size(1920,1080)
    sleep(3)
    username= driver.find_element("name","username")
    username.send_keys("my admin")
    sleep(0.5)
    password= driver.find_element("name","password")
    password.send_keys("kashi24M")
    sleep(7)
    enterkey=driver.find_element("tag name","button")
    enterkey.click()
    sleep(4)
    projectsection= driver.find_element("xpath","//span[text()='پروژه ها']")
    projectsection.click()
    sleep(1)
    createproject= driver.find_element("xpath","//p[text()='ایجاد پروژه']")
    createproject.click()
    sleep(4)
    pic=driver.find_element("xpath","//p[text()='انتخاب عکس']")
    pic.click()
    sleep(15)
    title= driver.find_element("name","title")
    title.send_keys(projectTitle)
    sleep(0.5)
    phone= driver.find_element("name","phoneNumber")
    phone.send_keys("+98"+phoneNumber)
    sleep(0.5)
    needs= driver.find_element("xpath","//p[text()='نیازمندی های پروژه']")
    needs.click()
    sleep(1)
    financil= driver.find_element("xpath","//p[text()='مالی']")
    financil.click()
    money= driver.find_element("xpath","//input[@type='number']")
    money.send_keys("8500000000")
    driver.find_element("xpath","//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    moral=driver.find_element("xpath","//p[text()='معنوی']")
    moral.click()
    moralDesc= driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    moralDesc.send_keys("توضیحات معنوی")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    idea= driver.find_element("xpath","//p[text()='ایده']")
    idea.click()
    ideaDesc=driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    ideaDesc.send_keys("توضیحات ایده")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    Capacity = driver.find_element("xpath", "//p[text()='ظرفیت']")
    Capacity.click()
    CapacityDesc = driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    CapacityDesc.send_keys("توضیحات ظرفیت")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    Professional = driver.find_element("xpath", "//p[text()='تخصصی']")
    Professional.click()
    ProfessionalDesc = driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    ProfessionalDesc.send_keys("توضیحات تخصصی")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    inperson = driver.find_element("xpath", "//p[text()='حضوری']")
    inperson.click()
    inpersonDesc = driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    inpersonDesc.send_keys("توضیحات حضوری")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='تاییدنیازمندی']").click()
    sleep(1)
    subject=driver.find_element("xpath","//p[text()='موضوع پروژه']")
    subject.click()
    sleep(1)
    subject1=driver.find_element("xpath","(//input[@type='checkbox'])[3]")
    subject1.click()
    subject2=driver.find_element("xpath","(//input[@type='checkbox'])[4]")
    subject2.click()
    subject3=driver.find_element("xpath","(//input[@type='checkbox'])[5]")
    subject3.click()
    sleep(3)
    calendar=driver.find_element("xpath","//input[@placeholder='تاریخ و زمان']")
    calendar.click()
    sleep(1)
    startDate= driver.find_element("xpath","//span[text()='۱۷']")
    startDate.click()
    endDate= driver.find_element("xpath","//span[text()='۲۷']")
    endDate.click()
    sleep(1)
    address= driver.find_element("name","address")
    address.send_keys("تهران.بلوار ابوذر.")
    sleep(1)
    location= driver.find_element("xpath","//p[text()='انتخاب از نقشه']")
    location.click()
    sleep(5)
    driver.find_element("xpath","(//p[text()='تایید'])[2]").click()
    sleep(1)
    tagsSection= driver.find_element("xpath","//p[text()='برچسب ها']")
    tagsSection.click()
    tags=driver.find_element("xpath","/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[1]/div/div/div/input")
    tags.send_keys("تگ 1")
    addBtn= driver.find_element("xpath","//div[contains(@class,'MuiGrid-root MuiGrid-item')]//button[1]")
    addBtn.click()
    tags.send_keys("تگ 2")
    addBtn.click()
    sleep(4)
    gender= driver.find_element("xpath","//span[text()='زنان']")
    gender.click()
    sleep(5)
    description=driver.find_element("name","description")
    description.send_keys("لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است،")
    sleep(1)
    confirm=driver.find_element("xpath","//p[text()='تایید']")
    confirm.click()
    sleep(5)
    dom = driver.page_source
    assert projectTitle in dom

def create_request_setad(phoneNumber,projectTitle):
    driver.implicitly_wait(5)
    driver.get("https://dashboard.hnaya.ir/login")
    driver.set_window_size(1920,1080)
    sleep(3)
    username= driver.find_element("name","username")
    username.send_keys("my admin")
    sleep(0.5)
    password= driver.find_element("name","password")
    password.send_keys("kashi24M")
    sleep(7)
    enterkey=driver.find_element("tag name","button")
    enterkey.click()
    sleep(4)
    requestsection= driver.find_element("xpath","//span[text()='درخواست ها']")
    requestsection.click()
    sleep(1)
    createrequest= driver.find_element("xpath","//p[text()='ایجاد درخواست']")
    createrequest.click()
    sleep(3)
    pic=driver.find_element("xpath","//p[text()='انتخاب عکس']")
    pic.click()
    sleep(15)
    title= driver.find_element("name","title")
    title.send_keys(projectTitle)
    sleep(0.5)
    phone= driver.find_element("name","phoneNumber")
    phone.send_keys("+98"+phoneNumber)
    sleep(0.5)
    needs= driver.find_element("xpath","//p[text()='نیازمندی های پروژه']")
    needs.click()
    sleep(1)
    financil= driver.find_element("xpath","//p[text()='مالی']")
    financil.click()
    money= driver.find_element("xpath","//input[@type='number']")
    money.send_keys("8500000000")
    driver.find_element("xpath","//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    moral=driver.find_element("xpath","//p[text()='معنوی']")
    moral.click()
    moralDesc= driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    moralDesc.send_keys("توضیحات معنوی")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    idea= driver.find_element("xpath","//p[text()='ایده']")
    idea.click()
    ideaDesc=driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    ideaDesc.send_keys("توضیحات ایده")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    Capacity = driver.find_element("xpath", "//p[text()='ظرفیت']")
    Capacity.click()
    CapacityDesc = driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    CapacityDesc.send_keys("توضیحات ظرفیت")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    Professional = driver.find_element("xpath", "//p[text()='تخصصی']")
    Professional.click()
    ProfessionalDesc = driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    ProfessionalDesc.send_keys("توضیحات تخصصی")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(0.5)
    inperson = driver.find_element("xpath", "//p[text()='حضوری']")
    inperson.click()
    inpersonDesc = driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    inpersonDesc.send_keys("توضیحات حضوری")
    driver.find_element("xpath", "//p[text()='تاییدنیازمندی']").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='تاییدنیازمندی']").click()
    sleep(1)
    subject=driver.find_element("xpath","//p[text()='موضوع پروژه']")
    subject.click()
    sleep(1)
    subject1=driver.find_element("xpath","(//input[@type='checkbox'])[3]")
    subject1.click()
    subject2=driver.find_element("xpath","(//input[@type='checkbox'])[4]")
    subject2.click()
    subject3=driver.find_element("xpath","(//input[@type='checkbox'])[5]")
    subject3.click()
    sleep(3)
    calendar=driver.find_element("xpath","//input[@placeholder='تاریخ و زمان']")
    calendar.click()
    sleep(1)
    date= driver.find_element("xpath","//span[text()='۱۷']")
    date.click()
    sleep(1)
    address= driver.find_element("name","address")
    address.send_keys("تهران.بلوار ابوذر.")
    sleep(1)
    location= driver.find_element("xpath","//p[text()='انتخاب از نقشه']")
    location.click()
    sleep(4)
    driver.find_element("xpath","(//p[text()='تایید'])[2]").click()
    sleep(1)
    tagsSection= driver.find_element("xpath","//p[text()='برچسب ها']")
    tagsSection.click()
    tags=driver.find_element("xpath","/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[1]/div/div/div/input")
    tags.send_keys("تگ 1")
    addBtn= driver.find_element("xpath","//div[contains(@class,'MuiGrid-root MuiGrid-item')]//button[1]")
    addBtn.click()
    tags.send_keys("تگ 2")
    addBtn.click()
    sleep(3)
    description=driver.find_element("name","description")
    description.send_keys("لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است،")
    sleep(1)
    confirm=driver.find_element("xpath","//p[text()='تایید']")
    confirm.click()
    sleep(3)
    dom = driver.page_source
    assert projectTitle in dom

# create_project_setad("9196549894","پروژه تست داشبورد 11 بهمن")
create_project("9196549915","پروژه تست وب 16 اسفند")
# sign_in_tashakol("9196549915","تشکل تست وب 16 اسفند")
