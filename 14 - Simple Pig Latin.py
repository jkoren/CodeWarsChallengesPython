'''
Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def is_punctuation(word):
        return word[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX'

def pig_word(word):
    if is_punctuation(word): return word
    else: return word[1:] + word[0] + "ay"

def pig_it(sentence):
    words_list = sentence.split()
    new_words_list = []

    for word in words_list:
        new_words_list.append(pig_word(word))

    separator = ' '
    return separator.join(new_words_list)

print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !

'''
best practice 1
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
    
best practice 2    
def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)
'''