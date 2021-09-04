# bounce.py
#
# Exercise 1.5

height = 100
bounce_percentage = 3/5.0

for i in range(10):
    height = bounce_percentage * height
    print(i, round(height, 4))