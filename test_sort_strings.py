import unittest
from sorting_strings import sort_strings

class TestSortStrings(unittest.TestCase):
    def test_sort_strings(self):
        
        input_list = ["banana", "apple", "cherry"]
        expected_output = ["apple", "banana", "cherry"]
        self.assertEqual(sort_strings(input_list), expected_output)

        
        self.assertEqual(sort_strings([]), [])

        
        self.assertEqual(sort_strings(["apple"]), ["apple"])

        
        input_list = ["Banana", "apple", "cherry"]
        expected_output = ["Banana", "apple", "cherry"]
        self.assertEqual(sort_strings(input_list), expected_output)

        
        input_list = ["10", "2", "1"]
        expected_output = ["1", "10", "2"]
        self.assertEqual(sort_strings(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()