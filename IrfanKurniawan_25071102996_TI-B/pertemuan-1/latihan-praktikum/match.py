day = 4
match day:               #match dievaluasi sekali 
    case 1:
        print('senin')   #nilai ekspresi dibandingkan dengan nilai masing-masing case
    case 2:
        print('selasa')  #jika ditemukan kecocokan, blok kode yang terkait akan dieksekusi
    case 3:
        print('rabu')
    case 4:
        print('kamis')
    case 5:
        print('jumat')
    case 6:
        print('sabtu')
    case 7:
        print('minggu')
        
#gunakan karakter garis bawah sebagai nilai default
day = 4
match day:
    case 6:
        print('sabtu')
    case 7:
        print('minggu')
    case _:
        print('tidak ada hari yang cocok') #karena tidak ada yang cocok, maka in iyang akan dicetak
        
#menggabungkan nilai dengan menggunakan karakter '|'
day = 4
match day:
    case 1|2|3|4|5:
        print('today is a weekday')
    case 6|7:
        print('i love weekends!')
        
#menambahkan if dalam evaluasi kasus sebagai pengecekan kondisi tambahan
month = 5 
day = 4
match day:
    case 1|2|3|4|5 if month == 4:
        print('A weekday in April')
    case 1|2|3|4|5 if month == 5:
        print('A weekday in May')
    case _:
        print('No match')