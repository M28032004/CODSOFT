print("WELCOME TO LIST PROGRAM")
print()
To_Do_List=[]
List = [1,2,3,"py",5.12,"universe"]
print(List)


while True:
    print("Enter the choice\n1-create\n2-edit\n3-delete\n4-extend\n")

    choice=int(input("Enter the choice:"))

    if choice == 1:
        To_Do_List.append(5)
        To_Do_List.append(6)
        To_Do_List.append(7)
        To_Do_List.append(8)
        To_Do_List.append("python")
        To_Do_List.append(10.12)
        To_Do_List.append("Hello,World")
        print(To_Do_List)
        
    elif choice == 2:
        To_Do_List[1]=8
        print(To_Do_List)
        
    elif choice == 3:
        To_Do_List.pop(2)
        print(To_Do_List)

    else:
        To_Do_List.extend(List)
        print(To_Do_List)
    print("Do you want to repeat again?(Y/N)")

    ans =input().lower()
    if ans == 'n':
        break
print("Thank You")
