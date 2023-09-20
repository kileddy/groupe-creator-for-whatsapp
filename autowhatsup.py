from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get('https://web.whatsapp.com/')
input('Отсканируйте QR-код в браузере и нажмите Enter после входа в WhatsApp Web...')

def create_group():
    try:
        
        new_chat_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[title="Новый чат"]')))
        new_chat_button.click()
        
        new_group_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[title="Новая группа"]')))
        new_group_option.click()
        
        # Добавить участников в группу 
        contacts = ['']
        for contact in contacts:
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.l7jjieqr')))
            search_box.send_keys(contact)
            time.sleep(1)  
            search_box.send_keys(Keys.RETURN)  
        
        
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.d6ll3xky')))
        next_button.click()

        # Добавить админов в группу 
        admins = ['']
        for admin in admins:
            admin_search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[title="Поиск или выбор участника"]')))
            admin_search_box.send_keys(admin)
            time.sleep(1)  
            admin_search_box.send_keys(Keys.RETURN)
        
        # Дать имя группе и создать ее (замените название на свое)
        group_name = 'TestGroupebyKILEDDY'
        group_name_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1PBlB')))
        group_name_box.send_keys(group_name)
        
        create_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.d6ll3xky')))
        create_button.click()
    
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


create_group()


driver.quit() 
