
from django.core.management.base import BaseCommand
from exchange.models import Bank
from exchange.scraper import scrape_bank_rates

class Command(BaseCommand):
    help = 'Scrape exchange rates from bank websites'

    def handle(self, *args, **kwargs):
        banks = Bank.objects.all()  # Get all bank URLs
        for bank in banks:
            print(f"Scraping rates for {bank.name} from {bank.url}")
            rates = scrape_bank_rates(bank.url)  # Call the scraping function with the bank URL
            if rates:
                # Save rates to the database here
                print(f"Successfully scraped rates for {bank.name}: {rates}")
