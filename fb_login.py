from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Mo 1 trang web
browser = webdriver.Chrome()
browser.get("https://www.facebook.com")


# Dien thong tin vao o user va pass
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
        txtUser = browser.find_element_by_id("email")
        txtUser.send_keys("maip8807@gmail.com")

        txtPass = browser.find_element_by_id("pass")
        txtPass.send_keys("txb511004")

# Submit form
txtPass.send_keys(Keys.ENTER)

sleep(5)

browser.close()