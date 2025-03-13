st=input("Enter the string : ")
for i in st:
    if i==" ":
        st=st.replace(" ","*")

st=st+'$'
print(st)