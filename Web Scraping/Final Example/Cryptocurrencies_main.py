import os
from Cryptocurrencies.PricesScreaper import PriceScraper
from FileWriter import FileWriter

def main():
    
    print("Cryptocurrencies scraper start")
    file_name = "cryptocurrencies.txt"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    destination_file = os.path.join(current_dir, "output", file_name)

    writer = FileWriter(destination_file)

    filter = {
        "exchanges": ["Gatehub", "Bitstamp", "Gate.io", "Binance", "Bitfinex"],
        "markets": ["XRP/USD", "XRP/BTC", "XRP/ETH", "XRP/LTC", "XLM/BTC"]
        }

    scraper = PriceScraper(writer, filter)
    scraper.run()

    print("Cryptocurrencies scraper end")

if __name__ == "__main__":
    
    main()
