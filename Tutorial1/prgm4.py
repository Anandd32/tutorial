def Compare(num1,num2):
    if num1>num2:
        print(f"{num1} is the largest")
        print(f"{num2} is the smallest")
    elif num1==num2:
        print(f"{num1} & {num2} are equal")
    else:
        print(f"{num2} is the largest")
        print(f"{num1} is the smallest")

num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
Compare(num1,num2)