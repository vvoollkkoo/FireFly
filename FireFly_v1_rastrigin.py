import numpy as np
import random
import math
print("Введите количество светлячков")
N=input()
N=int(N)
t=100 #количество итераций
k=0
p=30 #количество прогонов
sumX=0
sumY=0
ALFA=1
BETTA=[0]*N
best=-10
X=np.array([random.uniform(-5.12,5.12) for i in range(N)])
Y=np.array([random.uniform(-5.12,5.12) for i in range(N)])
for l in range(p):
    for j in range(t):
        for i in range(N):
            BETTA[i]=1/(20+X[i]**2+Y[i]**2-10*math.cos(2*math.pi*X[i])-10*math.cos(2*math.pi*Y[i]))
            if BETTA[i]>best: 
                best=BETTA[i]
                bestX=X[i]
                bestY=Y[i]
                k=i
              #двигаем всех к лучшему  
            if X[i]!=bestX:
                X[i]=bestX+BETTA[i]*(X[i]-bestX)+random.uniform(-1,1)*ALFA
            if Y[i]!=bestY:
                Y[i]=bestY+BETTA[i]*(Y[i]-bestY)+random.uniform(-1,1)*ALFA
          #двигаем лучшего      
        X[k]=bestX+random.uniform(-1,1)*ALFA
        Y[k]=bestY+random.uniform(-1,1)*ALFA
        ALFA=1+ALFA/math.e
    
sumX=bestX+sumX
sumY=sumY+bestY
print(sumX/p, sumY/p, 'fitness_func= ', 20+sumX/p**2+sumY/p**2-10*math.cos(2*math.pi*sumX/p)-10*math.cos(2*math.pi*sumY/p))
