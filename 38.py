a=int(input("enter a value in between 10 and 20:\n"))
if (a<10 or a>20):
    raise ValueError("number must be in between 10 and 20")