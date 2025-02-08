# copilot: disable

### Type Casting Exercises
# 1. Temperature Converter

# Convert temperature input from string to float
# Then convert Celsius to Fahrenheit using F = (C * 9/5) + 32
temperature_celsius = "27.5"
C = float(temperature_celsius)
F = (C * 9/5) + 32
print("Fahrenheit: ", F)

print('---------------------')
# 2. Age Calculator

# Convert birth year to integer and calculate age
birth_year = "1995"
current_year = "2024"
birth_year_int = int(birth_year)
current_year_int = int(current_year)
age = current_year_int - birth_year_int
print("Age: ", age)

print('---------------------')
# 3. Score Average

# Convert scores to floats and calculate average
## 1 - Solution
scores = ["85.5", "90.0", "95.5"]
scores_sum = 0
for item in scores:
  scores_sum += float(item)
avg = scores_sum / len(scores)
print("1 - Solution: Average: ", avg)

## 2 - Solution
scores_float = list(map(float, scores))
avg = sum(scores_float) / len(scores_float)
print("1 - Solution: Average: ", avg)

print('---------------------')
# 4. Boolean Converter

# Convert different values to boolean
value1 = "True"
value2 = "0"
value3 = ""
print(bool(value1))
print(bool(value2))
print(bool(value3))

print('---------------------')
# 5. Mixed Type Operations

# Perform calculations with mixed types
price = "19.99"
quantity = "5"
# Calculate total cost as float
cost = float(price) * int(quantity)
print("Total cost: ", cost)

print('======================')
### Exception Handling Exercises
# 1. Safe Division
# Create a function that safely divides two numbers
# Handle ZeroDivisionError and TypeError
def safe_divide(a, b):
  try:
    print('Division: ', a / b)
  except ZeroDivisionError:
    print('Divider must not be zero')
  except TypeError:
    print('Invalid value')
    
safe_divide(2, 0)
safe_divide(2, '1')

print('----------------------')
# 2. File Reader
# Create a function that safely reads a file
# Handle FileNotFoundError and PermissionError
def read_file(filename):
  try:
    file = open(filename)
  except FileNotFoundError:
    print('File not found')
  except PermissionError:
    print('You have not permission to access the file')
  finally:
    try:
      file.close()
      print(f'File {filename} has been closed successfully')
    except Exception:
      print(f'File {filename} cannot be closed')

read_file('data.txt')
print('----------------------')
# 3. Number Input Validator
# Create a function that gets valid integer input from user
# Keep asking until valid input is received

# 1 - approach:
def get_valid_number1():
  try:
    int(input('Enter a number: '))
    print('The entered number is valid')
  except:
    print('Invalid number entered')
    get_valid_number1()
  
# get_valid_number1()
print('\n')
# 2 - approach:
def get_valid_number2():
  is_valid_num = False
  while not is_valid_num:
    num = input('Enter a number: ')
    try:
      int(num)
      print('The entered number is valid')
      is_valid_num = True
    except:
      print('Invalid number entered')

# get_valid_number2()
print('----------------------')
# 4. List Index Handler
# Create a function that safely accesses list elements
# Handle IndexError
def safe_get_element(lst, index):