# 1. without pivot
import numpy as np

def manual_lu(A):
    n = A.shape[0]
    # Initialize L as Identity and U as a copy of A
    L = np.eye(n)
    U = A.copy().astype(float)

    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the multiplier (the 'k' in your notes)
            factor = U[j, i] / U[i, i]
            
            # Record the multiplier in L
            L[j, i] = factor
            
            # Perform Row Operation: Rj = Rj - factor * Ri
            U[j, i:] -= factor * U[i, i:]
            
    return L, U

# Test it
A = np.array([[1, 4, 7], 
              [2, 5, 8], 
              [3, 6, 10]])

L, U = manual_lu(A)
print("L:\n", L)
print("U:\n", U)

#2 . Partial pivot
from scipy.linalg import lu

A = np.array([[0, 0, 3], 
              [3, 5, 8], 
              [9, 15, 10]])

# P is the Permutation matrix, L is Lower, U is Upper
P, L, U = lu(A)

print("Permutation Matrix (P):\n", P)
print("Lower Triangular (L):\n", L)
print("Upper Triangular (U):\n", U)