# Bagian Library

import math 

# Bagian Variabel yang konstant

PHI = math.pi 

# Bagian Validator Input

def angka_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Terjadi kesalahan!!, semuanya tau itu")
            
def mode_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka! Coba lagi.")     

# Bagian Fungsi Modular

def hitung_luas_lingkaran():
    print("Ini adalah program untuk menghitung Luas pada Lingkaran")
    
    jari_jari = angka_input("Masukan Jari jari: ")
    
    luas_lingkaran = PHI * jari_jari * jari_jari
    print(f"Luas lingkaran adalah: {luas_lingkaran}")
    
    luas_lingkaran_bulat = round(luas_lingkaran)
    print(f"Luas Lingkaran setelah dibulatkan adalah: {luas_lingkaran_bulat}")
    
def hitung_keliling_lingkaran():
    print("Ini adalah program untuk mengitung Keliling pada Lingkaran")
    
    jari_jari = angka_input("Masukan Jari jari: ")
    
    keliling_lingkaran = 2 * PHI * jari_jari
    print(f"Keliling Lingkaran adalah: {keliling_lingkaran}")
    
    keliling_lingkaran_bulat = round(keliling_lingkaran)
    print(f"Keliling Lingkaran setelah dibulatkan adalah: {keliling_lingkaran_bulat}")

def hitung_panjang_busur():
    print("Ini adalah program untuk menghitung Busur pada Lingkaran")

    sudut_pusat = angka_input("Masukan sudut pusat: ")
    jari_jari = angka_input("Masukan jari jari: ")
        
    print()

    panjang_busur = sudut_pusat / 360 * 2 * PHI * jari_jari
    print(f"Panjang busur adalah: {panjang_busur}")
        
    panjang_busur_bulat = round(panjang_busur)
    print(f"Panjang busur setelah dibulatkan adalah: {panjang_busur_bulat}")

def hitung_luas_juring():
    print("Ini adalah program untuk menghitung luas juring pada lingkaran")
    sudut_pusat = angka_input("Masukan sudut pusat: ")
    jari_jari = angka_input("Masukan jari jari: ")
    
    print()
    
    luas_juring = sudut_pusat / 360 * PHI * jari_jari * jari_jari
    print(f"Luas juring adalah: {luas_juring}")
    
    luas_juring_bulat = round(luas_juring)
    print(f"Panjang busur setelah dibulatkan adalah: {luas_juring_bulat}")
    
# Bagian Pemilihan Mode
    
def pemilihan_mode():
    print("Mau ngapain?")
    print("1. Hitung Luas Lingkaran\n2. Hitung Keliling Lingkaran \n3. Hitung Panjang Busur\n4. Hitung Luas Juring")
    mode_modean = angka_input("Pilih mau kemana: ")
    
    if mode_modean == 1:
        hitung_luas_lingkaran()
    elif mode_modean == 2:
        hitung_keliling_lingkaran()
    elif mode_modean == 3:
        hitung_panjang_busur()
    elif mode_modean == 4:
        hitung_luas_juring()
    else:
        print("Terjadi kesalahan!, semuanya tau itu [ERROR MODE]")

# Bagian Start

def main():
    pemilihan_mode()

if __name__ == "__main__":
    main()

