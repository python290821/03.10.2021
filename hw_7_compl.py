import math

biggest_positive = math.nan # Not a Number
x = int(input('please enter a number: ')) # -1

while x > 0:
    if math.isnan(biggest_positive):
        biggest_positive = x
    elif x > biggest_positive:
        biggest_positive = x
    x = int(input('please enter a number: '))

print('biggest positive number is', biggest_positive)

