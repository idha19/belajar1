from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # biar browser ga auto-close
options.add_argument("--autoplay-policy=no-user-gesture-required")
# options.add_argument("--start-fullscreen") bahaya

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://google.com")
driver2.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# Isi username
driver2.find_element(By.ID, "username").send_keys("tomsmith")

# Isi password
driver2.find_element(By.ID, "password").send_keys("SuperSecretPassword!" + Keys.RETURN)

time.sleep(3)

# Cek pesan hasil login
message = driver2.find_element(By.ID, "flash").text
print("Pesan dari sistem:", message)