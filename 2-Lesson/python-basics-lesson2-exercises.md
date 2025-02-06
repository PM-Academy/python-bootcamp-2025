# Python Basics - Lesson 2
## Practice Exercises

### Type Casting Exercises
1. **Temperature Converter**
   ```python
   # Convert temperature input from string to float
   # Then convert Celsius to Fahrenheit using F = (C * 9/5) + 32
   temperature_celsius = "27.5"
   # Your code here
   ```

2. **Age Calculator**
   ```python
   # Convert birth year to integer and calculate age
   birth_year = "1995"
   current_year = "2024"
   # Your code here
   ```

3. **Score Average**
   ```python
   # Convert scores to floats and calculate average
   scores = ["85.5", "90.0", "95.5"]
   # Your code here
   ```

4. **Boolean Converter**
   ```python
   # Convert different values to boolean
   value1 = "True"
   value2 = "0"
   value3 = ""
   # Your code here
   ```

5. **Mixed Type Operations**
   ```python
   # Perform calculations with mixed types
   price = "19.99"
   quantity = "5"
   # Calculate total cost as float
   # Your code here
   ```

### Exception Handling Exercises
1. **Safe Division**
   ```python
   # Create a function that safely divides two numbers
   # Handle ZeroDivisionError and TypeError
   def safe_divide(a, b):
       # Your code here
       pass
   ```

2. **File Reader**
   ```python
   # Create a function that safely reads a file
   # Handle FileNotFoundError and PermissionError
   def read_file(filename):
       # Your code here
       pass
   ```

3. **Number Input Validator**
   ```python
   # Create a function that gets valid integer input from user
   # Keep asking until valid input is received
   def get_valid_number():
       # Your code here
       pass
   ```

4. **List Index Handler**
   ```python
   # Create a function that safely accesses list elements
   # Handle IndexError
   def safe_get_element(lst, index):
       # Your code here
       pass
   ```

5. **Custom Exception**
   ```python
   # Create a custom exception for password validation
   # Raise exception if password is less than 8 characters
   class PasswordTooShortError(Exception):
       pass
   
   def validate_password(password):
       # Your code here
       pass
   ```

### Function Exercises
1. **Shopping Cart Calculator**
   ```python
   # Create a function that calculates total price with discount
   def calculate_total(items, discount=0):
       # Your code here
       pass
   ```

2. **Email Generator**
   ```python
   # Create a function that generates email from first and last name
   def generate_email(first_name, last_name, domain="company.com"):
       # Your code here
       pass
   ```

3. **Arguments Counter**
   ```python
   # Create a function that counts total number of arguments
   def count_args(*args, **kwargs):
       # Your code here
       pass
   ```

4. **Temperature Converter Function**
   ```python
   # Create a function that converts between Celsius and Fahrenheit
   def convert_temperature(temp, unit="C"):
       # Your code here
       pass
   ```

5. **Password Generator**
   ```python
   # Create a function that generates random password
   def generate_password(length=8, include_special=True):
       # Your code here
       pass
   ```

### List Exercises
1. **List Manipulator**
   ```python
   # Create functions to add, remove, and find elements
   numbers = [1, 2, 3, 4, 5]
   # Add number at specific position
   # Remove number
   # Find number index
   ```

2. **List Statistics**
   ```python
   # Calculate average, minimum, maximum of a list
   scores = [85, 92, 78, 90, 88]
   # Your code here
   ```

3. **List Filter**
   ```python
   # Filter out negative numbers from list
   numbers = [1, -2, 3, -4, 5, -6]
   # Your code here
   ```

4. **List Merger**
   ```python
   # Merge two sorted lists keeping the result sorted
   list1 = [1, 3, 5]
   list2 = [2, 4, 6]
   # Your code here
   ```

5. **Duplicate Remover**
   ```python
   # Remove duplicates while preserving order
   items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
   # Your code here
   ```

### Tuple Exercises
1. **Coordinate System**
   ```python
   # Create functions to work with point coordinates
   point1 = (3, 4)
   point2 = (6, 8)
   # Calculate distance between points
   # Find midpoint
   ```

2. **Tuple Unpacker**
   ```python
   # Unpack different sized tuples with default values
   def unpack_info(info_tuple):
       # Your code here
       pass
   ```

3. **Data Swapper**
   ```python
   # Swap values between two variables using tuple unpacking
   x = 5
   y = 10
   # Your code here
   ```

4. **Tuple Sorter**
   ```python
   # Sort list of tuples based on second element
   data = [(1, 5), (2, 3), (3, 8), (4, 1)]
   # Your code here
   ```

5. **Tuple Counter**
   ```python
   # Count occurrences of each element in tuple
   numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
   # Your code here
   ```

### Set Exercises
1. **Unique Characters**
   ```python
   # Find unique characters in a string using set
   text = "hello world"
   # Your code here
   ```

2. **Common Elements**
   ```python
   # Find common elements between three lists using sets
   list1 = [1, 2, 3, 4, 5]
   list2 = [4, 5, 6, 7, 8]
   list3 = [5, 6, 7, 8, 9]
   # Your code here
   ```

3. **Set Operations**
   ```python
   # Implement union, intersection, difference without using built-in operations
   set1 = {1, 2, 3, 4}
   set2 = {3, 4, 5, 6}
   # Your code here
   ```

4. **Palindrome Checker**
   ```python
   # Check if string is palindrome using sets
   def is_palindrome(text):
       # Your code here
       pass
   ```

5. **Subset Checker**
   ```python
   # Check if one list is subset of another using sets
   list1 = [1, 2, 3]
   list2 = [1, 2, 3, 4, 5]
   # Your code here
   ```

### Dictionary Exercises
1. **Contact Manager**
   ```python
   # Create functions to add, update, delete contacts
   contacts = {}
   def manage_contacts(action, name, info=None):
       # Your code here
       pass
   ```

2. **Word Counter**
   ```python
   # Count frequency of each word in a text
   text = "the quick brown fox jumps over the lazy dog"
   # Your code here
   ```

3. **Grade Calculator**
   ```python
   # Calculate grade statistics for a class
   grades = {
       "Alice": [85, 90, 95],
       "Bob": [75, 80, 85],
       "Charlie": [95, 95, 98]
   }
   # Your code here
   ```

4. **Dictionary Merger**
   ```python
   # Merge two dictionaries with custom conflict resolution
   dict1 = {"a": 1, "b": 2}
   dict2 = {"b": 3, "c": 4}
   # Your code here
   ```

5. **Nested Dictionary Navigator**
   ```python
   # Create function to safely navigate nested dictionaries
   data = {
       "user": {
           "profile": {
               "name": "Alice",
               "age": 25
           }
       }
   }
   def get_nested_value(dict_obj, keys):
       # Your code here
       pass
   ```

### Solutions Guidelines
1. Try to solve exercises on your own first
2. If stuck, break the problem into smaller steps
3. Test your solution with different inputs
4. Consider edge cases
5. Compare your solution with others
6. Ask for help if needed
