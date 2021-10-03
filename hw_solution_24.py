
x = int(input('please enter a 1st number: '))
y = int(input('please enter a 2nd number: '))

if x > y:
    bigger = x
    smaller = y
else:
    bigger = y
    smaller = x

index = 2
biggest_divider = 1
while index <= smaller:
    if bigger % index == 0 and smaller % index == 0:
        biggest_divider = index
    index = index + 1

