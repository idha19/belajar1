from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# setup browser
driver = webdriver.Chrome()
driver.maximize_window() #agar nanti layar fulll

# buka halaman
driver.get("https://www.youtube.com")

wait = WebDriverWait(driver, 10)

#tunggu search bar muncul lalu ketik "windah basudara"
search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
search_box.send_keys("windah basudara" + Keys.RETURN)

#tunggu hasil pencariaanya muncul ke pertana
first_video = wait.until(EC.element_to_be_clickable((By.XPATH, '(//a[@id="video-title"])[1]'))) #angka 1 itu maka yang klik yang pertama jika 2 maka yang di klik yang kedua dan seterusnya

#klik video pertama
first_video.click()

time.sleep(10)

print("Video pertama 'windah basaudara' berhasil diputar")