import exercase6 as ex6

print(f'{5*"="}Selamat Datang Di Program Manajemen Barang{5*"="}')
print("Masukkan Pilihan\n1.Tambah Barang\n2.Cari Barang\n3.Hapus Barang\n4.Edit Barang\n5.Tampilkan Data Barang\n6.Tampilkan Jumlah Data\n7.Keluar")

while True:
    pilihan = int('Masukkan Pilihan: ')
    if pilihan == 1:
        ex6.sum()
        break
    elif pilihan == 2:
        ex6.search()
    elif pilihan == 3:
        ex6.delete()
    elif pilihan == 4:
        ex6.edit()
    elif pilihan == 5:
        ex6.view_data()
    elif pilihan == 6:
        ex6.view_item_cout()
    elif pilihan == 7:
        print("Terima Kasih Telah Menggunakan Program Kami")
        break