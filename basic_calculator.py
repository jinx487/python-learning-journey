num1 = int(input('Enter an interger: '))
num2 = int(input('Enter an interger: '))
op = input('Enter an operator: ')

if op == '+':
    print('The addition is ', num1+num2)
elif op == '-':
    print('The substraction is ', num1-num2)
elif op == '*':
    print('The multiplication is ', num1*num2)
elif op == '/':
    print('The division is ', num1/num2)
else:
    print('Invalid operator')
    