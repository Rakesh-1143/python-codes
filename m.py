try:
 k=[12,218,281,581,76,83]
 i=int(input("enter the index:"))
 print(k[i])
except:
 print("some error occurred")
finally:
 print("i am always executed")