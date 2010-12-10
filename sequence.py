"""
File    sequence.py
"""

import unittest

class sequence:
    """
    Provides helper methods used by the perm class.
    """

    def IsSequence(obj):
        return (type(obj) == tuple) or (type(obj) == list)

    def IsAllSequences(obj):
        for part in obj:
            if not sequence.IsSequence(part):
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

class Test(unittest.TestCase):
    def test_MinElt(self):
        self.assertEqual(1, sequence.MinElt([1,3,4,2]))
        self.assertEqual(1, sequence.MinElt((9,1,2,5)))

    def test_MaxElt(self):
        self.assertEqual(4, sequence.MaxElt([1,3,4,2]))
        self.assertEqual(9, sequence.MaxElt((9,1,2,5)))

    def test_IsAllIntegers(self):
        self.assertTrue(sequence.IsAllIntegers((1,2,3)))

    def test_IsAllSequences(self):
        self.assertTrue(sequence.IsAllSequences(((1,2,3),(4,5))))
        self.assertTrue(sequence.IsAllSequences([[1,4],[2,5,3]]))

    def test_IsSequence(self):
        self.assertTrue(sequence.IsSequence((1,2,3)))
        self.assertTrue(sequence.IsSequence([4,5]))


if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
