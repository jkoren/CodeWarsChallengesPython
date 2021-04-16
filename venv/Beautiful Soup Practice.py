'''
using beautiful soup - reference:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''

from bs4 import BeautifulSoup
html_doc = "Test.html"

#working with a CSV file
#dataframe = pandas.read_csv('data/pokemon_data.csv')  #something wrong with the pokeman_data.csv

#soup = BeautifulSoup('Test.html','html.parser')
#soup = BeautifulSoup.
#print(soup)

with open('../../Beautiful Soup Practice/Sample HTML File.html', 'r') as file:
    contents = file.read()

    soup = BeautifulSoup(contents, 'html.parser')

    print(soup)
    print(soup.head)

import requests
page = requests('https://youtu.be/E5cSNSeBhjw')
soup = BeautifulSoup(page.content,'html.parser')
print(soup)