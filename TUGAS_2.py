# ==========================================
# TUGAS METODE NUMERIK - BIOHACK SIGNAL
# METODE JACOBI & GAUSS-SEIDEL
# ==========================================

def solve_biohack_signals():
    # Matriks Koefisien (Diagonally Dominant)
    # 8x1 + 1x2 + 2x3 = 43
    # 2x1 + 10x2 + 1x3 = 61
    # 1x1 + 2x2 + 7x3 = 35
    
    A = [[8, 1, 2],
         [2, 10, 1],
         [1, 2, 7]]
    B = [43, 61, 35]
    
    # Parameter
    tolerance = 1e-5
    max_iter = 50
    n = len(B)
    
    print("="*50)
    print(" PENYELESAIAN MENGGUNAKAN METODE JACOBI")
    print("="*50)
    x_jac = [0.0, 0.0, 0.0] # Nilai awal
    for iter_count in range(1, max_iter + 1):
        x_new = [0.0, 0.0, 0.0]
        for i in range(n):
            sum_val = B[i]
            for j in range(n):
                if i != j:
                    sum_val -= A[i][j] * x_jac[j]
            x_new[i] = sum_val / A[i][i]
        
        # Hitung Error
        error = max(abs(x_new[i] - x_jac[i]) for i in range(n))
        x_jac = x_new.copy()
        print(f"Iterasi {iter_count:02d} | x1: {x_jac[0]:.6f} | x2: {x_jac[1]:.6f} | x3: {x_jac[2]:.6f} | Error: {error:.6f}")
        
        if error < tolerance:
            print(f"--> Konvergen pada iterasi ke-{iter_count}\n")
            break

    print("="*50)
    print(" PENYELESAIAN MENGGUNAKAN METODE GAUSS-SEIDEL")
    print("="*50)
    x_gs = [0.0, 0.0, 0.0] # Nilai awal
    for iter_count in range(1, max_iter + 1):
        x_old = x_gs.copy()
        for i in range(n):
            sum_val = B[i]
            for j in range(n):
                if i != j:
                    sum_val -= A[i][j] * x_gs[j] # Langsung menggunakan nilai terbaru
            x_gs[i] = sum_val / A[i][i]
        
        # Hitung Error
        error = max(abs(x_gs[i] - x_old[i]) for i in range(n))
        print(f"Iterasi {iter_count:02d} | x1: {x_gs[0]:.6f} | x2: {x_gs[1]:.6f} | x3: {x_gs[2]:.6f} | Error: {error:.6f}")
        
        if error < tolerance:
            print(f"--> Konvergen pada iterasi ke-{iter_count}\n")
            break
            
    print("="*50)
    print(" HASIL AKHIR (INTENSITAS SINYAL MURNI)")
    print("="*50)
    print(f"Sinyal Jantung (x1) : {x_gs[0]:.4f} mV")
    print(f"Sinyal Otak (x2)    : {x_gs[1]:.4f} mV")
    print(f"Sinyal Otot (x3)    : {x_gs[2]:.4f} mV")

# Menjalankan program
solve_biohack_signals()
