A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Buatlah program python (tanpa NumPy) yang:
# a. Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
def tambah_matrix(A, B):
    baris, kolom = len(A), len(A[0])
    c_tambah = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return c_tambah

# b. Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
def kurang_matrix(A, B):
    baris, kolom = len(A), len(A[0])
    c_kurang = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return c_kurang

# c. Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
def kali_skalar(matriks, k):
    hasil = []
    for baris in A:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

# d. Menampilkan ketiga hasil dengan format rapi baris per baris
print("soal a")
c_tambah = tambah_matrix(A, B)
for baris in c_tambah:
    print(baris)
print('')

print('soal b')
c_kurang = kurang_matrix(A, B)
for baris in c_kurang:
    print(baris)
print('')

print('soal c')
c_skalar = kali_skalar(A, 4)
for baris in c_skalar:
    print(baris)