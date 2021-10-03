# input grades until was input 40 grades or until a grade of 1 or until the average is exactly 99
# If a grade of 0 was input, do not count it for the average
_sum = 0
_avg = 0
number_of_grades = 0

while True: #do-while
    if number_of_grades > 40:
        break
    _grade = int(input('please enter a number: '))
    if _grade == -1:
        break
    if _grade == 0:
        continue
    # if grade == 0 the following lines will not occur
    _sum += _grade
    number_of_grades += 1
    _avg = _sum / number_of_grades
    if _avg == 99:
        break

print('avg is', _avg)

