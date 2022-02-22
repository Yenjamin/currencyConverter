import requests

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, first, second, amount):
        init = amount
        if first != "USD":
            amount = amount / self.currencies[first]
        amount = round(amount * self.currencies[second], 2)
        return amount