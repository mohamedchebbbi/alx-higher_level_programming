#!/usr/bin/python3
''' defines an inherited list '''

class MyList(list):
    '''implements sorted pinting for the built-in list class'''
    def print_sorted(self):
        '''print a list in sorted ascending order'''
        print(sorted(self))
