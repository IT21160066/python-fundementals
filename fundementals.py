name = "john"
print(name)
print(str == type(name))
print(isinstance(name, str))

age = 2
print(isinstance(age, int))

# casting
number = "20"
age = int(number)
print(isinstance(age, int))

new_number = float(5)
print(new_number)

# operators
result = 5 // 3
print(result)

# Regular division
print(7 / 3)  # Output: 2.3333333333333335

# Floor division
print(7 // 3)  # Output: 2

print("hello " + "bro")

new_age = 8
new_age += 8
print(new_age)

print(0 and 1)
print(1 and 0)
# print(False and 'hey')


def is_adult(age_check):
    return True if age_check > 18 else False


entered_age = int(input("Enter your age: "))
print(type(entered_age))
answer = is_adult(entered_age)
print(answer)

print("apple".upper())
print("ABcd".lower())

first_name = 'kamal'
print(len(first_name))
print(('amal' in first_name))
print(first_name[0])
print(first_name[1:3])

book1_read = True
book2_read = False
read_any_book = any([book1_read, book2_read])

if read_any_book:
    print('true')

print(abs(-5.5))

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)



