t=(1,2,3,4,12,56,9,4,90,43,21,49,"abc","kesava",'hello')
print(type(t),t)
print(len(t))
print(t[14])
print(t[-1])
r=t.count(2)
print(r)
print(t.index(56))


hello =(12,13,14,"one","two","three")
hi=list(hello)
hi.append("kesava")
hello=tuple(hi)
print(hello)


hello =(12,13,14,"one","two","three")
hi=list(hello)
hi.pop(1)
hello=tuple(hi)
print(hello)


list=[1,2,3,4]
list.pop(1)
list1=tuple(list)
print(list1)
print(type(list))
print(type(list1))

list3=[2,3,4,5,6,7]
list3[3]=51
list2=tuple(list3)

print(list2)


a=("apple","ball","cat")
b=("dog","egg","fan")
list4= a+b
print(list4)

tuple2=(11,1,12,3,43,2,42,343,1,231,2,2,3,1,3)
print(len(tuple2))
print(tuple2.index(2))
print(tuple2.index(2,9,14))
print(tuple2.index(2,11,14))



my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[2:5])  
print(my_tuple[:4])  
print(my_tuple[5:])  
print(my_tuple[::2]) 
print(my_tuple[::-1])  
print(my_tuple[8:2:-1])  





