#for 2017 results(even)

from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib
from PIL import Image
from pytesseract import image_to_string
import time



roll1=input('Enter Starting roll Number: ') #Starting Roll Number
numberOfIt=input('How many result: ')  #Number of result to be downloaded from starting roll '1' for single result
save=1


#Add a random valid path for captcha location
path='E:/'

#Add a path in which results will be downloaded and saved
savePath='E:/makaut/'

roll=int(roll1)

driver=webdriver.Firefox()

driver.set_window_size(1500,600)  #do not Decrease window size it may give you captcha error
for _ in range(0,int(numberOfIt)):
	driver.get('http://makautexam.net/GradeCardGenerateAndPrint.aspx?Type=UG')
	driver.find_element_by_xpath("//input[@id='txtrollcode']").send_keys(roll)
	driver.find_element_by_xpath("//form[@id='form1']").click()
	time.sleep(2)
	try:
		driver.find_element_by_xpath("//option[@value='03']").click()
	except:
		pass
	srcc=driver.find_element_by_xpath("//img[@alt='Captcha']").get_attribute('src')
	urllib.request.urlretrieve(srcc,'E:/1.png')
	a=Image.open(path+'1.png')    #saving captcha image
	img_info=a.info
	#a.save('E:/hh.png',**img_info)
	b=a.convert('RGBA')   
	num=image_to_string(b)  #using OCR for getting String from text 
	num=num.replace(':',' ') 
	try:
		captcha=eval(num)
	except:
		continue
		
	print(captcha)
	driver.find_element_by_xpath("//input[@id='txtCaptcha']").send_keys(captcha)
	driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
	time.sleep(1)
	try:
		driver.switch_to_alert().accept()
	except:
		save=save+1
		roll=roll+1
		continue
	time.sleep(1)
	driver.save_screenshot(savePath+str(save)+'.png')  #saving result as screenshot
	roll=roll+1
	save=save+1
print('Downloaded in'+savePath)
driver.quit()
driver.switch_to_alert().accept()





