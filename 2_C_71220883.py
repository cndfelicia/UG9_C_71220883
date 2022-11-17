Kecepatan = int(input("Masukkan kecepatan tempuh:"))
Waktu = int(input("Masukkan waktu yang diperlukan:"))
#rumus
bensin = Kecepatan*Waktu//10
biaya = bensin*15000
print("Teman Anda mengisi bensin sebanyak", bensin, "liter")
print("Biaya yang dikeluarkan untuk mengisi bensin adalah Rp.", biaya)
