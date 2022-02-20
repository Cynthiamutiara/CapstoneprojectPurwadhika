listBarang= [
    {
        'kodebarang': 2219,
        'namabarang': 'baju',
        'kuantitas' : '1',
        'warna': 'hitam',
        'model': 'kaos' 
    },
    {
        'kodebarang': 2218,
        'namabarang': 'celana',
        'kuantitas': '2',
        'warna': 'biru',
        'model': 'pendek' 
    }
]

def readBarang():
    read = True
    while read != '3':
        print('''
        =================
        Data Stok Barang
        =================

        1. Seluruh Stok Barang
        2. Stok Barang tertentu
        3. Menu Utama''')
        read = input('Pilih menu [1-3]: ')
        if read == '1':
            if len(listBarang) != 0:
                print('Data Stok Barang\n')
                print('kodebarang\t| namabarang  \t| kuantitas\t\t| warna\t\t\t\t| model')
                for i in range(len(listBarang)) :
                    print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listBarang[i]['kodebarang'],listBarang[i]['namabarang'],listBarang[i]['kuantitas'],listBarang[i]['warna'],listBarang[i]['model']))
            else:
                print('Barang tidak tersedia')
        elif read == '2':
            if len(listBarang) != 0:
                inputKode = int(input('Masukan Kode Barang: '))
                print('Stok barang dengan kode {}'.format(inputKode))
                for i in range(len(listBarang)):
                    if inputKode == listBarang[i]["kodebarang"]:
                        print('kodebarang\t| namabarang  \t| kuantitas\t\t| warna\t\t\t\t| model')
                        print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listBarang[i]['kodebarang'],listBarang[i]['namabarang'],listBarang[i]['kuantitas'],listBarang[i]['warna'],listBarang[i]['model']))
                        break
                else:
                    print('Barang tidak tersedia')
def tambahBarang():
    tambah = True
    while tambah != '2':
        print('''
        ========================
        Menambahkan Stok Barang
        ========================
        
        1. Tambah Stok Barang
        2. Menu Utama''')
        tambah = input('Masukan [1-2]: ')
        if tambah == '1':
            inputKode3 = int(input('Masukan kode barang: '))
            allPrimeKey = [listBarang[i]["kodebarang"] for i in range(len(listBarang))]
            if inputKode3 in allPrimeKey:
                print('Barang sudah ada')
            else:
                newnamabarang = input('Masukan Nama Barang: ')
                while (True):
                    newkuantitas = input('Masukan Kuantitas Barang: ')
                    if newkuantitas.isnumeric():
                        break
                newwarna = input('Masukan Warna Barang: ')
                newmodel = input('Masukan Model Barang: ')
                
                while True: 
                    konfirmTambah = input('Simpan Data? (Y/N) ')
                    if konfirmTambah == 'Y' or konfirmTambah == 'N':
                        break 
                if konfirmTambah == 'Y':
                    listBarang.append({
                    'kodebarang': inputKode3,
                    'namabarang': newnamabarang,
                    'kuantitas': newkuantitas,
                    'warna': newwarna,
                    'model': newmodel
                })
                    print('Barang Tersimpan')
                elif konfirmTambah == 'N':
                    print('Barang Tidak Ditambahkan')

def ubahBarang():
    ubah = True
    while ubah != '2':
        print('''
        =====================
        Mengubah Stok Barang
        =====================
        
        1. Ubah Stok Barang
        2. Menu Utama''')
        ubah = input('Masukan [1-2]: ')
        if ubah == '1':
            inputKode4 = int(input('Masukan Kode Barang: '))
            allPrimeKey = [listBarang[i]["kodebarang"] for i in range(len(listBarang))]
            if inputKode4 in allPrimeKey:
                i = allPrimeKey.index(inputKode4)
                print('kodebarang\t| namabarang  \t| kuantitas\t\t| warna\t\t\t\t| model')
                print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listBarang[i]['kodebarang'],listBarang[i]['namabarang'],listBarang[i]['kuantitas'],listBarang[i]['warna'],listBarang[i]['model']))
                
                while (True):
                    konfirmUbah = input('Y untuk mengubah data, N untuk membatalkan: ')
                    if konfirmUbah == 'Y' or konfirmUbah == 'N':
                        break
                if konfirmUbah == 'Y':
                    while True : 
                        kolomUbah = input('Masukan data ingin diubah: ')
                        if kolomUbah == 'namabarang' or kolomUbah == 'kuantitas' or kolomUbah == 'warna' or kolomUbah == 'model':
                            hasilUbah = input('Masukan {} baru: '. format(kolomUbah))
                            while(True):
                                konfirmUbah2 = input('Ubah data? (Y/N): ')
                                if konfirmUbah2 == 'Y' or konfirmUbah2 == 'N':
                                    break
                            if konfirmUbah2 == 'Y':
                                listBarang[i][kolomUbah] = hasilUbah
                                print('Data sudah diubah')
                                break
                            elif konfirmUbah2 == 'N':
                                print('Data tidak diubah')
                                break
                elif konfirmUbah == 'N':
                    print('Data tidak diubah')
            else:
                print('Kontak tidak ada')


def hapusBarang():
    hapus = True
    while hapus != '2':
        print('''
        ======================
        Menghapus Stok Barang
        ======================
        
        1. Hapus Stok Barang
        2. Menu Utama''')
        hapus = input('Masukan [1-2]: ')
        if hapus == '1':
            print('Data Stok Barang\n')
            print('kodebarang\t| namabarang  \t| kuantitas\t\t| warna\t\t\t\t| model')
            for i in range(len(listBarang)) :
                print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listBarang[i]['kodebarang'],listBarang[i]['namabarang'],listBarang[i]['kuantitas'],listBarang[i]['warna'],listBarang[i]['model']))
            inputKode2 = int(input('Masukan Kode Barang: '))
            
            primarykey = [listBarang[i]['kodebarang'] for i in range(len(listBarang))]
            if inputKode2 in primarykey:
                while(True):
                    konfirmDel = input('Apakah barang akan dihapus? (Y/N): ')
                    if konfirmDel == 'Y' or konfirmDel == 'N':
                        break

                if konfirmDel == 'Y':
                    for i in range(len(listBarang)):
                        if listBarang[i]['kodebarang'] == inputKode2:
                            del listBarang[i]
                            print('Barang telah terhapus')
                            break
                    else:
                        print('Barang Tidak Tersedia')
                elif konfirmDel == 'N':
                    print('Barang Tidak Terhapus')
            else:
                print('Kode Barang Tidak Tersedia')
while True: 
    pilihanMenu = input('''
    =====================================
    Data Stok Barang

    List Menu
    1. Data Stok Barang
    2. Menambahkan Stok Barang
    3. Mengubah Stok Barang
    4. Menghapus Stok Barang
    5. Keluar

    Silahkan Pilih Main Menu [1-5]: ''')
    
    if(pilihanMenu == '1') :
        readBarang()
    elif(pilihanMenu == '2') :
        tambahBarang()
    elif(pilihanMenu == '3') :
        ubahBarang()
    elif(pilihanMenu == '4') :
        hapusBarang()
    elif(pilihanMenu == '5') :
        print('Terimakasih!')
        break
    else:
        print('Tidak tersedia')