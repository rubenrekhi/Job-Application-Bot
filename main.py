from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
profile_path = '~/Users/rubenrekhi/Library/Application Support/Google/Chrome/Default'



chrome_options.add_argument("--user-data-dir=/Users/rubenrekhi/Library/Application Support/Google/Chrome")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)



driver.get("https://simplify.jobs/l/Top-Summer-Internships")
#driver.get('https://google.com')
time.sleep(10)
driver.quit()

