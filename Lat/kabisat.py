tahun = int(input('Masukkan Tahun:'))
print(tahun,'Adalah Tahun Kabisat') if tahun % 4 == 0 or tahun % 100 == 0 or tahun % 400 == 0 else print(tahun,'Bukan Tahun Kabisat')