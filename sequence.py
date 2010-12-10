"""
File    sequence.py
"""

import unittest

class sequence:
    """
    Provides helper methods used by the perm class.
    """
    def IsSequence(obj):
        return type(obj) == tuple

class Test(unittest.TestCase):
    def test_MinElt(self):
        pass

    def test_MaxElt(self):
        pass

    def test_IsAllIntegers(self):
        pass

    def test_IsAllSequences(self):
        pass

    def test_IsSequence(self):
        self.assertTrue(sequence.IsSequence((1,2,3)))


if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
