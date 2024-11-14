import data
import math
# Write your functions for each part in the space below.

# Part 1
#Purpose: count every vowel in a string
#Input: str
#output: int
#example = ["ever"]
#result = 2
def vowel_count(str) -> int:
    count = 0
    vowels = "aeiouAEIOU"
    for letter in str:
        if letter in vowels:
            count += 1
    return count
print(vowel_count("Hello"))


# Part 2
#Purpose: turn a lists of lists into smaller lists with a length of 2
#Input: list[list[int]]
#output: list[list[int]]
#example = ([1,2,3], [4,5,6]
# #result = [1,2],[3,4],[5,6]
def short_lists(list, n) -> list[list[int]]:
    result = []
    sublist_size = len(list) // n
    for i in range(0, len(list), sublist_size):
        result.append(list[i:i + sublist_size])
    return result
my_list = [1, 2, 3, 4, 5, 6]
print(short_lists(my_list, 2))



# Part 3
#Purpose: remake every list of length 2 to have ascending elements, all kept in original order
#Input: list[list[int]]
#output: [list[list[int]]
#example = [2,0,1],[7,5,6]
#result = [0,1,2],[5,6,7]
def ascending_pairs(input: list[list[int]]) -> list[list[int]]:
    result = []
    for sublist in input:
        if len(sublist) == 2:
            result.append(sorted(sublist))
        else:
            result.append(sublist)
    return result
print(ascending_pairs([[3,2],[6,8],[11,10]]))

# Part 4
#Purpose: Add the prices for two or more instances
#Input: price:float
#output: prince:float
#example = ($12.49 + $13.99)
#result = ($26.48)
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
price1 = Price(5, 30)
price2 = Price(3, 40)
result = adding_prices(price1, price2)
print(result.dollars, result.cents)



# Part 5
#Purpose: calculate rectangle angle
#Input: rectangle
#output: int
#example = x = 6, y = 4
#result = 24
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
rect = Rectangle((4,5), (9,6))
print(rectangle_area(rect))
# Part 6
#Purpose: Show a list of books by a certain author
#Input: str
#output: list[book]
#example = ["George Orwell"]
#result = ["Animal Farm, etc"]
class Book:
    def __init__(self, author: list[str], title: str):
        self.author = author
        self.title = title
def books_by_author(author:str, books: list[Book]) -> list[Book]:
    return [book for book in books if book.author == author]
book1 = Book("Bill", "Aka")
book2 = Book("Charlie", "KiKi")
book3 = Book("Bill", "Bouba")
books = [book1,book2,book3]
books_by_bill = books_by_author("Bill", books)
for book in books_by_bill:
    print(book.title)
# Part 7
#Purpose: return a circle that touches the corners of the rectangle
#Input: rectangle
#output: circle
#example = rectangle(3,4)
#result = circle(diameter = 50

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
rect = Rectangle((3,3),(2,2))
bound_circle = circle_bound(rect)
print(f"{bound_circle.center}")
print(f"{bound_circle.radius}")
# Part 8
#Purpose: See who is being paid less than the average wage
#Input: list[employee]
#output: list[str]
#example = ["Steve"]
#result = [paid less]
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
emp1 = Employee("Amy", 50000)
emp2 = Employee("Bob", 45000)
emp3 = Employee("Cole", 55000)
employees = [emp1,emp2,emp3]
below_avg_employees = below_pay_average(employees)
print(below_avg_employees)