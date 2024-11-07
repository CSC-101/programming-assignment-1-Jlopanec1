import data
import hw1
import unittest
class TestCases(unittest.TestCase):

# Write your test cases for each part below.

    def find_vowels(sentence):
     count = 0
     vowels = "aeiouAEIOU"
     for letter in sentence:
            if letter in vowels:
                count += 1





        # Part 2


    # Part 3


    # Part 4
class Price:
    def add_prices(basket):
        # Initialize the variable that will be used for the calculation
        total = 0
        # Iterate through the dictionary items
        for item, price in basket.items():
            # Add each price to the total calculation
            # Hint: how do you access the values of
            # dictionary items?
            total += price
        # Limit the return value to 2 decimal places
        return round(total, 2)
    groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
                 "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
    print(add_prices(groceries))

    # Part 5
    class Rectangle:
        # Initialize a new Rectangle object.
        # input: top-left corner as a Point
        # input: bottom-right corner as a Point
        def __init__(self, top_left: Point, bottom_right: Point):
            self.top_left = top_left
            self.bottom_right = bottom_right
        def test_Rectangle_1(self):
            rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
            self.assertEqual(rectangle.top_left, data.Point(7, 20))
            self.assertEqual(rectangle.bottom_right, data.Point(12, 10))


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
