from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless") 

service = Service(r'C:/Users/yonatan.addis/Desktop/python_playground/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://combanketh.et/en/exchange-rate/")
    
    time.sleep(5) 

    table = driver.find_element(By.CLASS_NAME, 'text-left')

    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        cell_data = [cell.text.strip() for cell in cells]
        
        if cell_data:
            cell_data[0] = cell_data[0].split('\n')[-1]
            
            filtered_data = cell_data[:3]
            print(filtered_data) 
finally:
    driver.quit()  
