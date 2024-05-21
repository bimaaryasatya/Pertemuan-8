import numpy as np
import main as mn

arr = np.array([])
siswa = int(input('Masukkan Jumlah Siswa: '))

for i in range(siswa):
    nilai = int(input(f'Masukkan Nilai Siswa Ke-{i+1}: '))
    arr = np.append(arr, nilai)

print('Nilai Rata-Rata Seluruh Siswa: ',mn.avrg(arr),'\nNilai Tertinggi: ',mn.maxi(arr),'\nNilai Terendah: ',mn.mins(arr),'\nJumlah Nilai Di Atas Rata-Rata: ',mn.ab_avg(arr))
