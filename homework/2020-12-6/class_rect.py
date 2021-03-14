import unittest
class Rect:
    def __init__(self, width, length, color="Red"): # arg color is optional
        self.width = int(width)
        self.length = int(length)
        self.color = color
    
    @property
    def perimeter(self):
        return self.width*2 + self.length*2
    
    @property
    def area(self):
        return self.width*self.length

class RectUnittest(unittest.TestCase):
    def test_rect1(self):
        rect1 = Rect(2, 3, "Turquoise")
        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect1.length, 3)
        self.assertEqual(rect1.perimeter, 10)
        self.assertEqual(rect1.area, 6)
        self.assertEqual(rect1.color, "Turquoise")

if __name__ == "__main__":
    unittest.main()
