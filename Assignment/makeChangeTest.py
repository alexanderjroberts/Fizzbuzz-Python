import unittest 
import Assignment.makeChange as mc

class MakeChangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0Example0_assertNominalInboundsNWorks(self):
        change = mc.makeChange(5)
        self.assertEqual(change,[0,0,1,0,0,0,0,0])
        
    def test_910_isNoInputHandled(self):
        shouldBeEmptyArray = mc.makeChange()
        self.assertEqual(shouldBeEmptyArray, [])
        
    def test_920_areNonNumericInputsHandled(self):
        shouldBeEmptyArray = mc.makeChange("1.23")
        self.assertEqual(shouldBeEmptyArray, [])   
        
    def test_930_areNegativeNumbersHandled(self):
        shouldBeEmptyArray = mc.makeChange(-1)
        self.assertEqual(shouldBeEmptyArray, []) 
        
    def test_940_lowerBoundTestShouldFail(self):
        shouldBeEmptyArray = mc.makeChange(-0.01)
        self.assertEqual(shouldBeEmptyArray, [])      
            
    def test_950_upperBoundTestShouldFail(self):
        shouldBeEmptyArray = mc.makeChange(50.01)
        self.assertEqual(shouldBeEmptyArray, []) 
        
    def test_010_lowerBoundTestShouldPass(self):   
        changeArray = mc.makeChange(0)
        self.assertEqual(changeArray, [0,0,0,0,0,0,0,0]) 
        
    def test_020_upperBoundTestShouldPass(self):   
        changeArray = mc.makeChange(50)
        self.assertEqual(changeArray, [2,1,0,0,0,0,0,0]) 
        
    def test_030_lowerBoundTestRoundUpShouldPass(self):   
        changeArray = mc.makeChange(-0.004)
        self.assertEqual(changeArray, [0,0,0,0,0,0,0,0]) 
        
    def test_040_upperBoundTestRoundDownShouldPass(self):   
        changeArray = mc.makeChange(50.004)
        self.assertEqual(changeArray, [2,1,0,0,0,0,0,0]) 
        
    def test_050_areCentsHandled(self):   
        changeArray = mc.makeChange(36.41)
        self.assertEqual(changeArray, [1,1,1,1,1,1,1,1]) 