from selenium import webdriver
import re,time
def login(driver, username, password):
    # driver.get('http://onestop.ucas.edu.cn/')
    # driver.find_element_by_id('menhuusername').send_keys(username)
    # driver.find_element_by_id('menhupassword').send_keys(password)
	# driver.find_element_by_class_name('loginbtn').click()
    driver.get('http://sep.ucas.ac.cn/')
    driver.find_element_by_id('userName').send_keys(username)
    driver.find_element_by_id('pwd').send_keys(password)
    driver.find_element_by_id('sb').click()
    #进入选课系统
    driver.find_element_by_link_text('选课系统').click()
    #选择学号
    id = driver.find_element_by_id('_id_1')
    if id:
        id.click()
        driver.find_element_by_class_name('btn-primary').click()
    driver.find_element_by_link_text('选修课程').click()

def click_button(driver, element):
    while True:
        try:
            element.click()
            break
        except Exception as e:
            driver.execute_script("window.scrollByPages(1)")

def get_course(driver, parts, courses):
    #选择课程界面
    driver.find_element_by_link_text('选择课程').click()
    for part in parts:
        driver.find_element_by_id(part).click()
    driver.find_elements_by_class_name('btn-primary')[1].click()
    #获取所需选择课程id
    values = []
    codes = []
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        s = link.get_attribute('innerHTML')
        r = re.findall(r'<span id=\"courseCode_(.+?)\">(.+?)</span>',s)
        if r:
            if r[0][1] in courses:
                print(r)
                values.append(r[0][0])
                codes.append(r[0][1])

    #遍历选项框,找到所需课程选择框
    inputs = driver.find_elements_by_name('sids')
    get = False
    for input in inputs:
        v = input.get_attribute('value')
        if v in values:
            disable = input.get_attribute('disabled')
            index = values.index(v)
            if not disable:
                time.sleep(1)
                click_button(driver, input)
                print(v,codes[index],'可选')
                get = True
            else:
                print(v,codes[index],'已满')
    #如果可以选,则选择课程
    if get:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_elements_by_class_name('btn-primary')[0].click()
        driver.find_elements_by_class_name('jbox-button')[0].click()
        print('提交已选课程')
        return True
    else:
        print('没有可选课程')
        return False

if __name__ == '__main__':
    username = '' #sep账号
    password = '' #sep密码
    courses = ['15MGB003H-27', '15MGB003H-28','15MGB003H-33','15MGB003H-34','15MGB003H-35','15MGB003H-51','15MGB003H-52'
				] #课程编号
    parts = ['id_915' #外语系
            ]
    interval = 10 #时间间隔,秒
    flag = True
    while flag:
        try:
            driver = webdriver.Firefox()  #浏览器引擎
            login(driver, username, password)
            failtimes = 0
            while True:
                try:
                    driver.switch_to_default_content()
                except:
                    pass
                try:
                    if get_course(driver, parts, courses):
                        driver.quit()
                        flag = False
                        break
                    time.sleep(interval)
                except Exception as e:
                    print(e)
                    failtimes = failtimes + 1
                    if failtimes == 10:
                        break
        except Exception as e:
            print(e)
            if driver:
                print('quit driver')
                driver.quit()
