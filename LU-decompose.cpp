#include <iostream>
#include <vector>
#include <iomanip> // For pretty printing

using namespace std;

typedef vector<vector<double>> Matrix;

void printMatrix(const string& name, const Matrix& M) {
    cout << name << ":" << endl;
    for (const auto& row : M) {
        for (double val : row) {
            cout << setw(10) << fixed << setprecision(2) << val << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void luDecomposition(const Matrix& A, Matrix& L, Matrix& U) {
    int n = A.size();

    // 1. Initialize L as Identity and U as a copy of A
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) L[i][j] = 1.0;   // Diagonal of L is 1s
            else L[i][j] = 0.0;
            
            U[i][j] = A[i][j];           // Copy A into U to start
        }
    }

    // 2. Perform Gaussian Elimination
    for (int i = 0; i < n; i++) {
        // Safety check for your zero-pivot concern!
        if (abs(U[i][i]) < 1e-9) {
            cerr << "Error: Zero pivot encountered at index " << i << ". Swapping needed!" << endl;
            return;
        }

        for (int j = i + 1; j < n; j++) {
            // Calculate the multiplier (factor)
            double factor = U[j][i] / U[i][i];

            // Store the multiplier in L (the "recording" step)
            L[j][i] = factor;

            // Update the rest of the row in U
            for (int k = i; k < n; k++) {
                U[j][k] -= factor * U[i][k];
            }
        }
    }
}

int main() {
    // Test Matrix from your board: [1 4 7; 2 5 8; 3 6 10]
    Matrix A = {
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 10}
    };

    int n = A.size();
    Matrix L(n, vector<double>(n));
    Matrix U(n, vector<double>(n));

    luDecomposition(A, L, U);

    printMatrix("Matrix A (Original)", A);
    printMatrix("Matrix L (Lower)", L);
    printMatrix("Matrix U (Upper)", U);

    return 0;
}