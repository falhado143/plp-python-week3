count = 1
total = 0

# BUG: Missing colon (:) after while condition. Added colon to make the while loop work.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original loop condition was count < 5, which stopped at 4 and missed adding 5.
# Fixed it by changing it to count <= 5.

# BUG: Adding an integer to a string causes an error. Converted total to string using str().
print("Sum of 1 to 5 is: " + str(total))
