i = 1
f = int(input('please enter a number: '))

while i <= 9:
    s = int(input('please enter a number: '))
    if s < f:
        print('not sorted!')
        break
    f = s
    i = i + 1

if i == 10:
    print('sorted')
