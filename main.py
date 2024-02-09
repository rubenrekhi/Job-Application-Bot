from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://simplify.jobs/auth/login")
time.sleep(3)
email_input = driver.find_element(By.ID, "email")
email = input("Enter your simplify login email")

email_input.send_keys(email)

pass_input = driver.find_element(By.ID, "password")
password = input("Enter your simplify password")
pass_input.send_keys(password + Keys.ENTER)
time.sleep(10)




driver.get("https://simplify.jobs/l/Top-Summer-Internships")
time.sleep(3)
search_jobs = driver.find_element(By.CLASS_NAME, "block h-11 w-full rounded-md border-gray-300 pl-10 text-base leading-5 transition focus:border-primary-base focus:outline-none focus:ring-4 focus:ring-primary-lightest")
search_jobs.send_keys("Software" + Keys.ENTER)


time.sleep(3)




driver.quit()

