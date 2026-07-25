a=float(input("Enter first number = "))
b=float(input("Enter second number = "))
c=input("Choose operator like (+,-,*,/) = ")
if c=="+":
    print("Sum=",a+b)
elif c=="-":
    print("Difference =",a-b)
elif c=="*":
    print("Product =",a*b);
elif c=="/":
    if b!=0:
        print("Result =",a/b)
    else:
        print("ERROR!!! Division with zero isnot possible")
else:
    print("Invalid operator")