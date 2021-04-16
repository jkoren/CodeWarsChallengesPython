'''
In this kata you will create a function that takes a list of non-negative integers and
strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''

def filter_list(list):
    #return a new list with the strings filtered out
    new_list = []
    for item in list:
        if isinstance(item,int):         # if item is a number
            new_list.append(item)        # append to new list
    return new_list

print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))

# after looking at answers, another approach using List Comprehension
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
def filter_list2(list):
  'return a new list with the strings filtered out'
  new_list =  [item for item in list if not isinstance(item, str)]
  return new_list

print(filter_list2([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
#test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2])
#test.assert_equals(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
#test.assert_equals(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])

# credit to: https://stackoverflow.com/questions/402504/how-to-determine-a-python-variables-type