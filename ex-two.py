num1 = input("type a number: ")
num2 = input ("type another number: ")

num1 = int(num1)
num2 = int(num2)

result = num1 / num2
result = int(result + 0.5)
# int eliminates the decimals
print(result)