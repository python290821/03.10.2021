
biggest_positive = 0
x = int(input('please enter a number: '))

if x <= 0:
    print('none positive number was entered')
else:
    while x > 0:
        if x > biggest_positive:
            biggest_positive = x
        x = int(input('please enter a number: '))
    print('biggest positive number is', biggest_positive)

