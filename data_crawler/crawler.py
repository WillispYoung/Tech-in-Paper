from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# # ban image loading
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2
#     }
# }

option = webdriver.ChromeOptions()
# option.add_argument("--proxy-server=http://127.0.0.1:3128")
# option.add_argument('--disable-infobars')
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_extension("ChromeExtensionScrapy.crx")
# option.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome("C:/Python/chromedriver.exe")
browser.minimize_window()

domain = "https://v.qq.com/channel/"
channels = ["tv", "movie", "variety", "cartoon"]
# CDNs = []

output = open("v.qq.com-domains.txt", "w")

for c in channels:
    browser.get(domain + c)
    listItems = browser.find_elements_by_class_name("list_item")

    links = []
    for item in listItems:
        link = item.find_element_by_tag_name("a").get_attribute("href")
        links.append(link)

    for link in links:
        browser.get(link)
        try:
            console_cdn = browser.find_element_by_xpath("//txpdiv[@data-role='txp-ui-console-cdn']")
            # CDNs.append(console_cdn.get_attribute("innerHTML"))
            # print(console_cdn.get_attribute("innerHTML"))
            output.write(console_cdn.get_attribute("innerHTML") + "\n")
        except NoSuchElementException as e:
            print(link)
            continue

browser.close()
output.close()

