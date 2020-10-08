# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(10,10,12),'Isoceles','Should be Isoceles')
        self.assertEqual(classify_triangle(6,7,6), 'Isoceles', 'Should be Isoceles')

    def testTriangle(self):
        self.assertEqual(classify_triangle(10,15,30),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classify_triangle(-6,-7,-6), 'InvalidInput', 'Should be InvalidInput')
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

