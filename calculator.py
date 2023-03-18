number1 = float(input("Input the number:"))
operator = input("Input operator(+,-,*,/):")
number2 = float(input("Input the number:"))

if operator == "+":
    result = (number1+number2)
elif operator == "-":
    result = (number1-number2)
elif operator == "*":
    result = (number1*number2)
elif operator == "/":
    result = (number1/number2)
else:
    print("Invalid operator")

print("Answer is:",result)


