from retangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
    self.r1 = Rectangle(1)
    self.r2 = Rectangle(1)
    self.r3 = Rectangle(1, 2)
    self.r4 = Rectangle(4, 6)
    self.r5 = Rectangle(3, 5)

def test_get_perim(self):
    self.assertEqual(self.r1.perimetr(), self.r2.perimetr())
    self.assertNotEqual(self.r1.perimetr(), 2)

def test_equal_rects(self):
    )

def test_sub_rects(self):
    self.assertEqual(self.r4 - self.r1, self.r5)


if __name__ == '__main__':
    unittest.main(verbosity=10)