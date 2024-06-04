history = []
stack = []
def undo():
    rec = history[-1]
    if rec[0] == "+":
        history.pop()
        stack.pop()
        print(f'Berhasil mengundo menambahkan "{rec[1:]}"')
    elif rec[0] == "-":
        history.pop()
        stack.append(rec[1:])
        print(f'Berhasil mengundo menghapus "{rec[1:]}"')

while True:
    print(f"Riwayat pencarian saat ini : {stack} \nHistori: {history}","\nPilihan:","\n1. Tambah Pencarian","\n2. Hapus pencarian terakhir","\n3. Undo","\n4. Keluar\n")
    inp = str(input("Pilih Operasi (1/2/3/4): "))
    if inp == "1":
        kk = input("Masukkan kata kunci pencarian: ")
        stack.append(kk)
        history.append(f"+{kk}")
        print(f'"{kk}" ditambahkan ke riwayat pencarian')
    elif inp == "2":
        print(f'"{stack[-1]}" berhasil di hapus')
        stack.pop()
        history.append(f"-{kk}")
    elif inp == "3":
        undo()
    elif inp == "4":
        break
    else:
        print("Pilihan Tidak Valid")
    print("\n")