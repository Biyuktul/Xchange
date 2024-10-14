import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_bank_rates(bank_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver_path = 'C:/Users/yonatan.addis/Desktop/python_playground/chromedriver-win64/chromedriver.exe'  # Update with the correct path
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    print(f"Scraping bank: {bank_url}")
    try:
        driver.get(bank_url)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'table'))
        )

        table = driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.TAG_NAME, 'tr')[3:] 
        rates = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) >= 3:  
                currency = cells[0].text.strip()  
                buying_rate = cells[1].text.strip()  
                selling_rate = cells[2].text.strip()  

                if buying_rate.replace('.', '', 1).isdigit() and selling_rate.replace('.', '', 1).isdigit():
                    rates.append({
                        'currency': currency,
                        'buying_rate': float(buying_rate.replace(',', '').strip()),
                        'selling_rate': float(selling_rate.replace(',', '').strip())
                    })
                else:
                    print(f"Skipping non-numeric rates for {currency} - Buying Rate: {buying_rate}, Selling Rate: {selling_rate}")

        return rates

    except Exception as e:
        print(f"Error occurred while scraping: {e}")
        return []

    finally:
        driver.quit() 