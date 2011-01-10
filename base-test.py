import base
import unittest

class Test(unittest.TestCase):
    def test_number_of_perms(self):
        self.assertEqual(6, len(base.B))
    def test_order_of_elements(self):
        for p in base.B:
            self.assertEqual(4, p.Order())
    def test_fixed_points(self):
        for p in base.B:
            self.assertEqual(34, p.NrFixedPoints(base.N))
        self.assertEqual(6, len(base.fixed_points))
        for p in base.B:
            for fp in base.fixed_points:
                self.assertTrue(p.Image(fp) == fp)

if __name__ == '__main__':
    unittest.main()

# vim:expandtab:softtabstop=4:shiftwidth=4
