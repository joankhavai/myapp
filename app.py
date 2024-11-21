num1 = input("Enter first number :")
op = input("Enter operator :")
num2 = input("Enter second number :")

n1 = int(num1)
n2 = int(num2)

if op == "+":
    ans = n1+n2
    print(ans)
    
elif op == "-":
    ans = n1-n2
    print(ans)

elif op == "x":
    ans = n1*n2
    print(ans)


elif op == "/":
    ans = n1/n2
    print(ans)

else:
    print("Enter valid values")