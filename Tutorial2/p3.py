def is_palindrome(strng):
    n=len(strng)
    left=0
    for i in range(0, int(n/2)):
       if strng[i] != strng[n-i-1]:
           return False
    return True


strng = input("Enter the string : ")
if is_palindrome(strng):
    print("string is paliendrome")
else :
    print("string is not palidrome")