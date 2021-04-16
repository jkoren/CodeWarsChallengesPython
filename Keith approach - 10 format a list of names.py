#!/usr/bin/python3

'''
Format a string of names like 'Bart, Lisa & Maggie'.
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas
except for the last two names, which should be separated by an ampersand.
'''

import sys

def namelist(uglynames):
    names = [n['name'] for n in uglynames]
    out = []
    if names:
        if len(names) > 1:
            out.append(', '.join(names[:-1]))
        out.append(names[-1])
    print(' & '.join(out))

def main(args):
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    namelist([ {'name': 'Bart'} ])
    namelist([])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))