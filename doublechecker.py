num=int(input("enter a number"))
if num>=100:
    print("the number is greater than 100")
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
else:
    print("number is less than 100")