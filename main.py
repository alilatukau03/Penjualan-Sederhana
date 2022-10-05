total = 0
barang = []
harga = []

while True:
    print("""Daftar Barang Yang Tersedia\n
    1. Baju \t 50000
    2. Jeans \t 40000
    3. Sweeter \t 150000
    4. Topi \t 15000
    5. Sepatu \t 250000
    6. Jaket \t 170000
    7. Kacamata \t 20000
    8. Celana \t 50000
    9. Dompet \t 35000
    10. Lekton \t 10000
    """)

    kode = int(input("Masukan Barang Yang Di Inginkan : "))
    if kode == 1:
        barang.append('baju')
        harga.append(50000)
        total += 50000
    elif kode == 2:
        barang.append('jeans')
        harga.append(40000)
        total += 40000
    elif kode == 3:
        barang.append('sweeter')
        harga.append(150000)
        total += 150000
    elif kode == 4:
        barang.append('topi')
        harga.append(15000)
        total += 15000
    elif kode == 5:
        barang.append('sepatu')
        harga.append(250000)
        total += 250000
    elif kode == 6:
        barang.append('jaket')
        harga.append(170000)
        total += 40000
    elif kode == 7:
        barang.append('kacamata')
        harga.append(20000)
        total += 20000
    elif kode == 8:
        barang.append('celana')
        harga.append(50000)
        total += 50000
    elif kode == 9:
        barang.append('dompet')
        harga.append(35000)
        total += 35000
    elif kode == 10:
        barang.append('lekton')
        harga.append(10000)
        total += 10000
    else:
        print('Barang Tidak Ada')

    lanjut = input('Lanjut Belanja? (y/t) : ')
    if lanjut == 't':
        print("")
        break

print('Barang Yang Dibeli : ', barang)
print('Harga Barang : ', harga)
print('Total Yang Harus Dibayar : ', total, '\n')

uang = int(input('Masukan Uang Pembayaran : '))
if uang > total:
    print('Kembaliannya : ', uang - total)
elif uang == total:
    print('Uang Pas')
else:
    print('Uangnya Kurang', uang - total)