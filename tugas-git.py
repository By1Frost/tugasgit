#tugasgit-at06
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

def no1():
    i=1
    for lokasi, data in data_panen.items():
        print(f"> Lokasi {i}: {data['nama_lokasi']}")
        print("Hasil Panen:")
        for panen, jumlah in data['hasil_panen'].items():
            print(f"{panen}: {jumlah}")
        print("===================")
        i = i+1

def no2():
    print(f"> Jumlah hasil panen jagung lokasi 2: {data_panen['lokasi2']['hasil_panen']['jagung']}")

def no3():
    print(f"> Nama lokasi 3: {data_panen['lokasi3']['nama_lokasi']}")

def no45():
    hasil_panen = {}

    for lokasi, data in data_panen.items():
        nama_lokasi = data['nama_lokasi']
        padi = data['hasil_panen']['padi']
        kedelai = data['hasil_panen']['kedelai']
        hasil_panen[nama_lokasi] = {'padi': padi, 'kedelai': kedelai}

    # Menampilkan hasil panen padi dan kedelai setiap lokasi
    for nama_lokasi, hasil in hasil_panen.items():
        print(f"{nama_lokasi}: Padi = {hasil['padi']}, Kedelai = {hasil['kedelai']}")

def no6():
    hasil_panen = {}

    for lokasi, data in data_panen.items():
        nama_lokasi = data['nama_lokasi']
        padi = data['hasil_panen']['padi']
        jagung = data['hasil_panen']['jagung']
        hasil_panen[nama_lokasi] = {'padi': padi, 'jagung': jagung}

    # Menampilkan hasil panen padi dan kedelai setiap lokasi
    for nama_lokasi, hasil in hasil_panen.items():
        if padi > 1300 or jagung > 800:
            print(f"> {nama_lokasi}: padi = {hasil['padi']}, jagung = {hasil['jagung']} | MEMERLUKAN PERHATIAN KHUSUS!")
        else:
            print(f"> {nama_lokasi}: padi = {hasil['padi']}, jagung = {hasil['jagung']} | KONDISI BAIK")

no1()
no2()
no3()
no45()
no6()