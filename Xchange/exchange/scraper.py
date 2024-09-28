import requests
from bs4 import BeautifulSoup
import urllib3

# Suppress InsecureRequestWarnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_bank_rates(bank_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(bank_url, headers=headers, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    rates = []

    def append_rate(currency, buying_rate, selling_rate):
        """Helper function to append rates if valid."""
        try:
            if buying_rate and selling_rate:  # Check if rates are not empty
                rates.append({
                    'currency': currency,
                    'buying_rate': float(buying_rate.replace(',', '').strip()),
                    'selling_rate': float(selling_rate.replace(',', '').strip())
                })
                print(f"Appended - Currency: {currency}, Buying Rate: {buying_rate}, Selling Rate: {selling_rate}")  # Debugging output
            else:
                print(f"Skipping - Incomplete rates for {currency}")  # Debugging output
        except ValueError as ve:
            print(f"ValueError for {currency} - Buying Rate: {buying_rate}, Selling Rate: {selling_rate}: {ve}")  # Debugging output

    # Attempt to find the table
    table = soup.find('table')  # Adjust this selector based on the actual table
    if table:
        for row in table.find_all('tr')[1:]:  # Skipping the header row
            cells = row.find_all('td')
            if len(cells) >= 3:
                currency = cells[0].text.strip()
                buying_rate = cells[1].text.strip()
                selling_rate = cells[2].text.strip()

                append_rate(currency, buying_rate, selling_rate)
    else:
        print("No exchange rate table found.")

    return rates

