import numpy as np

def iter_policy_evaluation(V_0,R,PI,P,gamma,iters):
    for i in range(iters):
        V_i=PI@np.tensordot(P,R+gamma*V_0,axes=1)
        V_0=V_i
    return V_i

def policy_improvement(V_0,R,PI,P,gamma,iters):
    for i in range(iters):
        Q_i=np.tensordot(P,R+gamma*V_0,axes=1)
        V_i=PI@Q_i
        V_0=V_i
    return V_i,Q_i

if __name__ == '__main__':
    ...