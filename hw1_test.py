import data
import hw1
import unittest
import math
# Write your test cases for each part below.

def vowel_count(str) -> int:
    count = 0
    vowels = "aeiouAEIOU"
    for letter in str:
        if letter in vowels:
            count += 1
    return count
print(vowel_count("Good"))
print(vowel_count("crypt"))

    # Part 2
def short_lists(my_list, n) -> list[list[int]]:
    result = []
    sublist_size = len(my_list) // n
    for i in range(0, len(my_list), sublist_size):
        result.append(my_list[i:i + sublist_size])
    return result
my_list = []
print(short_lists([23,43,56,12,3,10,78], 2))
print(short_lists([0,-3,9,2,10,7,-1], 2))

    # Part 3
def ascending_pairs(input: list[list[int]]) -> list[list[int]]:
    result = []
    for sublist in input:
        if len(sublist) == 2:
            result.append(sorted(sublist))
        else:
            result.append(sublist)
    return result
print(ascending_pairs([[1,2],[3,4],[5,6]]))
print(ascending_pairs([[6,5],[3,4],[1.1,.6]]))


    # Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents
def adding_prices(price1:Price, price2:Price) ->Price:
        total_dollars = price1.dollars + price2.dollars
        total_cents = price1.cents + price2.cents

        if total_cents >= 100:
            total_dollars += total_cents // 100
            total_cents = total_cents % 100
        return Price(total_dollars, total_cents)
price1 = Price(20, 99)
price2 = Price(10, 99)
result = adding_prices(price1, price2)
print(result.dollars, result.cents)
price1 = Price(1, 00)
price2 = Price(12, 99)
result = adding_prices(price1, price2)
print(result.dollars, result.cents)

    # Part 5
class Rectangle:
    def __init__(self, top_left: tuple[int,int], bottom_right: tuple[int,int]):
        self.top_left = top_left
        self.bottom_right = bottom_right

def rectangle_area(rect: Rectangle) -> int:
    top_left_x, top_left_y = rect.top_left
    bottom_right_x, bottom_right_y = rect.bottom_right
    width = bottom_right_x - top_left_x
    height = top_left_y - bottom_right_y
    return width * height
rect = Rectangle((5,5), (6,1))
print(rectangle_area(rect))
rect = Rectangle((2,10), (3,1))
print(rectangle_area(rect))



    # Part 6
class Book:
    def __init__(self, author: list[str], title: str):
        self.author = author
        self.title = title
def books_by_author(author:str, books: list[Book]) -> list[Book]:
    return [book for book in books if book.author == author]
book1 = Book("George", "Animal")
book2 = Book("Dan", "Bark")
book3 = Book("Ethan", "Colin")
books = [book1,book2,book3]
books_by_dan = books_by_author("Dan", books)
for book in books_by_dan:
    print(book.title)
book1 = Book("Flores", "Igloo")
book2 = Book("Heidi", "Janana")
book3 = Book("Heidi", "Koko")
books = [book1, book2, book3]
books_by_heidi = books_by_author("Heidi", books)
for book in books_by_heidi:
    print(book.title)

    # Part 7
    class Rectangle:
        def __init__(self, top_left: tuple[float, float], bottom_right: tuple[float, float]):
            self.top_left = top_left
            self.bottom_right = bottom_right
    class Circle:
        def __init__(self, center: tuple[float, float], radius: float):
            self.center = center
            self.radius = radius
def circle_bound(rect: Rectangle) -> Circle:
    x1, y1 = rect.top_left
    x2, y2 = rect.bottom_right
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = math.sqrt((x1 - center_x) ** 2 + (y1 - center_y) ** 2)
    return Circle((center_x, center_y), radius)
rect = Rectangle((5,5), (1,1))
bound_circle = circle_bound(rect)
print(f"{bound_circle.center}")
print(f"{bound_circle.radius}")
rect = Rectangle((2,6), (5,0))
bound_circle = circle_bound(rect)
print(f"{bound_circle.center}")
print(f"{bound_circle.radius}")

    # Part 8
class Employee:
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate
def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []
    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)
    below_average = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average
emp1 = Employee("Dale", 12500)
emp2 = Employee("Elli", 15000)
emp3 = Employee("Flores", 20000)
emp4 = Employee("Gina", 30000)
employees = [emp1,emp2,emp3]
below_avg_employees = below_pay_average(employees)
print(below_avg_employees)
empty = []
print(below_pay_average(empty))





if __name__ == '__main__':
    unittest.main()
