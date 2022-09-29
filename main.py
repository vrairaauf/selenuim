import requests

import os 
import time
import random
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("./chromedriver")

driver.get("https://www.justkiss.co.uk")
driver.implicitly_wait(10)

f = open("mail.txt","r")
lines = f.readlines()
for email in lines:

	genderArray=["//*[@id='box-quick-signup']/div/div[2]/a[1]", "//*[@id='box-quick-signup']/div/div[2]/a[2]"]
	chooseGender=random.randint(0, 1)



	genderObject=driver.find_element(By.XPATH, genderArray[chooseGender])
	genderUrl=genderObject.get_attribute("href")
	driver.get(genderUrl)

	haveBeenSingleArray=["//*[@id='signup_step_single_length_less_than_6_months']", "//*[@id='signup_step_single_length_from_6_to_12_months']", "//*[@id='signup_step_single_length_from_1_to_2_years']", "//*[@id='signup_step_single_length_more_than_2_years']"]
	chooseSingle=random.randint(0, 3)
	haveBeenSingleObject=driver.find_element(By.XPATH, haveBeenSingleArray[chooseSingle])
	haveBeenSingleObject.click()

	countryObject=driver.find_element(By.XPATH, "//*[@id='signup_step_city_name']")
	countryObject.send_keys("Truro")
	time.sleep(2)
	driver.find_element(By.XPATH, "//*[@id='-option-0']/span[1]").click()
	submitButtonForCountry=driver.find_element(By.XPATH, "//*[@id='new_signup_step']/div[3]/div/input")
	submitButtonForCountry.click()

	nameObject=driver.find_element(By.XPATH, '//*[@id="signup_step_username"]')
	namesArray=["mohamed", "ahmed", "omar", "rayen", "mahmoud"]
	namesChoice=random.randint(0, 4)
	nameObject.send_keys(namesArray[namesChoice])
	time.sleep(1)
	driver.find_element(By.XPATH, '//*[@id="new_signup_step"]/div[2]/div/input').click()


	#choose a day of birth
	driver.find_element(By.XPATH, '//*[@id="signup_step_birthdate_3i"]').click()
	birthDayArray=['//*[@id="signup_step_birthdate_3i"]/option[2]', '//*[@id="signup_step_birthdate_3i"]/option[3]', '//*[@id="signup_step_birthdate_3i"]/option[4]', '//*[@id="signup_step_birthdate_3i"]/option[5]', '//*[@id="signup_step_birthdate_3i"]/option[6]', '//*[@id="signup_step_birthdate_3i"]/option[7]', '//*[@id="signup_step_birthdate_3i"]/option[8]']
	chooseBirthDay=random.randint(0, 5)
	driver.find_element(By.XPATH, birthDayArray[chooseBirthDay]).click()

	#choose a month of birth
	driver.find_element(By.XPATH, '//*[@id="signup_step_birthdate_2i"]').click()
	birthMonthArray=['//*[@id="signup_step_birthdate_2i"]/option[2]', '//*[@id="signup_step_birthdate_2i"]/option[3]', '//*[@id="signup_step_birthdate_2i"]/option[4]', '//*[@id="signup_step_birthdate_2i"]/option[5]', '//*[@id="signup_step_birthdate_2i"]/option[6]', '//*[@id="signup_step_birthdate_2i"]/option[7]', '//*[@id="signup_step_birthdate_2i"]/option[8]']
	chooseBirthMonth=random.randint(0, 6)
	driver.find_element(By.XPATH, birthMonthArray[chooseBirthMonth]).click()

	#choose a year of birth

	driver.find_element(By.XPATH, '//*[@id="signup_step_birthdate_1i"]').click()
	birthYearArray=['//*[@id="signup_step_birthdate_1i"]/option[2]', '//*[@id="signup_step_birthdate_1i"]/option[3]', '//*[@id="signup_step_birthdate_1i"]/option[4]', '//*[@id="signup_step_birthdate_1i"]/option[5]', '//*[@id="signup_step_birthdate_1i"]/option[6]', '//*[@id="signup_step_birthdate_1i"]/option[7]', '//*[@id="signup_step_birthdate_1i"]/option[8]']
	chooseBirthYear=random.randint(0, 6)
	driver.find_element(By.XPATH, birthYearArray[chooseBirthYear]).click()

	#submit button

	driver.find_element(By.XPATH, '//*[@id="new_signup_step"]/div[2]/div/input').click()

	#complete email address

	driver.find_element(By.XPATH, '//*[@id="signup_step_email"]').send_keys(email)
	time.sleep(1)
	
	driver.find_element(By.XPATH, '//*[@id="new_signup_step"]/div[2]/div/input').click()
	#complete a password
	time.sleep(1)
	driver.find_element(By.ID, "signup_step_password").click()
	driver.find_element(By.ID, "signup_step_password").send_keys("jhdgfkjzhefkjs65s6")
	time.sleep(2)
	driver.find_element(By.XPATH, '//*[@id="new_signup_step"]/div[2]/div/input').click()

	#check required checkbox (permission and privacy)

	driver.find_element(By.XPATH, '//*[@id="signup_step_accept_terms"]').click()
	time.sleep(2)
	driver.find_element(By.XPATH, '//*[@id="signup_step_accept_newsletter"]').click()
	driver.find_element(By.XPATH, '//*[@id="signup_step_accept_privacy_policy"]').click()
	driver.find_element(By.XPATH, '//*[@id="new_signup_step"]/div[4]/div/input').click()

	driver.find_element(By.XPATH, '//*[@id="upload-user-images"]/div[1]/div/button').click()
	driver.find_element(By.XPATH, '//*[@id="upload-user-images"]/div[1]/div/button').send_keys(os.getcwd()+"/pexels-photo-7109174.jpeg")
	time.sleep(10)

	driver.find_element(By.XPATH, '//*[@id="user_tags_2"]').click()
	driver.find_element(By.XPATH, '//*[@id="user_tags_4"]').click()
	driver.find_element(By.XPATH, '//*[@id="user_tags_6"]').click()
	time.sleep(3)

	driver.find_element(By.XPATH, '//*[@id="edit_user_2086369"]/div[2]/input').click()

	#complete phone number

	driver.find_element(By.XPATH, '//*[@id="unfreeze_phone_activation_attributes_phone_number"]').send_keys("7720147896")
	driver.find_element(By.XPATH, '//*[@id="new_unfreeze"]/div[2]/div/input').click()

os.system("pause")