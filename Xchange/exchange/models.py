from django.db import models

# Represents a bank (like Bank A, Bank B).
class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=200)  # Link to the bank's website
    currencies = ['USD', 'EUR', 'GBP', 'AED', 'SAR', 'CAD', 'AUD', 'CHF', 'SEK', 'JPY', 'ZAR', 'KWD']
    
    def __str__(self):
        return self.name

#  Represents an exchange rate for a specific currency (like USD, EUR) for a particular bank.
class ExchangeRate(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE) 
    currency = models.CharField(max_length=10)  # Currency code like USD, EUR, GBP
    buying_rate = models.DecimalField(max_digits=10, decimal_places=4)  # Buying rate
    selling_rate = models.DecimalField(max_digits=10, decimal_places=4)  # Selling rate
    date = models.DateField(auto_now_add=True)  # Date the rate was scraped

    def __str__(self):
        return f'{self.currency} - {self.bank.name}'