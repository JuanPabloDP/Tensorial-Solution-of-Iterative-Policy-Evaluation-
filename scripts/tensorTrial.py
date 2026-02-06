
import numpy as np

num_states=15 #number of states 
reward=-1 #reward on all transitions
prob_action=1/4 #probability of taking any action
gamma=1 #gamma is a parameter called the discount rate 
num_actions=4 #numer of possible actions

V_0=np.zeros(num_states) #initial aproximation 
R=np.full(num_states,reward) #reward vector
PI=np.full(num_actions,prob_action) #probabilities vector

P_up=np.zeros((num_states,num_states)) #up transition matrix
P_down=np.zeros((num_states,num_states)) #down transition matrix
P_right=np.zeros((num_states,num_states)) #right transition matrix
P_left=np.zeros((num_states,num_states)) #left transition matrix

d=4 #gridworld length
for i in range(num_states):
    if i<d:
        P_up[i,i]=1

    if i>=d*(d-1):
        P_down[i,i]=1

    for j in range(num_states):
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

P=np.array([P_up,P_down,P_right,P_left]) #transition matrices tensor

RV=R+V_0

RVP=np.tensordot(P,RV,axes=1)

V_1=PI @ RVP 

V_2=PI @ np.tensordot(P,R+V_1,axes=1)

iters=1000
for i in range(iters):
    V_i=PI @ np.tensordot(P,R+V_0,axes=1)
    V_0=V_i


for i in range(iters):
    Q_i=np.tensordot(P,R+gamma*V_0,axes=1)
    V_i=PI @ Q_i
    V_0=V_i
