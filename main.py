nama = 'Silva Damayanti'
program = 'gerak lurus'

print(f'Program {program} oleh {nama}')

#TUGAS: buat fungsi _APA_SAJA_YANG_KALIAN_TAHU
#DAN_GUNAKAN


def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

#jarak = 1000
#waktu = 5* 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan (3000, 70 * 60)



def hitung_gaya(massa, percepatan):
    gaya = massa * percepatan
    print(f'massa = {massa * 50}kg ditempuh dengan percepatan = {percepatan * 10}m/s')
    print(f'sehingga gaya = {gaya} N')
    return gaya

#massa = 50
#percepatan = 10
gaya = hitung_gaya(50, 10)
gaya = hitung_gaya (50, 10)
