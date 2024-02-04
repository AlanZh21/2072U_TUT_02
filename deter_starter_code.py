# Recursive computation of the determinant starter code. Tutorial 3 of MATH/CSCI2072 CSI, Ontario Tech U, 2024.
import numpy as np
import math

def deter(A):
# Recursive computation of the determinant. Input: n X n array A. Out: determinant of A (float).
    n = np.shape(A)[0]                                              # Extract number of rows.
    if n==2:                                            # For 2x2 matrix, use definition.
        # First catch the exceptional case n=2.
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
        
    else:                                               # For larger matrices, compute recursively.
        detA = 0.0                                         # Initialize the determinant.
        for i in range(0,n):                            # Cofactor expansion.
            B = np.delete(A, i, axis = 0)                                     # Delete i-th row.
            B = np.delete(B, 0, axis = 1)                                    # Delete first column.
            detA += (-1)**(i) * deter(B)                                  # Recursive call.
    return detA

