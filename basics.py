# Wojciech Pogorzelski G00375250
#Python Basics
#2021-02-18

#print("Hello World!")

a = 1
b = 1.5

s = "String"
t='String in the single quote'

#print(a,b,s,t)
#print(t[3:10:2]) #String slice, works like a for loop, starts from character at index 2 and displays every second one

#--list in python
x = [1,2,3, "Hello",1.0]

#print(x)
#print(x[0])
#print(x[2])
#print(x[-1])


# for i in x[::2]: #give me every second element of the list
#     print(i)
#     print(i+i)


# for i in range(10):
#     print(i)

#--dictionaries in python

d={"no_wheels": 4, "make": "VW" }
d["model"] = "Golf"

#print(d["model"])

r = [1,2,3,4]

print(r)

s = [i*i for i in r]

print(s)

#################################################################

def factorial(n):

    #Number to calculate factorial of

    if n < 1:
        m = -n
    else:
        m=n

    #The running total
    total = 1

    #Loop to do the multiplications

    while m>1:
        total = total * m 
        m =m-1

    if n <1:
        return -total
    else:
        return total


#Test function
n=-20

#Calculate factorial on n

print(f"The factorial of {n} is {factorial(n)}")


