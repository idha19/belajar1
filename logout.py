from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Setup browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Buka halaman login
driver.get("https://the-internet.herokuapp.com/login")

# 3. Login
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!" + Keys.RETURN)

# 4. Tunggu pesan login
wait = WebDriverWait(driver, 10)
flash = wait.until(EC.presence_of_element_located((By.ID, "flash")))
message_login = flash.text
print("Pesan setelah login:", message_login)
assert "You logged into a secure area!" in message_login

# 5. Klik tombol logout
logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button secondary radius']")))
logout_button.click()

# 6. Tunggu pesan logout muncul
flash_logout = wait.until(EC.presence_of_element_located((By.ID, "flash")))
message_logout = flash_logout.text
print("Pesan setelah logout:", message_logout)
assert "You logged out of the secure area!" in message_logout

# 7. Pastikan kembali ke halaman login
wait.until(EC.presence_of_element_located((By.ID, "username")))
print("✅ Logout berhasil dan kembali ke halaman login")