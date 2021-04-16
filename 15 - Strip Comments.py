'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:
apples, pears # and bananas
grapes
bananas !apples

The output expected would be:
apples, pears
grapes
bananas

The code would be called like so:
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
---
My first thoughts

/first break into lists with \n as delimiter

[["apples, pears # and bananas"],[grapes],[bananas !apples]]

then separate words then with space as delimiter
["apples,","pears","#","and","bananas"]

then search each list, making a new list
   for each word, if it has a delimiter,
      take part before delimter and add to list and stop
    if it does not have a delimiter
      add to list

join lists back together
and add to list

'''

def solution(phrase, delimiters):
    list_of_lines = phrase.split("\n")
    # example output: ['apples, pears # and bananas', 'grapes', 'bananas !apples']
    return_line = []
    new_list_of_lines = []
    for line in list_of_lines:
            first_delimiter_index = -1
            for delimiter in delimiters:
                if line.find(delimiter) != -1:  #if a delimiter is found
                    if first_delimiter_index == -1: #this is the first delimiter found
                        first_delimiter_index = line.find(delimiter)
                    if first_delimiter_index != -1: # if already a delimiter found, take the earlier one
                        if line.find(delimiter) < first_delimiter_index:
                            first_delimiter_index = line.find(delimiter)
            if first_delimiter_index != -1: #if a delimiter was found
                if first_delimiter_index == 0: # if delimiter first character in line:
                    return_line = ""
                else:
                    return_line = line[:first_delimiter_index-1]
            if first_delimiter_index == -1: ## no delimiter found
                return_line = line
                
            new_list_of_lines.append(return_line)
    if len(new_list_of_lines) == 1:
        return new_list_of_lines[0]
    else:
        return "\n".join(new_list_of_lines)



print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print("---")
#print(solution("apples, pears and bananas", ["#", "!"]))
#print(solution("pears watermelons avocados ' strawberries\nstrawberries , apples apples cherries\napples apples # - "
#              "?\n@ pears @ cherries", ['?', '=', '@', '.', '^', '-', ',']))

#print(solution('lemons watermelons lemons strawberries oranges\noranges apples pears =\napples watermelons bananas '
#             'lemons pears\nwatermelons avocados', ['^', '@', '-', '!', "'", '.', '=', ',', '?']))

#print(solution('lemons strawberries\noranges watermelons\nstrawberries lemons watermelons - cherries\nlemons\n@ '
#              'avocados '
#          'lemons', ['-', '^', '?', '@', "'", ',']))

# should equal 'lemons strawberries\noranges watermelons\nstrawberries lemons watermelons\nlemons\n'

print(solution("= bananas oranges\n' pears\napples strawberries lemons pears", ['^', '=', '@', "'"]))
print("---")
# should equal '\n\napples strawberries lemons pears'

'''
best practices
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


'''