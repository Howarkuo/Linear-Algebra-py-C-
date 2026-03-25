from sympy import Matrix

def solve_augmented_lights_out():
    # 1. Define the Augmented Matrix [A | x] directly
    # The last column is the target state (Case 1 / last column : 1,0,1,0,1 )
    M = Matrix([
        [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1]
    ])

    print("Original Augmented Matrix [A|x]:")
    print(M)

    # 2. Compute RREF using modulo 2 logic
    # iszerofunc tells SymPy to treat any even number as 'zero' during elimination
    rref_matrix, pivot_cols = M.rref(iszerofunc=lambda x: x % 2 == 0)

    # 3. Clean up the result with mod 2
    # This handles any -1 or 2 that might appear during standard elimination
    final_rref = rref_matrix.applyfunc(lambda x: x % 2)

    print("\nReduced Row Echelon Form (RREF) mod 2:")
    print(final_rref)
    
    print(f"\nPivot Columns: {pivot_cols}")
    print(f"Rank of A: {len(pivot_cols)}")

solve_augmented_lights_out()

# PS C:\Users\howar\Desktop\Linear-Algebra> poetry run python .\light-out.py    
# Original Augmented Matrix [A|x]:
# Matrix([[1, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1]])

# Reduced Row Echelon Form (RREF) mod 2:
# Matrix([[1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

# Pivot Columns: (0, 1, 2, 3)
# Rank of A: 4

# final column: 0, 1,1,1,0 
# Which means to press button {2,3,4} for Case 1 / last column : 1,0,1,0,1