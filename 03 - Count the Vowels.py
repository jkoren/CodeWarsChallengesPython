'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

for example getCount("abracadabra") = 5

'''
def isvowel(character):
    if "aeiou".find(character) == -1:
        return False
    else:
        return True
    # reference: https://www.w3schools.com/python/ref_string_find.asp

def getCount(string):
    vowel_count = 0
    for character in string:
        if isvowel(character):
            vowel_count = vowel_count + 1
    return vowel_count

print(getCount("abracadabra"))

# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

#from answer
print(sum(1 for let in "idea" if let in "aeiou"))