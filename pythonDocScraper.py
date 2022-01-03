from bs4 import BeautifulSoup
import requests
import csv

#You can paste any library link here, I am using struct.html as an example
source = requests.get('https://docs.python.org/3.11/library/struct.html').text
soup = BeautifulSoup(source, 'lxml')

#CSV File to store data.
csv_file = open('documentationScraped.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['method', 'description'])

#Get all functions
functionNames = soup.find_all('dt')
for i in range(0, len(functionNames)):
    elementToText = functionNames[i].text
    elementToText.replace(' ', '')

#Get all descriptions of functions.
descriptions = soup.find_all('dd')

#Print function names and descriptions for debugging purposes
for i in range(0, len(descriptions)):
    print(functionNames[i].text)
    print(descriptions[i].text)

#Add To CSV file
for i in range(0, len(descriptions)):
    elementToPush = functionNames[i].text
    descriptionToPush = descriptions[i].text
    csv_writer.writerow([elementToPush, descriptionToPush])

csv_file.close()