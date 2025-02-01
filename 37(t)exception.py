# a=10
# b=2

# try:
#     print(a/b)
# except Exception:
#     print("unable to print")


# a=10
# b=2

# try:
#     print(a/b)
# except Exception:
#     print("unable to print")
# finally:
#     print("finally printed")





# a=10
# b=0

# try:
#     print(a/b)
# except Exception:
#     print("unable to print")
    
    
# a=10
# b=0

# try:
#     print("resource open")
#     print(a/b)
#     print("resource closed")
# except Exception:
#     print("unable to print")


# a=10
# b=2

# try:
#     print("resource open")
#     print(a/b)
#     print("resource closed")
# except Exception:
#     print("unable to print")


# a=10
# b=0

# try:
#     print("resource open")
#     print(a/b)
    
# except Exception:
#     print("unable to print")
#     print("resource closed")


# a=10
# b=0

# try:
#     print("resource open")
#     print(a/b)
#     print("resource closed")
# except Exception as e:
#     print("unable to print",e)         #it prints as unable to print and also prints alongwith the "division by zero"


# a=10
# b=2

# try:
#     print("resource open")
#     print(a/b)
#     print("resource closed")
#     k=int(input("enter value:"))
#     print(k)
# except Exception as e:
#     print("unable to print",e)
    
# except ValueError as e:
#     print("value error",e)
    
# except ZeroDivisionError as e:
#     print("unable to divide with zero",e)



# a=10
# b=0

# try:
#     print("resource open")
#     print(a/b)
#     print("resource closed")
#     k=int(input("enter value:"))
#     print(k)
# except ValueError as e:
#     print("value error",e)    
# except ZeroDivisionError as e:
#     print("unable to divide with zero",e)
# except Exception as e:
#     print("unable to print",e)       #here both zerodivisionerror and exception are works as same 


# a=10
# b=12
 
# k=int(input("enter a value:"))
# print(k)
# try:
#     print(a/b)
# except Exception as e:
#     print("enter a number",e)
# finally:
#     print("all executed")        #if we enter any character(such as k) then it shows ValueError:invalid literal for int() with base 10: 'k'



# a=10
# b=12
 
# k=int(input("enter a value:"))
# print(k)
# try:
#     print(a/b)
# except ValueError as e:
#     print("it is value error")
# except Exception as e:
#     print("enter a number",e)
# finally:
#     print("all executed")                 # same as above it shows value error


a=10
b=12
 
try:
    print(a/b)
    k=int(input("enter a value:"))
    print(k)
except ValueError as e:
    print("it is value error")
except Exception as e:
    print("enter a number",e)
finally:
    print("all executed") 
    
