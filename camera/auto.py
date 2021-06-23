from selenium import webdriver
import time

class Auto ():
    
    def auto():
        navegador = webdriver.Chrome(executable_path="/home/backend/Downloads/chromedriver")
        time.sleep(2)
        navegador.get("http://rasp-01.sa.ngrok.io/")
        username = navegador.find_element_by_id("input_username")
        password = navegador.find_element_by_id("input_password")
        username.send_keys("admin")
        password.send_keys("datarhei")

        time.sleep(1)

        button_login = navegador.find_element_by_xpath("//*[@type='submit']")
        button_login.submit()

        time.sleep(3)

        navegador.find_element_by_xpath('//*[@id="content"]/div[4]/label/input').click()

        time.sleep(2)

        navegador.find_element_by_xpath('//*[@id="content"]/div[7]/div/div').click()

        time.sleep(90)

        navegador.find_element_by_xpath('//*[@id="content"]/div[7]/div[1]').click()







