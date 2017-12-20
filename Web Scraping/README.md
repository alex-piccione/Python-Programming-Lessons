# Web Scraping lesson

Lesson about [web scraping](https://en.wikipedia.org/wiki/Web_scraping).  

The idea came to me bacause I was monitoring the prices of some cryptocurrencies on a web page.  
It is not simple to quickly find the Exchange and markets (prices) you are interested in so... I wrote this.  

Python packages:
- requests
- urllib
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

To save the data in a text file we will use a simple class I already have created.  
I can quickly explain it but I prefer not to spent much time on it (consider it a tool).  


## Complete example

A complete working example is in [Final Example](Final%20Example/README.md).

## Proposed features

- Format the output file as HTML or Markdown
- Show the data in a Window (TKinter ?)
    - Show variation of the price with icons and colors  
    - Make possible to select different filters (Exchange/Markets)
- Make the program a running service that update the data every N seconds
- Add other sources for the prices, using other generic sites or the Exchange sites directly, then use the data based on priority of the source
- Save the data on a database to have historical information (MongoDB ?)


## Known issues and Open questions

None. It's perfect!