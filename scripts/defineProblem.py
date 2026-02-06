import numpy as np

def define_problem():
    num_states=15 #number of states 
    num_actions=4 #numer of possible actions
    prob_action=1/num_actions #probability of taking any action
    reward=-1 #reward on all transitions
    return num_states,num_actions,prob_action,reward

def build_vectors():
    num_states,num_actions,prob_action,reward=define_problem()

    V_0=np.zeros(num_states) #initial aproximation 
    R=np.full(num_states,reward) #reward vector
    PI=np.full(num_actions,prob_action) #probabilities vector
    P=transition_tensor(num_states) #transition matrices tensor
    return V_0,R,PI,P

def transition_tensor(num_states,grid_length=4):
    P_up=np.zeros((num_states,num_states)) #up transition matrix
    P_down=np.zeros((num_states,num_states)) #down transition matrix
    P_right=np.zeros((num_states,num_states)) #right transition matrix
    P_left=np.zeros((num_states,num_states)) #left transition matrix 

    for i in range(num_states):
        if i<grid_length:
            P_up[i,i]=1
        if i>=grid_length*(grid_length-1):
            P_down[i,i]=1
        for j in range(num_states):
            if i-j==grid_length:
                P_up[i,j]=1
            if j-i==grid_length:
                P_down[i,j]=1
            if (i+1)%grid_length==0:
                P_right[i,i]=1
            elif j-i==1:
                P_right[i,j]=1
            if i%grid_length==0:
                P_left[i,i]=1
            elif i-j==1:
                P_left[i,j]=1

    #Especial corrections
    P_down[11,0]=1
    P_right[14,0]=1
    P_up[0,0]=0
    P_down[0,4]=0
    P_right[0,1]=0
    P_left[0,0]=0

    return np.array([P_up,P_down,P_right,P_left]) 

if __name__ == '__main__':
    V_0,R,PI,P=build_vectors()
    ...
    