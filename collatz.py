"""Veryfying the Collatz conjecture."""

#Wojciech Pogorzelski G00375250
#20-02-2021

def f(n):
    #if n is even
    if n % 2 ==0:
        return n//2 #double forwardslash indicates integer division
    elif n % 2==1:
        return (3*n) +1
    else:
        return None


def collatz(n):

    so_far =[]

    while n!=1:
        if n in so_far:
            return False
        so_far.append(n) #append to the list
        #print(n)
        n = f(n)
    so_far.append(n)
    return so_far

#print(collatz(10))
print(collatz(27))


