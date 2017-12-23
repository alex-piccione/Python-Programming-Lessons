import os
from Cryptocurrencies.PricesScreaper import PriceScraper
from FileWriter import FileWriter
from UI.MainWindow import MainWindow

def main():
    
    print("Cryptocurrencies scraper start")

    file_name = "cryptocurrencies.txt"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    destination_file = os.path.join(current_dir, "output", file_name)
    writer = FileWriter(destination_file)
    scraper = PriceScraper(writer)    
    MainWindow(writer, scraper)    

    print("Cryptocurrencies scraper end")


if __name__ == "__main__":
    
    main()
