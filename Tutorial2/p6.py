str= input("Enter the string")
substr= input("Enter the substring ")

if substr in str:
    str = str.replace(substr, "")
    print(str)