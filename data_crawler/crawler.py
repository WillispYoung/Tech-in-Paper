from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument("--proxy-server=http://127.0.0.1:3128")
option.add_argument('--disable-infobars')
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_extension("ChromeExtensionScrapy.crx")

browser = webdriver.Chrome("C:/Python/chromedriver.exe")
browser.maximize_window()
browser.get("https://v.qq.com")

links = browser.find_elements_by_tag_name("a")
for link in links:
    print(link.get_attribute("href"))
