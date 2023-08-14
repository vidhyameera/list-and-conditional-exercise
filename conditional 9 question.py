num= int(input("Enter the N:"))
s=num*num
print(s)
a = num %10
b= s%10
if(a==b):
    print("its a square root")
else:
    print("its not a square root")
