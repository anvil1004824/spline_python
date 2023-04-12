import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi

def spline(x,y):
    C=[0]
    B=[(y[1]-y[0])/(x[1]-x[0])-C[0]*(x[1]-x[0])]
    for i in range(len(x)-2):
        C.append(((y[i+2]-y[i+1])/(x[i+2]-x[i+1])-(y[i+1]-y[i])/(x[i+1]-x[i])-(x[i+1]-x[i])*C[i])/(x[i+2]-x[i+1]))
        B.append((y[i+2]-y[i+1])/(x[i+2]-x[i+1])-(x[i+2]-x[i+1])*C[i+1])
    nx=[]
    ny=[]
    for i in range(len(x)-1):
        newx=np.arange(x[i],x[i+1],0.1)
        newy=[]
        for j in newx:
            newy.append((j-x[i])**2*C[i]+(j-x[i])*B[i]+y[i])
        nx.extend(newx)
        ny.extend(newy)

    nx.append(x[-1])
    ny.append(y[-1])
    return [nx,ny]

x=[1,2,3,4,5,6,7,8]
y=[2,5,10,1,1,12,20,2]
x0=spline(x,y)[0]
y0=spline(x,y)[1]
ipo=spi.splrep(x,y,k=3)
x1=np.linspace(x[0],x[-1],70)
y1=spi.splev(x1,ipo)

plt.plot(x,y,color='black',marker='.')
plt.plot(x,y,'g')
plt.plot(x0,y0,'b')
plt.plot(x1,y1,'r')
plt.show()

