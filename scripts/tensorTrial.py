
import numpy as np

N=15
m=4
d=4

r=-1
pi=1/4

V_0=np.zeros(N)

R=np.full(N,r)

PI=np.full(m,pi)

P_up=np.zeros((N,N))
P_down=np.zeros((N,N))
P_right=np.zeros((N,N))
P_left=np.zeros((N,N))

for i in range(N):
    if i<d:
        P_up[i,i]=1

    if i>=d*(d-1):
        P_down[i,i]=1

    for j in range(N):
        if i-j==d:
            P_up[i,j]=1

        if j-i==d:
            P_down[i,j]=1

        if (i+1)%d==0:
            P_right[i,i]=1
        elif j-i==1:
            P_right[i,j]=1
    
        if i%d==0:
            P_left[i,i]=1
        elif i-j==1:
            P_left[i,j]=1

P_down[11,0]=1
P_right[14,0]=1

P_up[0,0]=0
P_down[0,4]=0
P_right[0,1]=0
P_left[0,0]=0

P=np.array([P_up,P_down,P_right,P_left])

RV=R+V_0

RVP=np.tensordot(P,RV,axes=1)

V_1=PI @ RVP

V_2=PI @ np.tensordot(P,R+V_1,axes=1)

iters=1000

for i in range(iters):
    V_1=PI @ np.tensordot(P,R+V_0,axes=1)
    V_0=V_1
