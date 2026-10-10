import numpy as np
import matplotlib.pyplot as plt

def solve_biohack_signals():
    # Pemodelan Matriks BioHack (Sensitif Jantung, Otak, Otot)
    # 8x1 + 1x2 + 2x3 = 43
    # 2x1 + 10x2 + 1x3 = 61
    # 1x1 + 2x2 + 7x3 = 35
    A = [[8, 1, 2],
         [2, 10, 1],
         [1, 2, 7]]
    B = [43, 61, 35]
    
    # Parameter Komputasi
    tolerance = 1e-5
    max_iter = 50
    n = len(B)
    
    # Array untuk menyimpan data log grafik
    err_jacobi_log = []
    err_gs_log = []
    iter_jacobi_log = []
    iter_gs_log = []
    
    print("="*55)
    print(" PENYELESAIAN MENGGUNAKAN METODE JACOBI")
    print("="*55)
    x_jac = [0.0, 0.0, 0.0] 
    for iter_count in range(1, max_iter + 1):
        x_new = [0.0, 0.0, 0.0]
        for i in range(n):
            sum_val = B[i]
            for j in range(n):
                if i != j: sum_val -= A[i][j] * x_jac[j]
            x_new[i] = sum_val / A[i][i]
        
        # Kalkulasi Error Maksimum
        error = max(abs(x_new[i] - x_jac[i]) for i in range(n))
        x_jac = x_new.copy()
        
        # Simpan Log untuk Grafik
        err_jacobi_log.append(error)
        iter_jacobi_log.append(iter_count)
        
        print(f"Iterasi {iter_count:02d} | x1: {x_jac[0]:.6f} | x2: {x_jac[1]:.6f} | x3: {x_jac[2]:.6f} | Error: {error:.6f}")
        
        if error < tolerance:
            print(f"--> Konvergen pada iterasi ke-{iter_count}\n")
            break

    print("="*55)
    print(" PENYELESAIAN MENGGUNAKAN METODE GAUSS-SEIDEL")
    print("="*55)
    x_gs = [0.0, 0.0, 0.0]
    for iter_count in range(1, max_iter + 1):
        x_old = x_gs.copy()
        for i in range(n):
            sum_val = B[i]
            for j in range(n):
                if i != j: sum_val -= A[i][j] * x_gs[j] # In-place updating
            x_gs[i] = sum_val / A[i][i]
        
        # Kalkulasi Error Maksimum
        error = max(abs(x_gs[i] - x_old[i]) for i in range(n))
        
        # Simpan Log untuk Grafik
        err_gs_log.append(error)
        iter_gs_log.append(iter_count)
        
        print(f"Iterasi {iter_count:02d} | x1: {x_gs[0]:.6f} | x2: {x_gs[1]:.6f} | x3: {x_gs[2]:.6f} | Error: {error:.6f}")
        
        if error < tolerance:
            print(f"--> Konvergen pada iterasi ke-{iter_count}\n")
            break
            
    print("="*55)
    print(" HASIL AKHIR (INTENSITAS SINYAL MURNI)")
    print("="*55)
    print(f"Sinyal Jantung (x1) : {x_gs[0]:.4f} mV")
    print(f"Sinyal Otak (x2)    : {x_gs[1]:.4f} mV")
    print(f"Sinyal Otot (x3)    : {x_gs[2]:.4f} mV\n")

    # =================================================================
    # BAGIAN VISUALISASI GRAFIK
    # =================================================================
    print("Membuat grafik konvergensi... (Silakan cek jendela baru atau file gambar)")
    plt.figure(figsize=(10, 6))
    
    # Plot skala logaritmik (semilogy) untuk membandingkan peluruhan error
    plt.semilogy(iter_jacobi_log, err_jacobi_log, 'bo-', linewidth=2, label=f'Metode Jacobi ({len(iter_jacobi_log)} iterasi)')
    plt.semilogy(iter_gs_log, err_gs_log, 'ro-', linewidth=2, label=f'Metode Gauss-Seidel ({len(iter_gs_log)} iterasi)')
    
    # Formatisasi Tampilan Grafik
    plt.title('Grafik Perbandingan Konvergensi Error\nMetode Jacobi vs Gauss-Seidel', fontsize=14, fontweight='bold')
    plt.xlabel('Jumlah Iterasi', fontsize=12)
    plt.ylabel('Error Relatif Maksimum (Skala Logaritmik)', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=12)
    
    # Menyimpan dan menampilkan plot
    plt.savefig('grafik_konvergensi_biohack.png', dpi=300, bbox_inches='tight')
    plt.show()

# Menjalankan program utama
if __name__ == "__main__":
    solve_biohack_signals()
