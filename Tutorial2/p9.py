str=input("Enter the string : ")

num=len(str)
middle=num//2
for i in range(middle-1,-1,-1):
    print(str[i], end="")
for i in range(num-1,middle-1,-1):
    print(str[i], end="")