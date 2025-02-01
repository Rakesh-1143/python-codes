# x=10
# def function():
#     y=2
#     print(y)
    
# print(x)      #here x=10 because x is global variable
# function()
# print(y)   #here it gives error, there is no global variable 


# x=2
# y=3
# def f1():
#     x=4
#     y=5
#     print(int(x)+int(y))
    
# print(x)          #here x value is 2 
# print(y)          #here y value is 3
# f1()


# x=6
# y=7
# print(x)
# def f2():
#     global x 
#     x=8
#     print(x)
    
  
# print(x)   # here also x value is 6 because f2 function is not called then there is no update in value of x

# f2()
# print(x)   #here x value is updated because f2 function is called




# x=20
# def f3():
#     print("global variable", x)
    
# f3()    #here there is no x value in function, but x value is global 



# a=10
# def f4():
#     a=20
#     x=globals()['a']
#     print("inside",a)
#     print(id(x))
#     globals()['a']=25
    

# print(id(a))
# print(a)
# f4()
# print(a)
# print(id(a))



# b= 20
# def f5():
#     b=25
#     print(b)
#     print(id(b))
#     globals()['b']=30
#     print(b)
#     print(id(b))
    
# print(b)
# print(id(b))    
# f5()
# print(b)
# print(id(b))    


# b= 20
# def f5():
#     b=25
#     print(b)
#     print(id(b))
#     x=globals()['b']
#     print(x)
#     print("inside",x)
#     print(id(x))
#     globals()['b']=30
#     print(b)
#     print(id(b))
    
# print(b)
# print(id(b))    
# f5()
# print(b)
# print(id(b)) 

b= 20
def f5():
    b=20
    print(b)
    print(id(b))
    x=globals()['b']
    print(x)
    print("inside",x)
    print(id(x))
    globals()['b']=20
    print(b)
    print(id(b))
    
print(b)
print(id(b))    
f5()
print(b)
print(id(b)) 