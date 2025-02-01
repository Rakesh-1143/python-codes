#atmmain
from banking import *
import sys
from atmmenu import atmmenu
while True:
    atmmenu()
    try:
        ch=int(input("enter your choice"))

        match ch:
            case 1:
                deposit()
            case 2:
                withdraw()
            case 3:
                balenq()
            case 4:
                print("\n Thanks for using this ATM application")
                sys.exit()
            case _:
                print("your selection is wrong")
    except ValueError:
        print("\n Don't enter symblos alpha numerics")
