questions=[["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 4],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 3],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 2],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 1],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 4],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 3],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 2],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 1],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 4],["national game ?" ,"cricket", "kabaddi", "chess", "hockey", 3]]

levels = [1000,2000,4000,10000,20000,50000,100000,500000,2500000,10000000]
for i in range(0, len(questions)):
    question=questions[i]
    print(f"question for {levels[i]}")
    print(f"{question[0]}")
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")
    reply=int(input("enter your answer  1-4:"))
    if (reply == question[-1]):
        print(f"correct answer, you have won Rs. {levels[i]}")
        if(i==0):
         money=0
        elif(i==2):
         money = 1000
        elif(i==5):
         money =10000
        elif(i==8):
         money=100000
    else:
        print("wrong answer")
        break
    
print(f"take home money {money}")