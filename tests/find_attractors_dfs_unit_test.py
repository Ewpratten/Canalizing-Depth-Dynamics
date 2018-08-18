import unittest
import pyximport
pyximport.install()
import numpy as np

import sys
sys.path.insert(0, '../core')
import find_attractors as fa

class TestAttractors(unittest.TestCase):
    def setUp(self):
        pass

    def test_size_2(self):
        self.assertEqual(fa.find_attractors_and_basins([[0, 0, 0, 1], [0, 1, 1, 1]]),
            [[1, 1],[1, 2],[1, 1]])
 
    def test_size_3(self):
        self.assertEqual(fa.find_attractors_and_basins([[0, 0, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 1, 0]]), [[2, 6],[1, 2]])

    def test_more_than_2_attractor_size(self):
        self.assertEqual(fa.find_attractors_and_basins(
            [[0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0]])
        	, [[4, 6],[2, 2]])

if __name__ == '__main__':
    unittest.main()
