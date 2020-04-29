# -*- coding: utf-8 -*-
import json
from selenium import webdriver

URL = "https://en.wikipedia.org/wiki/Software_metric"
EXECUTABLE_PATH = "C:\chromedriver\chromedriver.exe" 

def test_app_dynamics_job():
	with open ('output.txt','w') as json_file:
		for result in range(10):
			driver = webdriver.Chrome(executable_path = EXECUTABLE_PATH)
			total = {}
			driver.get ("https://en.wikipedia.org/wiki/Software_metric")
			result = driver.execute_script('return window.performance.getEntries()')
			
			for res in result:
				json_file.write(json.dumps(res,indent=2))
				URL = res["name"]
				URL = res["duration"]
				current_list = total.get(URL,[])
				current_list.append(res["duration"])
				total[URL] = current_list
			print(result)
		driver.quit()

	with open ('output.csv','w') as csv_file:
		csv_file.write(f'URL,duration(ms)\n')
		for key in list(total.keys()):
			average = sum(total[key])/len(total[key])
			print (key,average)
			csv_file.write(f'{key}, {average} \n')

if __name__ == "__main__":
	test_app_dynamics_job()
