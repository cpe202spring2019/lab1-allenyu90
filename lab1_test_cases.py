import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests max list iter for code coverage"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        emptylst = []
        self.assertEqual(max_list_iter(emptylst), None)
        self.assertEqual(max_list_iter([0]), 0)
        lst = [1, 3, 5, 6, 8, 2, 4]
        self.assertEqual(max_list_iter(lst), 8)
        lst1 = [1, 2, 3]
        lst2 = [1, 3, 2]
        lst3 = [3, 1, 2]
        lst4 = [3, 2, 1]
        lst5 = [3, 3, 1]
        lst6 = [2, 3, 3]
        lst7 = [3, 3, 3]
        self.assertEqual(max_list_iter(lst1), 3)
        self.assertEqual(max_list_iter(lst2), 3)
        self.assertEqual(max_list_iter(lst3), 3)
        self.assertEqual(max_list_iter(lst4), 3)
        self.assertEqual(max_list_iter(lst5), 3)
        self.assertEqual(max_list_iter(lst6), 3)
        self.assertEqual(max_list_iter(lst7), 3)

    def test_reverse_rec(self):
        """Tests reverse_rec for code coverage"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([4, 5, 6, 7, 8]), [8, 7, 6, 5, 4])
        self.assertNotEqual(reverse_rec([1, 3, 5, 7, 9]), [9, 7, 5, 1, 3])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([5]), [5])
        tlst = None
        with self.assertRaises(ValueError):
            reverse_rec(tlst)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)
        self.assertEqual(bin_search(4, 6, 4, list_val), None)
        self.assertEqual(bin_search(4, 0, 3, list_val), None )
        self.assertEqual(bin_search(4, 5, len(list_val)-1, list_val), None )


    def test_bin_search_error(self):
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(4, 0, 7, tlist)

    def test_bin_search_empty(self):
        tlist = []
        self.assertEqual(bin_search(4, 0, 5, tlist), None)
        

if __name__ == "__main__":
        unittest.main()

    
