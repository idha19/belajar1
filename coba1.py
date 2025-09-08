from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # biar browser ga auto-close
options.add_argument("--autoplay-policy=no-user-gesture-required")
# options.add_argument("--start-fullscreen") bahaya

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://google.com")