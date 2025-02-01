#pickling Example program
#Acept emp details and save them in file
import pickle
noe=int(input("enter how many employees data u want"))

if noe<=0:
    print("{} invalid number of employees ".format(noe))
else:
    with open("empe.txt","wb")as fp:
        for i in range(1,noe+1):
            print("enter {} employee details".format(i))
            eno=int(input("enter employee number"))
            ename=input("enter the name of employee")
            sal=float(input("enter employee Salary"))
            lst=list()
            lst.append(eno)
            lst.append(ename)
            lst.append(sal)
            pickle.dump(lst,fp)
            print("{} Employee record saved successfully in file".format(i))

with open("empe.txt","rb") as fp:
    try:
        while True:
            obj=pickle.load(fp)
            for i in obj:
                print(chr(i))
    except Exception:
        print("error")



