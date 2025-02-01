a={1,2,3,4}
b={3,4,5,6}
c={8,9,0,11,10}
d={1,2,3,4,5,6,7,8,9}
# #union
# z= a.union(b)
# print(z)
 
# # here union of a and b becomes a
# a.update(b)
# print(a)

# print(a.intersection(b))

# a.intersection_update(b)
# print(a)

# print(a.difference(b))
# a.difference_update(b)
# print(a)

# y=a.symmetric_difference(b)
# print(y)               #it is opposite intersection of two sets. it removes the common elements and prints remainin elements

# x=a.symmetric_difference_update(b)
# print(x)              #here set a is updated, so no need to allocate a variable to this

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))

# print(a.issubset(d))
# print(b.issubset(d))
# print(d.issuperset(b))
# print(d.issuperset(b))


# a.add(6)
# print(a)
# a.add("hello")
# print(a)

# a.remove(1)
# print(a)
# a.remove("hello")
# print(a)

# a.discard(1)
# print(a)

# the main difference between remove and discard is , if we try to delete an item which is not presented in set, then remove raises an error but discard does not raise any error

# k=a.pop()      
# print(a)      #to get result after an item is popped
# print(k)      #to get result which item is popped

# t=c.pop()      
# print(c)      # in an unordered list we didn't expect the popping item (random element is popped)
# print(t)    

# del a
# print(a)       #delete an entire set completely

# del(a)
# print(a)

# a.clear()
# print(a)                # here all items deleted and prints only set






