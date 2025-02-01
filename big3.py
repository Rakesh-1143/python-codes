a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))

big=a
if a==b and b==c:
    print("equal")
else:
    big=a
    if (b>big):
        big=b
    if (c>big):
        big=c
    print("biggest values of {} {} {} is {}".format(a,b,c,big))
