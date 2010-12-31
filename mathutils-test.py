import mathutils
import unittest

class Test(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(2, mathutils.gcd(2, 2*3))
        self.assertEqual(2, mathutils.gcd(2*3, 2))
        self.assertEqual(3, mathutils.gcd(3*5, 3*8))
        self.assertEqual(3*17, mathutils.gcd(3*5*17*29, 3*8*17))
    def test_lcm(self):
        self.assertEqual(3*5*8, mathutils.lcm(3*5, 3*8))
    def test_gcd_extreme_cases(self):
        self.assertEqual(9, mathutils.gcd(0, 9))
        self.assertEqual(3, mathutils.gcd(-3*4, -3*5))
        self.assertEqual(0, mathutils.gcd(0, 0))
    def test_lcm_extreme_cases(self):
        self.assertEqual(0, mathutils.lcm(0, 9))
        self.assertEqual(3*4*5, mathutils.lcm(-3*4, -3*5))
        self.assertEqual(0, mathutils.lcm(0, 0))
    def test_gcd_handles_list(self):
        self.assertEqual(6, mathutils.gcd([6]))
        self.assertEqual(3, mathutils.gcd([2*3, -3, 3*5]))
    def test_lcm_handles_list(self):
        self.assertEqual(6, mathutils.lcm([6]))
        self.assertEqual(2*3*5, mathutils.lcm([2*3, -3, 3*5]))

if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
