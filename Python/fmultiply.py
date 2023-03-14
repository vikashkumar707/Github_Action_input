import sys

def multiply(num1,num2):
    return num1*num2

num1=int(sys.argv[1])
num2=int(sys.argv[2])

c=print(f'The multiply of {num1} and {num2} is:',multiply(num1,num2))
