numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 1
while value in numbers:
    if value < 5:
        print('I\'m # ' + str(value))
        value = value + 1
        continue
        print('I\'m in the if-condition, why are you ignoring me?!')
    elif value == 5:
        break
print('I have reached the last statement in the program and need to exit')