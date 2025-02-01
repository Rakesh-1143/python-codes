dic={1:"abcd",2:"efgh",3:"ijkl","a":"mnop","b":"qrst"}
print(dic[1])

#if there is a key contains any value in dictonaries,then prints the output
print(dic["a"])       #suppose if there is "a" key is not available in dictionaries, then it shows error
print(dic.get("a"))   #suppose if there is "a" key is not available in dictionaries, then it shows none

# print(dic["c"])
# print(dic.get("c"))

# print(dic.keys())

# for i in dic.keys():
#     print(i)
    

# for i in dic.keys():
#     print(dic.get(i))
    
# for i in dic.keys():
#     print(dic[i])

# for hello in dic.keys():
#     print(f"the key is {hello} the value is {dic[hello]} ")

# for key,value in dic.items():
#     print(f"the key {key} is corresponding to value {value}")