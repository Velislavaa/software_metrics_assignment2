import json
from selenium
import webdriver
url = 'https://en.wikipedia.org/wiki/Software_metric#See_also'
driver = webdriver.Chrome()
driver.get(url)
json_text = driver.find_element_by_css_selector('pre').get_attribute('innerText')
json_response = json.loads(json_text)