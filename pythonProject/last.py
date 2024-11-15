import matplotlib.pyplot as plt
import numpy as np

def GaussianElimination(A,B):
    n=np.size(B)
    a = np.zeros((n,n+1))
    for i in range(n):
        for j in range(n):
            a[i][j]=A[i][j]
        a[i][n]=B[i]
    for i in range(0,n-1,1):
        temp=i
        for xx in range(i+1,n,1):
            if(abs(a[xx,i])>abs(a[temp,i])):
                temp=xx
        a[[temp,i]]=a[[i,temp]]
        j=n-1
        while(j!=i):
            if(a[i][i]==0):
                print("Divide by 0")
                return None
            rat=a[j][i]/a[i][i]
            for k in range(0,n+1,1):
                temp=rat*a[i][k]
                a[j][k]=a[j][k]-temp
            j=j-1
    ans=np.zeros(n)
    for i in range(n-1,-1,-1):
        j=n-1
        ans[i]=a[i][n]
        while(j>i):
            ans[i]=ans[i]-(ans[j]*a[i][j])
            j=j-1
        if(a[i][i]==0):
            print("Divide by 0")
            return None
        ans[i]=ans[i]/a[i][i]
    return ans

#start
xList = [00,10,20,30,40,50,60,70,80,90,100]
yList = [10.3,13.5,13.9,14.2,11.6,10.3,9.7,9.6,14.1,19.8,31.1]
sumX=0.0
sumX2=0.0
sumX3=0.0
sumX4=0.0
sumX5=0.0
sumX6=0.0
sumY=0.0
sumXY=0.0
sumX2Y=0.0
sumX3Y=0.0

n=np.size(xList)
for i in range(n):
    sumX=sumX+xList[i]
    sumY=sumY+yList[i]
    sumXY=sumXY+(xList[i]*yList[i])
    sumX2=sumX2+(xList[i]**2)
    sumX3=sumX3+(xList[i]**3)
    sumX4=sumX4+(xList[i]**4)
    sumX5=sumX5+(xList[i]**5)
    sumX6=sumX6+(xList[i]**6)
    sumX2Y=sumX2Y+((xList[i]**2)*yList[i])
    sumX3Y=sumX3Y+((xList[i]**3)*yList[i])

mat=[[n,sumX,sumX2,sumX3],
    [sumX,sumX2,sumX3,sumX4],
    [sumX2,sumX3,sumX4,sumX5],
    [sumX3,sumX4,sumX5,sumX6]]
c=[sumY,sumXY,sumX2Y,sumX3Y]
a=GaussianElimination(mat,c)

#plotting
y=[]
for i in xList:
    y.append(a[0]+a[1]*i+a[2]*i**2+a[3]*i**3)


#prediction
pred=(a[0]+a[1]*110+a[2]*110**2+a[3]*110**3)
print(pred)


plt.plot(xList,y)
plt.plot(xList,yList, marker = '.')
plt.grid()
plt.show()