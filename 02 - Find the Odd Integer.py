'''
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''
def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

def find_it(list):
    if len(list) == 1:
        return(list[0])

    list.sort()
    previous_item = []
    appearance_count = 0
    list_item_number = 0
    for item in list:
        list_item_number = list_item_number+1
        current_item = item
        if current_item == previous_item:
            appearance_count = appearance_count+1
        else:
            if is_odd(appearance_count):
                return(previous_item) #quit and return as soon as you get an odd count of the same number
            appearance_count = 1  # if they are different, reset count to 1
        previous_item = current_item
        if list_item_number == len(list) and appearance_count==1:  # edge case, count of 1 for last item
            return(current_item)
    return "No integer appears an odd number of times"

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
print(find_it([10]))
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
#test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
#test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
#test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
#test.assert_equals(find_it([10]), 10);
#test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
#test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);