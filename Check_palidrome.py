# check Entered number is palidrome or not

org=int(input("Enter the number:"))
check=org

new=0

while(org>0):
    r=org%10
    new=new*10+r
    org=int(org/10)

if(new==check):
    print ("Entered number is Palidrome.")
else:
    print ("Entered number is not Palidrome.")