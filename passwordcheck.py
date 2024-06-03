i = input("enter your password ")

if i.isdecimal() == True:
    print("add letter")

elif i.isalpha() == True:
    print("add number")

elif i.isspace() == True:
    print("add letter and number")

elif i.isalnum() == True:
    print("welcome")

else:
    print("wrong you need to either add a letter or a number ")