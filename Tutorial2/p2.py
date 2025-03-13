str= input("Enter the name of string : ")
result=[]
for i in range(len(str)):
    if i % 2 == 0:
        result.append(str[i])
print("".join(result))