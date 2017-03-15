#Call Collatz until value is 1
#pg 77 ATBSWP
import Collatz

def CallCollatz(CurrentNumber):
    while CurrentNumber != 1:
        CurrentNumber=Collatz.Collatz(CurrentNumber)
        print(CurrentNumber)
        
