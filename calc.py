num1=int(input("enter first num:"))
num2=int(input("enter second num:"))
print("choose operations")
print("1) Addition:")
print("2) subtraction:")
print("3) multiplication:")
print("4) division:")
print("5) remainder:")
opt=input("enter operation :")
if opt=='1':
    print("addition:",num1+num2)
elif opt=='2':
    print("subtraction:",num1-num2)
elif opt=='3':
    print("multiplication :",num1*num2)
elif opt=='4':
    print("division:",num1/num2)
elif opt=='5':
    print("remainder:",num1%num2)
else:
    print("invalid operation")
