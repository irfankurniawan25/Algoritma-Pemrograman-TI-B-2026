class Mobile_legend:
    def __init__(self, nama, role, lane):
        self.nama = nama
        self.role = role
        self.lane = lane
        
    def farming(self):
        return 'Mendapatkan buff'
        
    def kill(self):
        return 'Savage'
        
    def hitung_KDA(self):
        try:
            kill = int(input('\njumlah kill = '))
            death = int(input('jumlah death = '))
            assist = int(input('jumlah assist = '))
            
            if death == 0:
                KDA = kill + assist
            else:
                KDA = (kill + assist) / death
                
            if KDA <= 3.0:
                print(f'Bronze {3.0}')
            elif KDA > 3.0 and KDA < 4.5:
                print(f'Bronze {KDA:.1f}')
            elif KDA >= 4.5 and KDA < 7.5:
                print(f'Silver {KDA:.1f}')
            elif KDA >= 7.5 and KDA < 10.0:
                print(f'Gold {KDA:.1f}')
            elif KDA >= 10.0:
                print(f'MVP {KDA:.1f}')
            
        except ValueError:
            print('\nError: Harap masukkan angka!')
        except ZeroDivisionError:
            print('\nError: Tidak bisa dibagi dengan 0')
        else:
            print('\nKode berjalan dengan baik!')
        finally:
            print('Program selesai!')
        
hero1 = Mobile_legend('layla', 'marksmane', 'gold lane')

print(hero1.farming())
print(hero1.kill())
hero1.hitung_KDA()