from recipe import Recipe
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def testIngredient(self):
        burger = Recipe("burger")
        burger.addIngredient("bun", 2)
        burger.addIngredient("ground beef")
        burger.addIngredient("tomato", "1 slice")

        self.assertEqual(len(burger.getIngredients()), 3) 
        
        burger.removeIngredient("ground beef")
        self.assertFalse("ground beef" in burger.getIngredients())
    
    def testStep(self):
        burger = Recipe("burger")
        burger.addStep("Form ground beef into patty shape")
        burger.addStep("Put patty on pan")
        self.assertEqual(len(burger.getSteps()), 2) 

        burger.addStep("Take buns out", 0)
        self.assertEqual(burger.getSteps()[0], "Take buns out")
        self.assertEqual(burger.getSteps()[1], "Form ground beef into patty shape")
        self.assertEqual(burger.getSteps()[2], "Put patty on pan")

        burger.addStep("Take ground beef out", 0)
        burger.addStep("Put oil on pan", 2)
        self.assertEqual(burger.getSteps()[0], "Take ground beef out")
        self.assertEqual(burger.getSteps()[1], "Take buns out")
        self.assertEqual(burger.getSteps()[2], "Put oil on pan")
        self.assertEqual(burger.getSteps()[3], "Form ground beef into patty shape")
        self.assertEqual(burger.getSteps()[4], "Put patty on pan")

        burger.addStep("Cook patty", 5)
        self.assertEqual(burger.getSteps()[0], "Take ground beef out")
        self.assertEqual(burger.getSteps()[1], "Take buns out")
        self.assertEqual(burger.getSteps()[2], "Put oil on pan")
        self.assertEqual(burger.getSteps()[3], "Form ground beef into patty shape")
        self.assertEqual(burger.getSteps()[4], "Put patty on pan")
        self.assertEqual(burger.getSteps()[5], "Cook patty")

        burger.moveStep(0, 1)
        self.assertEqual(burger.getSteps()[0], "Take buns out")
        self.assertEqual(burger.getSteps()[1], "Take ground beef out")

        burger.removeStep(3)
        self.assertEqual(burger.getSteps()[0], "Take buns out")
        self.assertEqual(burger.getSteps()[1], "Take ground beef out")
        self.assertEqual(burger.getSteps()[2], "Put oil on pan")
        self.assertEqual(burger.getSteps()[3], "Put patty on pan")
        self.assertEqual(burger.getSteps()[4], "Cook patty")


if __name__ == '__main__':
    unittest.main()
