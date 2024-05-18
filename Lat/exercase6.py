list_barang = {}

def sum():
    nama = input('Masukkan Nama Barang: ')
    if nama in list_barang:
        list_barang[nama] += 1
        print(f'Barang {nama} telah ditambahkan')
        return
    
    stok = int(input('Masukkan Jumlah Barang: '))
    list_barang[nama] = stok
    print(f'Barang {nama} telah ditambahkan\n{list_barang}')

def search():
    lihat = input('Cari Barang: ')
    if lihat in list_barang:
        print(f'Barang {lihat} tersedia {list_barang[lihat]} pcs')
    else:
        print(f'Barang {lihat} tidak tersedia')

def delete():
    hapus = input('Hapus Barang: ')
    if hapus in list_barang:
        del list_barang[hapus]
        print(f'Barang {hapus} telah dihapus')
    else:
        print(f'Barang {hapus} tidak tersedia')

def edit():
    nama = input('Masukkan barang yang ingin diubah: ')
    if nama not in list_barang:
        print(f'Barang {nama} tidak tersedia')
        return
    
    print(f"List Barang Saat Ini '{nama}':")
    print(f"\tJumlah: {list_barang[nama][0]}")

    pilihan = input('Pilihan Ubah\n1. Jumlah\n2. Batal')
    if pilihan == 1:
        jumlah = int(input('Masukkan Jumlah: '))
        list_barang[nama][0] = jumlah
        print(f'Jumlah {nama} telah diubah')
    elif pilihan == 2:
        exit

def view_data():
    print(list_barang)
    
def view_item_cout():
    if not list_barang:
        print('Tidak ada data')
        return
    print(f"List Barang Saat Ini:")
    for nama,data in list_barang.items():
        kuantitas = data
        print(f'{nama}: ')
        print(f'\tJumlah: {kuantitas}')

sum()
view_item_cout()