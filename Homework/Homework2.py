print(20*"=", "Program Boarding Pass", 20*"=")
nama = str(input("Nama : "))
kode = str(input("Kode Booking : "))
NIK = int(input("NIK : "))
Nomor_Kursi = str(input("Nomor Kursi : "))
Tanggal = str(input("Tanggal Pemberangkatan : "))
Waktu =  input("Jam Keberangkatan : ")

data_tiket = ["AMT39R"]
data_nama = ["UDIN"]
data_NIK = [33281234567]
data_nokursi = ["4A"]

data = "Diperbolehkan Masuk" if kode in data_tiket and nama in data_nama and  NIK in data_NIK and Nomor_Kursi in data_nokursi else "Tidak Sesuai"
print(data)