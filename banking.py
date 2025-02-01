#Banking.py
from bankexcep import *
from WithdrawError import WithdrawError
bal=500.00
def deposit():
    damt=float(input("enter how much amt u want to deposit"))
    if damt<0:
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("your account balance credited with inr{}".format(damt))
        print("Now your current balance is {}".format(bal))
        
def withdraw():
    global bal
    wamt=float(input("enter how much amt u want to deposit"))
    if wamt<0:
        raise WithdrawError
    elif wamt+500>bal:
        print("insuffient balance")
    else:
        bal=bal-wamt
        print("your account debieted with inr{}".format(wamt))
        print("Now your current balance is {}".format(bal))

def balenq():
    print("Now your current balance is {}".format(bal))
    


    
     
