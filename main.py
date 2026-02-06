
import numpy as np

from scripts.defineProblem import build_vectors
from scripts.tensorial_solution import iter_policy_evaluation

def main() -> None:
    gamma=1 
    iterations=1000

    V_0,R,PI,P=build_vectors()

    V_i=iter_policy_evaluation(V_0,R,PI,P,gamma,iterations)

    print(V_i)

if __name__ == '__main__':
    main()