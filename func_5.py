def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


print('Enter a number below!!')
number = int(input('Number is : '))
print('Factorial of this number is : ', fact(number))
