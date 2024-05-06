total = 0
while True:
    nilai = int(input('Masukkan Nilai Masing-Masing Siswa: ')) 
    jawab = input('Lanjutkan?: ')
    total += nilai
    if jawab == 'tidak':
        break
rata = total / nilai
print(f'Rata-rata nilai semua siswa adalah:{rata}')