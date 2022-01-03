Program Author:
Adam Luczaj

Purpose:
Scrape function names and descriptions from the python documentation site using a framework used for measuring data and interfacing. 
Coded in a manner so that it will be generalized and work with each documentation topic (I used struct topic).
This project was made to demonstrate knowledge for Python, BeautifulSoup, requests, web scraping, and the concept of grabbing information from a source to be later used. 

Notes:
This project was made for demonstration and learning purposes only.
This program will crash when saving to CSV, this is because there are special characters that must be removed to be able to be processed by CSV files (this is seen during runtime).
The header for the CSV will still be generated in the spreadsheet.
When the error is fixed this README will be updated.

To run:
1. install python if you haven't done so already, if you haven't visit https://www.python.org to install
2. cd into the directory where the file is downloaded and open a terminal
3. run: pip install beautifulsoup4
4. run: pip install lxml
5. run: pip install requests
6. run: python pythonDocScraper.py
7. open the created documentationScraped spreadsheet with your favourite spreadsheet software to see data (I used Excel)
