#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

// --- Mathematical Abstraction: The Field Z2 ---
struct Z2 {
    int val;
    Z2(int v = 0) : val(v % 2) {}
    Z2 operator+(const Z2& other) const { return Z2(val ^ other.val); }
    Z2 operator*(const Z2& other) const { return Z2(val & other.val); }
    bool isZero() const { return val == 0; }
};

typedef vector<vector<Z2>> MatrixZ2;

class LightsOutSolver {
public:
    static void solveAugmented(MatrixZ2 A, vector<Z2> b) {
        int rows = A.size();
        int cols = A[0].size();

        // 1. Construct Augmented Matrix [A | b] (5 rows x 6 columns)
        for (int i = 0; i < rows; ++i) A[i].push_back(b[i]);

        cout << "--- Solving Augmented Matrix [A | b] ---" << endl;

        // 2. Gauss-Jordan Elimination to RREF
        int pivot = 0;
        for (int j = 0; j < cols && pivot < rows; ++j) {
            int sel = pivot;
            while (sel < rows && A[sel][j].isZero()) sel++;
            if (sel == rows) continue; 

            swap(A[pivot], A[sel]);

            for (int i = 0; i < rows; ++i) {
                if (i != pivot && !A[i][j].isZero()) {
                    for (int k = j; k <= cols; ++k) {
                        A[i][k] = A[i][k] + A[pivot][k];
                    }
                }
            }
            pivot++;
        }

        // 3. Print RREF
        for (const auto& row : A) {
            for (int j = 0; j < row.size(); ++j) {
                cout << row[j].val << (j == cols - 1 ? " | " : " ");
            }
            cout << endl;
        }

        // 4. Check Consistency (Row Space / Column Space Logic)
        bool consistent = true;
        vector<int> solution;
        for (int i = 0; i < rows; ++i) {
            bool allZerosLeft = true;
            for (int j = 0; j < cols; ++j) if (!A[i][j].isZero()) allZerosLeft = false;
            if (allZerosLeft && !A[i][cols].isZero()) consistent = false;
        }

        if (!consistent) {
            cout << "\nRESULT: INCONSISTENT. Target vector is NOT in C(A).\n" << endl;
        } else {
            cout << "\nRESULT: CONSISTENT. Solution found in Augmented Column.\n" << endl;
        }
    }
};

int main() {
    MatrixZ2 A = {{1,1,0,0,0},{1,1,1,0,0},{0,1,1,1,0},{0,0,1,1,1},{0,0,0,1,1}};
    vector<Z2> x1 = {1, 0, 1, 0, 1}; // Case 1
    vector<Z2> x2 = {1, 0, 0, 0, 0}; // Case 2

    cout << "CASE 1 (Target: 1,0,1,0,1)" << endl;
    LightsOutSolver::solveAugmented(A, x1);

    cout << "CASE 2 (Target: 1,0,0,0,0)" << endl;
    LightsOutSolver::solveAugmented(A, x2);
    return 0;
}