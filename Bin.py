import os

def options():
    showops = input("op1: Normal op2: Repair")

    if showops == "op1":
        os.system("python3 Op1.py")

    elif showops == "op1":
        os.system("python3 Op2.py")

    else:
        print("Oops! Try Again")
    

options()
