print("WELCOME TO CALCULATOR PROGRAM")
print()
print("ENTER THE CORRECT INPUT\n1=add\n2=sub\n3=mul\n4=div\n")

def operation(c,d):
    operator = input("Enter the operation name:")
    
    if (operator == "add"):
        print("ADDITION OPERATION:",a+b)

    elif (operator == "sub"):
        print("SUBTRATION OPERATION:",a-b)

    elif (operator == "mul"):
        print("MULTIPLICATION OPERATION:",a*b)

    elif (operator == "div"):
        print("DIVISION OPERATION:",a/b)
    else:
        print("INVALID OPERATOR")
          

a=int(input("Enter the value of a:"))
print()

b=int(input("Enter the value of b:"))
print()

operation(a,b)


