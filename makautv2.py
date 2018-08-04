# this script is for downloading MAKAUT  results 

#   n= number of results
#   roll= initial roll
#   sem=semester


from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import sys
import time


n=200
sem=4

roll=int('10400316040')
savePath=sys.path[0]

c=1
driver=webdriver.Chrome(executable_path='/home/rakesh/py/selenium_drivers/chromedriver')
driver.set_window_position(3000,4000)

for r in range(roll,(roll+n)):
	i=0
	while(True):
		try:
			driver.get('https://makaut.ucanapply.com/smartexam/public/result-details')
			print(".")
			break
		except:
			i+=1
			if(i>5):
				break
			else:
				continue

	while(True):
		try:
			driver.find_element_by_xpath('//*[@id="username"]').send_keys(r)
			print("..")
			break
		except:
			i+=1
			if(i>5):
				break
			else:
				continue
	
	while(True):
			try:
				driver.find_element_by_xpath('//*[@id="semester"]/option['+str(sem+1)+']').click()
				print("...")
				break
			except:
				i+=1
				if(i>5):
					break
				else:
					continue

	while(True):
			try:
				driver.find_element_by_xpath('//*[@id="result-search-panal"]/div[2]/div[1]/button').click()
				print("....")
				break
			except:
				i+=1
				if(i>5):
					break
				else:
					continue

	driver.fullscreen_window()
	driver.execute_script("window.scrollTo(0, 580)")
	time.sleep(1)
	driver.save_screenshot(savePath+str(r)+'.png')  #saving result as screenshot
	print("saved iamge  "+str(c))
	c+=1
	driver.set_window_position(3000,4000)

	time.sleep(1)
driver.quit()
