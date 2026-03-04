import numpy as np

def build_environment():
    n = 4
    N = n * n
    gamma = 0.99
    r = -1

    P = []
    R = []

    for a in ["up", "down", "left", "right"]:
        P_a = np.zeros((N, N))
        R_a = np.full((N, N), r)

        for s in range(N):
            row, col = divmod(s, n)

            if a == "up":
                next_row, next_col = max(row - 1, 0), col
            elif a == "down":
                next_row, next_col = min(row + 1, n - 1), col
            elif a == "left":
                next_row, next_col = row, max(col - 1, 0)
            elif a == "right":
                next_row, next_col = row, min(col + 1, n - 1)

            s_next = next_row * n + next_col
            P_a[s, s_next] = 1.0

        for t in [0, 15]:
            P_a[t, :] = 0
            P_a[t, t] = 1.0
            R_a[t, :] = 0

        P.append(P_a)
        R.append(R_a)
    
    return P,R