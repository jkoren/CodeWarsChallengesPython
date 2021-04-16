'''
lesson: https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/introduction
data file: https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html

Do not spam the website with a ton of requests. A large number of requests can break a website that is unprepared for that level of traffic. As a general rule of good practice, make one request to one webpage per second.
'''

import requests

# webpage = requests.get('https://www.codecademy.com/articles/http-requests')
# print(webpage.text)

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')


webpage = webpage_response.content
print(webpage)

# need free subscription for the rest
from bs4 import BeautifulSoup
soup = BeautifulSoup(webpage,'html.parser')
print(soup)

'''
A Tag corresponds to an HTML Tag in the original document. These lines of code:

soup = BeautifulSoup('<div id="example">An example div</div><p>An example p tag</p>')
print(soup.div)
Would produce output that looks like:

<div id="example">An example div</div>
Accessing a tag from the BeautifulSoup object in this way will get the first tag of that type on the page.

You can get the name of the tag using .name and a dictionary representing the attributes of the tag using .attrs:

print(soup.div.name)
print(soup.div.attrs)
'''
text = '<div id="example">An example div</div><p>An example p tag</p>'
soup = BeautifulSoup(text, features="html.parser")
print(soup.div)
print(soup.div.name)
print(soup.div.attrs)
print(soup.div.string)

print(soup.h1)
for child in soup.div.children:
  print("HELLO",child)