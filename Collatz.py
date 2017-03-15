#! python3
#Collatz sequence, pg 77 ATBSWP

def Collatz(number):
    if number % 2 == 0:
        valu=number//2
        #print(valu)
    else:
        valu=number * 3 + 1
        #print(valu)
    return valu
