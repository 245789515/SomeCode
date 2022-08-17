from selenium import webdriver
url = "http://210.77.16.21:80/eportal/index.jsp?wlanuserip=328be82e8ed6086faf6325a38a79e475&wlanacname=5fcbc245a7ffdfa4&ssid=&nasip=2c0716b583c8ac3cbd7567a84cfde5a8&mac=908f22a9769994760e32c47fc30aab32&t=wireless-v2&url=d20b79da3e12046dd6075edb8d6491feb801ca0516776129"
username = ''
password = ''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(driver_path='<path-to-driver>/chromedriver', chrome_options=chrome_options,service_args=['--verbose', '--log-path=<path-to-log>/chromedriver.log'])
driver = webdriver.Chrome(driver_path='/root/chromedriver',chrome_options=chrome_options)

driver.get(url)
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('pwd').send_keys(password)
driver.find_element_by_id('loginLink_div').click()
