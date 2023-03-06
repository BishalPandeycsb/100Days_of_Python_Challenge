def isLeap(year):                               #leap year function
    if(year%4==0 and year%400==0):
        print("Yes, It's a leap year")
    elif(year%4==0 and year%100!=0):
        print("Yes, It's a leap year")
    else:
        print("Not a Leap Year")


x=int(input("Enter the year"))
isLeap(x)                                    #function call
