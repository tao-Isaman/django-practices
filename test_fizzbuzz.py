import unittest as ut

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    


#extends class with python
class TestFizzBuzz(ut.TestCase):
    def test_Input3SholdBeShowFizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result , "Fizz")
    def test_Input6SholdBeShowFizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result , "Fizz")
    def test_Input15SholdBeShowFizzBuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result , "FizzBuzz")

ut.main()





