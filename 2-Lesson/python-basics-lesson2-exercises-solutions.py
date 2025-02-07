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

print('---------------------')