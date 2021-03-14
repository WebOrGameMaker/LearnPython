class NumberIterator:
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number

    def __iter__(self):
        self.current_number = self.start_number
        return self
    
    def __next__(self):
        if self.current_number > self.end_number:
            self.current_number =  self.start_number
        next_value = self.current_number
        self.current_number += 1
        return next_value

if __name__ == '__main__':
    import unittest
    class NumberIteratorUnitTest(unittest.TestCase):
        def test1(self):
            li3 = NumberIterator(0, 3)
            li3_iterator = iter(li3)
            assert next(li3_iterator) == 0
            assert next(li3_iterator) == 1
            assert next(li3_iterator) == 2
            assert next(li3_iterator) == 3
            assert next(li3_iterator) == 0
        
        def test2(self):
            li57 = NumberIterator(5, 7)
            li57_iterator = iter(li57)
            assert next(li57_iterator) == 5
            assert next(li57_iterator) == 6
            assert next(li57_iterator) == 7
            assert next(li57_iterator) == 5
    unittest.main()