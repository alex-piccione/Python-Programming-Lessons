# Web Scraping lesson

Lesson about web scraping.  

The idea came to me bacause I was monitoring the prices of some cryptocurrencies on a web page.  
It is not simple to simple find the Exchange and markets (prices) you are interested in so.. I write this.  

Python packages:
- requests
- urllib
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

To save the data in a text file we will use a simple class I already have created.  
I can quickly explain it but I prefer not to spent much time on it (consider it a tool).  


## Proposed features

- Show the data in a Window (TKinter ?)
    - Show variation of the price with icons and colors  
    - Make possible to select different filters (Exchange/MArkets)
- Make the program a running service that update the data every N seconds
- Add other sources for the prices, using other generic sites or the Exchange sites directly, then use the data based on priority of the source
- Save the data on a database to have historical information (MongoDB ?)


## Known issues and Open questions

None. It's perfect!