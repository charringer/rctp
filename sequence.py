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
    curmax = None
    for elem in obj:
        if IsSequence(elem):
            value = MaxElt(elem)
        else:
            value = elem
        if curmax == None or value > curmax:
            curmax = value
    return curmax

def MinElt(obj):
    curmin = None
    for elem in obj:
        if IsSequence(elem):
            value = MinElt(elem)
        else:
            value = elem
        if curmin == None or value < curmin:
            curmin = value
    return curmin


# vim:expandtab:softtabstop=4:shiftwidth=4
