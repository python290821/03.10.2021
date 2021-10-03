i = 1
_sum = int(input('please enter a number: '))

while i <= 9:
    x = int(input('please enter a number: '))
    if x == _sum:
        break
    _sum = _sum + x
    i = i + 1

print('sum', _sum)
