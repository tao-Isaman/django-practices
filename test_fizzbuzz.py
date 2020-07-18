import unittest as ut

def fizzbuzz(number):
    return "Fizz"

#extends class with python
class TestFizzBuzz(ut.TestCase):
    def test_Input3SholdBeShowFizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result , "Fizz")

ut.main()





