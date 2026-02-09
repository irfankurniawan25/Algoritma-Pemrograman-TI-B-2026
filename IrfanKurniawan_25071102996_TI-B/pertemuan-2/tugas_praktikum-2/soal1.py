def rata_rata(nilai):
    total = 0
    banyakBil = len(nilai)

    if nilai == []:
        return 'Data kosong'
    else:
        for x in nilai:
            total += x
            
        rata_rata = total / banyakBil
    return rata_rata

nilai = [80, 75, 90, 60, 85]
print('hasil rata-rata =',rata_rata(nilai)) #output: 78.0