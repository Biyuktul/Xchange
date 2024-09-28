from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.http import JsonResponse
from .models import Bank
from .scraper import scrape_bank_rates

# Create your API's here.

@api_view(['GET'])
def hi_api(request):
    if request.method == 'GET':
        current_time = datetime.now().isoformat()
        response_data = {
            "message": "Hi",
            "timestamp": current_time,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    


def run_scraper_view(request):
    banks = Bank.objects.all()
    results = {}
    for bank in banks:
        rates = scrape_bank_rates(bank.url)
        if rates:
            results[bank.name] = rates  # Store the scraped data in a dictionary
    return JsonResponse(results)




import requests
from bs4 import BeautifulSoup

# Define the bank URL
bank_url = "https://combanketh.et/en/exchange-rate/"

# Try to make the request
try:
    response = requests.get(bank_url)
    response.raise_for_status()  # Raise an exception if the request failed
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    response = None

if response:
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table
    table = soup.find('table')
    
    # Print the table to check its structure
    print("Table found:", table)

    if table:
        # Print all rows in the table
        rows = table.find_all('tr')
        for row in rows:
            print("Row data:", row)
