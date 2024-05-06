print('program menghitung gaji')
nama, jabatan, status = input("Masukkan Nama, Jabatan [Design, Programmer, Resource], dan Status Perkawinan [Y/T]: ").split(',')
gajipokok = 5000000 if jabatan == "Design" or  jabatan == "Resource" else 10000000
tunjangan = gajipokok * 0.2 if status == 'Y' or status == 'y' else 0
print(f'Nama: {nama}', f'\nJabatan: {jabatan}', f'\nGaji Pokok: {gajipokok:,.2f}', f'\nTunjangan: {tunjangan:,.2f}','\nGaji Kotor:', "{:,.2f}".format(gajipokok + tunjangan),'\nPajak:', '{:,.2f}'.format(gajipokok * 0.1),'\nTotal Pendapatan:', '{:,.2f}'.format(gajipokok - (gajipokok * 0.1)))