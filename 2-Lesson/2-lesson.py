# String to Number Conversions
age_str = "25"
age_num = int(age_str)
print(age_str)

height_str = "1.75"
height_num = float(height_str)  # 1.75 (float)
print(height_num)

print('\n')
# Number to String
price = 19.99
price_str = str(price)      # "19.99"
print(price_str)
print(type(price_str))
print(price + 1)

print('\n')
# Other Conversions
bool_var = bool("True")
print(type(bool_var)) # True
false_val = bool("")         # False
print(type(false_val))
if "":
    print("True")
else:
    print("False")
int(True)        # 1
int(False)       # 0
print(float("inf"))     # Infinity

print('\n')
# What are Exceptions
# TypeError
# "hello" + 42     # TypeError: can't concat str to int

# ValueError
# print(int("hello"))     # ValueError: invalid literal for int()

# ZeroDivisionError
# 10 / 0           # ZeroDivisionError: division by zero

# IndexError
# list = [1, 2]
# list[5]          # IndexError: list index out of range

print('\n')
# Raising Exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def check_age(age):
  if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
  if age < 0:
        raise ValueError("Age cannot be negative!")
      
# print(divide(10, 1))     # ValueError: Cannot divide by zero!
# check_age(9)      # ValueError: Age cannot be negative!

try:
    check_age("10")   # TypeError: Age must be an integer!
except BaseException as e:
    print("Exception happned:: ", e)
    
    
print('\n')
# Custom Exceptions
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Invalid email format!")
      
validate_email("my@example.com")     # InvalidEmailError: Invalid email format!

print('\n')
# Basic Try-Except
# try:
#     num = int(input("Enter a number: "))
# except ValueError as error:
#     print("That's not a valid number!:: ", error)   

# Multiple Exception Types
# try:
#     result = 10 / int(input("Enter a number: "))
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number!")
# except Exception as e:
#     print("An error occurred:: ", e)

# Try-Except-Else-Finally
try:
    file = open("/Users/c5341846/Documents/PM Academy/python-bootcamp-2025/2-Lesson/data.txt")
except FileNotFoundError:
    print("File not found!")
else:
    print("File operations successful!")
finally:
    try:
        file.close()
        print("Everything is fine!")
    except NameError:
        print("File not opened!")

# Catching and Using Exception Information
try:
    age = int("not_a_number")
except ValueError as e:
    print(f"Error occurred: {str(e)}")