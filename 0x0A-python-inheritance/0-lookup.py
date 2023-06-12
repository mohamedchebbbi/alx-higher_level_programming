#!/usr/bin/python3
'''define an object attribute lookup func'''

def lookup(obj):
    '''return list of an object available attribute'''
    return (dir(obj))
