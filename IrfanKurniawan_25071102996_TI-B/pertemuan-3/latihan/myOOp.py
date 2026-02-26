class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga
        
    def info_produk(self):
        return self.nama_produk, self.harga
    
class Produkelektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi
        
    def info_produk(self):
        return f'{self.nama_produk} seharga {self.harga} dengan garansi {self.garansi}'
        
class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, kadaluarsa):
        super().__init__(nama_produk, harga)
        self.kadaluarsa = kadaluarsa
        
    def info_produk(self):
        return f'{self.nama_produk} seharga {self.harga} kadaluarsa {self.kadaluarsa}'
        
'''
==================================================
B. POLYMORPHISM
==================================================
'''
class Notifikasi:   
    def kirim(self):
        return 'pesan'
    
class Email(Notifikasi):
    def kirim(self):
        return 'Mengirim notifikasi melalui SMS'
        
class SMS(Notifikasi):
    def kirim(self):
        return 'Mengirim notifikasi melalui Email'
        

'''
==================================================
C. ENCAPSULATION
==================================================
'''
class Mahasiswa:
    def __init__(self, nilai):
        self.__nilai = nilai
        
    def get_nilai(self):
        return self.__nilai
        
    def set_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            print('Nilai tidak valid!')    
        else:
            self.__nilai = nilai