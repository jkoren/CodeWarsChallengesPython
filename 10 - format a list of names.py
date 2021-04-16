'''
Format a string of names like 'Bart, Lisa & Maggie'.
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand.

try 1 is below:

def get_name(name_value_pair):
    # take this {'name': 'Bart'} and return Bart
    name = name_value_pair["name"]
    return name

def namelist(names):
    name_count = len(names)
    name_string = ""
    if name_count == 0:
        return ""
    elif name_count == 1:
        return get_name(names[0])
    else: #if 2 or more names
        processing = 1 # which name are we processing?
        for name_value_pair in names:
            name = get_name(name_value_pair)
            if processing == name_count-1: # the second to last name
                name_string = name_string + name + ' & '
            elif processing == name_count: # the last name
                name_string = name_string + name
            else: # not the last two names
                name_string = name_string + name + ', '
            processing = processing + 1
        return(name_string)
'''

# try 2 - not finished
def namelist(names):
    if len(names) == 0: return ""
    if len(names) == 1: return names[0]["name"]
    all_but_last = names[0:len(names)-1]
    # print(separator.join(numList))
    return_value = ", ".join(all_but_last["name"])
    return_value = return_value + " & " + names[len(names)]["name"]
    return return_value

#print(get_name({'name': 'Bart'}))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'} ]))
print(namelist([{'name': 'Bart'} ]))
print(namelist([]))



'''
best practice: def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
    
Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''