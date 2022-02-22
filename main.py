import convert
import display

if __name__ == "__main__":
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = convert.RealTimeCurrencyConverter(url)
    display.app(converter)