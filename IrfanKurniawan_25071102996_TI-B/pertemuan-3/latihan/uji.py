import myOOp as mo

a1 = mo.Produkelektronik('tv', 3000000, 2)
a2 = mo.ProdukMakanan('roti', 15000, '12-12-2026')

print(a1.info_produk())
print(a2.info_produk())

pesan1 = mo.Email()
pesan2 = mo.SMS()

print(pesan1.kirim())
print(pesan2.kirim())

m1 = mo.Mahasiswa(50)
print(m1.get_nilai())

m1.set_nilai(87)
print(m1.get_nilai())