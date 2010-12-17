import mathutils
import unittest

class Test(unittest.TestCase):
    def test_lcm_exists(self):
        self.assertEqual(3*5*8, mathutils.lcm(15, 24))


if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
