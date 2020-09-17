# Tri567
HW 02a - Testing a legacy program and reporting on testing results  
I pledge my honor that I have abided by the Stevens Honor System  
Miriam Podkolzin
1.	Assignment Description: 
Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.   In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.   You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.  
•	These are the two files:  Triangle.py and TestTriangle.py
o	Triangle.py is a starter implementation of the triangle classification program.  
o	TestTriangle.py  contains a starter set of unittest test cases to test the classifyTriangle() function in the file Triangle.py file.   
In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program.  You will need to update the test program until you feel that your tests adequately test all of the conditions.   Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is.    Capture and then report on those results in a formal test report described below.   For this first part you should not make any changes to the classify triangle program.  You should only change the test program.
Based on the results of your initial tests, you will then update the classify triangle program to fix all defects.  Continue to run the test cases as you fix defects until all of the defects have been fixed.   Run one final execution of the test program and capture and then report on those results in a formal test report described below.   
Note that you should NOT simply replace the logic with your logic from Assignment 1.  Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team.   

2. Author: Miriam Podkolzin
3. Summary: 
Though syntax errors are such a common easy mistake to make, a majority of my errors came from spelling errors. It’s funny I still learn no matter how many years of coding, spelling errors always creep their way in. Something I found that I liked is the process of making test cases. My gut instinct was to use the test cases from the previous homework assignment. Then I ran into some troubles because I had to modify them. For example, an additional output was added instead of NotATriangle for invalid inputs, the output was InvalidInput. Getting inspiration from previous work is nice but worked best for me was to go through the code and verify my test cases covered all the logic.
When updating the Traingle.py code, I found that my test cases told me exactly where the problem was. If it was outputting scalene instead of equilateral, I needed to modify the equilateral if statement. 
5. Honor pledge
I pledge my honor that I have abided by the Stevens Honor System
6. Detailed results, if any:
- Assumptions I made included that the original Triangle.py covered all edge cases for identifying a triangle.  
- Data inputs used were for testing. Inputs were the length of sides of a triangle.   
Test cases used:   
    def testRightTriangleA(self):   
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')  
  
    def testRightTriangleB(self):   
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')    
          
    def testEquilateralTriangles(self):   
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')  
  
    def testIsoscelesTriangles(self):  
        self.assertEqual(classifyTriangle(10,10,12),'Isoceles','Should be Isoceles')  
        self.assertEqual(classifyTriangle(6,7,6), 'Isoceles', 'Should be Isoceles')  
  
    def testTriangle(self):  
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be NotATriangle')  
        self.assertEqual(classifyTriangle(-6,-7,-6), 'InvalidInput', 'Should be InvalidInput')  
  
The strategy I used to decide on a sufficient number of test cases was to think about edge cases from HW 01. I also made sure to cover all logic within Triangle.py. Once all logic was verified, I could decide that it was a sufficient amount of test cases. 

