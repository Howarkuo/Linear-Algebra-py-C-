import tkinter as tk
from tkinter import messagebox
from sympy import Matrix

class LightsOutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lights Out: Augmented Matrix Solver")
        
        # State: 0 = OFF, 1 = ON
        self.state = [0, 0, 0, 0, 0]
        self.buttons = []
        
        # Matrix A (Toggle Adjacency)
        self.A = Matrix([
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1]
        ])

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Toggle lights, then solve using RREF mod 2", font=('Arial', 10)).pack(pady=5)
        
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=10)
        
        for i in range(5):
            btn = tk.Button(self.btn_frame, text="OFF", width=8, height=3, 
                            bg="gray", command=lambda i=i: self.toggle(i))
            btn.grid(row=0, column=i, padx=5)
            self.buttons.append(btn)

        tk.Button(self.root, text="Solve Augmented System", command=self.solve_system, 
                  bg="#2ecc71", fg="white", font=('Arial', 10, 'bold')).pack(pady=10)
        
        tk.Button(self.root, text="Reset Board", command=self.reset).pack(pady=5)

    def toggle(self, i):
        for idx in [i-1, i, i+1]:
            if 0 <= idx < 5:
                self.state[idx] = 1 - self.state[idx]
                color = "yellow" if self.state[idx] == 1 else "gray"
                self.buttons[idx].config(bg=color, text="ON" if self.state[idx] == 1 else "OFF")

    def solve_system(self):
        # 1. Create Augmented Matrix [A | state]
        b = Matrix(self.state)
        augmented = self.A.row_join(b)
        
        print("\n--- Current Augmented Matrix [A|b] ---")
        print(augmented)

        # 2. Compute RREF mod 2
        rref_mat, pivots = augmented.rref(iszerofunc=lambda x: x % 2 == 0)
        rref_mat = rref_mat.applyfunc(lambda x: x % 2)
        
        print("--- RREF mod 2 ---")
        print(rref_mat)

        # 3. Check for contradiction [0 0 0 0 0 | 1]
        is_solvable = True
        for r in range(rref_mat.rows):
            if all(rref_mat[r, c] == 0 for c in range(5)) and rref_mat[r, 5] == 1:
                is_solvable = False
                break

        if not is_solvable:
            messagebox.showerror("Linear Algebra Error", "Inconsistent System!\nTarget state is NOT in C(A).")
        else:
            # Extract solution (last column of pivot rows)
            # For simplicity, we assume free variables = 0
            u = rref_mat.col(5)
            press_indices = [i+1 for i in range(5) if u[i] == 1]
            
            msg = f"Consistent System!\n\nRank: {len(pivots)}\n"
            msg += f"Press Switches: {press_indices if press_indices else 'None'}"
            messagebox.showinfo("Solution Found", msg)

    def reset(self):
        self.state = [0]*5
        for btn in self.buttons: btn.config(bg="gray", text="OFF")

if __name__ == "__main__":
    root = tk.Tk()
    app = LightsOutApp(root)
    root.mainloop()