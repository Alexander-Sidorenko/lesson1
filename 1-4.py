number = int(input('Введите число, состоящее из нескольких цифр: '))
max = number%10
number = number//10
while number > 0:
    if number%10 > m:
        max = number%10
    number = number//10
print(max)


