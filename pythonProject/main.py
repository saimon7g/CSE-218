import matplotlib.pyplot as plt
import numpy as np
import math

def function(x):
    return -((6.73*x)+(6.725*10**(-8))+3.63*10**(-7))/((x*3.62*10**(-12))+(x*1.954*10**-11))
def RelativeError(prev , curr):
    return abs((curr-prev)/curr)*100


def Trapezoid(n,a,b):
    h=(b-a)/n
    ret= (function(a)) + function(b)
    for i in range(1,n,1):
        ret = ret + (2*(function(a+(i*h))))
    ret = ret*(h/2)
    return ret



def Simpson(n,a,b):
    h=(b-a)/n
    ret = (function(a)) + (function(b))
    for i in range(1,n,2):
        ret= ret + (4*(function(a+(i*h))))
    for i in range(2,n-1,2):
        ret=ret + (2*(function(a+(i*h))))
    ret = ret *((b-a)/(3*n))
    return ret


n=int(input())
a=1.22*10**(-4)
b=a/2
prev=1
curr=1
print('Trapezoid Method')
for i in range(1,n+1,1):
    if(i==1):
        curr=prev=Trapezoid(i,a,b)
        print(f'n={i}, Result= {curr}sec  Error: N/A')
    else:
        curr=Trapezoid(i,a,b)
        relError=RelativeError(prev,curr)

        print(f'n={i}, Result= {curr}sec  Error: {relError}%')
        prev=curr
print('Simpson Method')
for i in range(1,n+1,1):
    if(i==1):
        curr=prev=Simpson(2*i,a,b)
        print(f'n={i}, Result= {curr}sec Error: N/A')
    else:
        curr=Simpson(2*i,a,b)
        relErroe=RelativeError(prev,curr)
        print(f'n={i}, Result= {curr}sec  Error: {relError}%')
        prev=curr


x = [1.22* 1e-4 , 1.20* 1e-4 , 1.0* 1e-4 , 0.8* 1e-4 , 0.6* 1e-4 , 0.4* 1e-4 , 0.2* 1e-4 ]
y=[]
for i in x:
    y.append(Simpson(10,a,i))
plt.plot(x,y)
plt.grid()
plt.show()