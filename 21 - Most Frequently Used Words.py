'''
Most frequently used words in a text
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.

'''

def increment_word_count(dict,key):
    if key in dict.keys(): dict[key] += 1
    else: dict[key] = 1
    return dict

def has_chars(string):
    for letter in string:
        if letter.isalpha(): return True
    return False

def top_3_words(string):
    dict = {}
    letters = "abcdefghijklmnopqrstuvwxyz'"
    word = ""

    for letter in string:
        if letter.lower() in letters:
            word += letter.lower()
        elif has_chars(word):
            dict = increment_word_count(dict, word)
            word = ""

    if has_chars(word): dict = increment_word_count(dict, word) #add last word
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    return_list, count = [], 0
    while count < min(3,len(sorted_dict)):
        return_list += [sorted_dict[count][0]]
        count += 1
    return return_list

print(top_3_words("Now - is the winter Of our discontent."))

print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not "
                  "long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, "
                  "a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on "
                  "most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, "
                  "made away with three-quarters of his income."))

print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
# => ["e", "ddd", "aa"]

print(top_3_words("  //wont won't won't"))
# => ["won't", "wont"]

print(top_3_words("  ...  ")) #, [])
print(top_3_words("  '  ")) #, [])
print(top_3_words("  '''  ")) #, [])

print("how to use Regular Expressions")
'''
https://www.regular-expressions.info/python.html
Call re.search(regex, subject) to apply a regex pattern to a subject string. 

'''
print("How to use counter")
# https://stackabuse.com/introduction-to-pythons-collections-module/

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a':2, 'b':3, 'c':1}))
print(collections.Counter(a=2, b=3, c=1))
test = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
for letter, count in test.most_common(2):
    print(letter, count)
print(list(test))
print(list(test.elements()))
'''
best practices

#1
from collections import Counter
import re

def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]
  
#2  
import re
from collections import Counter

top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]
'''