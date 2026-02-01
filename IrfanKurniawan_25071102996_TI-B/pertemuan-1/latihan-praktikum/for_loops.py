#cetak setiap buah di dalam daftar buah
buah = ['apel', 'pisang', 'ceri']
for x in buah:
    print(x)
    
#perulangan pada sebuah string
for x in "semangka":
    print(x)
    
#menghentikan perulangan sebelum selesai mengeksekusi semua item
buah = ['apel', 'pisang', 'ceri']
for x in buah:
    print(x)   
    if x == 'pisang':
        break
    
#menghentikan iterasi loop saat ini dan melanjutkan ke iterasi berukutnya
buah = ['apel', 'pisang', 'ceri']
for x in buah:
    if x == 'pisang':
        continue
    print(x)
    
#mengggunakan range untuk menjalankan serangkaian kode dalam jumlah yang ditentukan
for x in range(10):
    print(x)
    
#range dengan menggukan parameter
for x in range(1,5):
    print(x)
    
#dengan tiga parameter yang digunakan sebagai nilai penambahan
for x in range(1,10,2):
    print(x)
    
#if else didalam for loop
for x in range(6):
    print(x)
else:
    print('selesai')  #mencetak kata selesai ketika perulangan telah berakhir

#else tidak akan dieksekusi jika perulangan dihentikan oleh break    
for x in range(6):
    if x == 3: break
    print(x)
else:
    print('selesai')
    
#perulagan bersarang
adj = ['merah', 'besar', 'manis']
buah = ['apel', 'pisang', 'mangga']

for x in adj:
    for y in buah:
        print(x,y)  #"loop dalam" akan dieksekusi satu kali setiap iterasi dari "loop luar"
        
#tambahkan kata pass jika ingin mengosongkan isi for
for x in [0,1,2]:
    pass