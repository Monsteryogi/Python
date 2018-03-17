# palidrome of number

org=int(input("Enter the number:"))

new=0

while(org>0):
    r=org%10
    new=new*10+r
    org=int(org/10)

print (new)