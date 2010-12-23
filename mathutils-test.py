import mathutils
import unittest

class Test(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(3*5*8, mathutils.lcm(3*5, 3*8))
    def test_gcd(self):
        self.assertEqual(2, mathutils.gcd(2, 2*3))
        self.assertEqual(2, mathutils.gcd(2*3, 2))
        self.assertEqual(3, mathutils.gcd(3*5, 3*8))
        self.assertEqual(3*5*17, mathutils.gcd(3*5*17*29, 3*8*17))

if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
