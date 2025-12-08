# Day 1 

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(2 + 3j))      # Complex number
print(type('jay'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'jay'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


import math

point1 = (2, 3)
point2 = (10, 8)

distance = math.dist(point1, point2)
print(distance)