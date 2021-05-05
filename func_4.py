print('Enter a number !!')
num = int(input('Number is : '))

temp = num

while num > 1:
    num = num - 1

    temp = temp * num

if num == 0:
    print(1)
else:
    print(temp)