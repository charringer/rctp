import sequence
import unittest

class Test(unittest.TestCase):
    def test_MinElt(self):
        self.assertEqual(1, sequence.MinElt([1,3,4,2]))
        self.assertEqual(1, sequence.MinElt((9,1,2,5)))

    def test_MaxElt(self):
        self.assertEqual(4, sequence.MaxElt([1,3,4,2]))
        self.assertEqual(9, sequence.MaxElt((9,1,2,5)))

    def test_IsAllIntegers(self):
        self.assertTrue(sequence.IsAllIntegers((1,2,3)))
        self.assertFalse(sequence.IsAllIntegers((1,'3')))

    def test_IsAllSequences(self):
        self.assertTrue(sequence.IsAllSequences(((1,2,3),(4,5))))
        self.assertTrue(sequence.IsAllSequences([[1,4],[2,5,3]]))
        self.assertFalse(sequence.IsAllSequences([[12,3],4]))

    def test_IsSequence(self):
        self.assertTrue(sequence.IsSequence((1,2,3)))
        self.assertTrue(sequence.IsSequence([4,5]))
        self.assertFalse(sequence.IsSequence(999))


if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
