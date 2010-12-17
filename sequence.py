"""
File    sequence.py

Description
    Provides helper methods used by the perm class.
"""


def IsSequence(obj):
    return (type(obj) == tuple) or (type(obj) == list)

def IsAllSequences(obj):
    for part in obj:
        if not IsSequence(part):
            return False
    return True

def IsAllIntegers(obj):
    for part in obj:
        if not type(part) == int:
            return False
    return True

def MaxElt(obj):
    curmax = obj[0]
    for elem in obj:
        if elem > curmax:
            curmax = elem
    return curmax

def MinElt(obj):
    curmin = obj[0]
    for elem in obj:
        if elem < curmin:
            curmin = elem
    return curmin


# vim:expandtab:softtabstop=4:shiftwidth=4
