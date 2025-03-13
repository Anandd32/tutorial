str= input("Enter the string")
sub= input("Enter the substring ")
sub2= input("Enter the new substring ")

if sub in str:
    str = str.replace(sub,sub2)
    print(str)