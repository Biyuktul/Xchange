# Bank Exchange Rate Scraper API

This Django-based project scrapes exchange rate data from multiple Ethiopian bank websites and exposes an API that returns the rates in JSON format. The API can be used as a backend to display the data in frontend frameworks like React or Angular.

## Features
- Scrapes exchange rates (buying/selling) from 8+ bank websites in Ethiopia.
- Exposes a REST API to access the latest exchange rates.
- Designed for integration with frontend frameworks.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Web Scraping**: Selenium


## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Add bank URLs in the Django admin.
5. Run the server: `python manage.py runserver`
6. Access the API at `127.0.0.1:8000/xchange/run-scraper/`
