import numpy as np

def iter_policy_evaluation(V_0,R,PI,P,gamma,iters):
    for _ in range(iters):
        V_i=PI@np.tensordot(P,R+gamma*V_0,axes=1)
        V_0=V_i
    return V_i

def iter_policy_evaluation_conv(V_i,R,PI,P,gamma,iters,delta):
    for _ in range(iters):
        V_0=V_i
        V_i=PI@np.tensordot(P,R+gamma*V_0,axes=1)
        if np.max(np.abs(V_i-V_0))<delta:
            break
    return V_i  

def policy_improvement(V_0,R,PI,P,gamma,iters):
    for _ in range(iters):
        Q_i=np.tensordot(P,R+gamma*V_0,axes=1)
        V_i=PI@Q_i
        V_0=V_i
    return V_i,Q_i

def value_iteration(R,P,gamma,iters,delta):
    V_i=np.zeros(P.shape[1])
    for _ in range(iters):
        V_0=V_i
        V_i=np.max(np.tensordot(P,R+gamma*V_0,axes=1), axis=0)
        if np.max(np.abs(V_0-V_i))<delta:
            break
    return np.argmax(np.tensordot(P,R+gamma*V_i,axes=1), axis=0) 

def iter_policy_evaluation_low(V_0,R,PI,P_low,gamma,iters):
    for _ in range(iters):
        V_i=PI@np.where(P_low == -1, 0, (R+gamma*V_0)[P_low])
        V_0=V_i
    return V_i

def iter_policy_evaluation_lowconv(V_i,R,PI,P_low,gamma,iters,delta):
    for _ in range(iters):
        V_0=V_i
        V_i=PI@np.where(P_low == -1, 0, (R+gamma*V_0)[P_low])
        if np.max(np.abs(V_i-V_0))<(delta*(1-gamma)/gamma):
            break
    return V_i  

if __name__ == '__main__':
    ...