str=input("Enter the passsword ")
hasupper=False
haslower=False
hasdigit=False
hasspecial=False
specialChar="$@#"

if(len(str)>=6):
    for i in str:
        if i.islower():
            haslower=True
        elif i.isupper():
              hasupper=True
        elif i.isdigit():
              hasdigit=True
        elif i in specialChar:
            hasspecial=True

    if hasupper and haslower and hasdigit and hasspecial:
         print(" Pasword is vlaid")
    else:
         print("Invalid password")

else:
    print("invalid password")                        
