num =int(input("Enter the two digit:"))
a = num %10
b= num //10
if((a+b==7) or (a==7 or b==7) or(num%7==0)):
    print("Special  number is satisfied")
else:
    print("Normal number is satisfied")
