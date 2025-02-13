import unittest
from sorting_integers import sort_integers

class TestSortingIntegers(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(sort_integers([3, 1, 4, 1, 5, 9]), ([1, 1, 3, 4, 5, 9], [9, 5, 4, 3, 1, 1]))
        self.assertEqual(sort_integers([10, -1, 2, 8, 0]), ([-1, 0, 2, 8, 10], [10, 8, 2, 0, -1]))
        self.assertEqual(sort_integers([]), ([], []))  
        self.assertEqual(sort_integers([1]), ([1], [1]))  

if __name__ == "__main__":
    unittest.main()
