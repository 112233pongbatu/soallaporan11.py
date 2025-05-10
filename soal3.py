import re

def tampilkan_kata_unik(namafile):
    try:
        with open(namafile, 'r', encoding='utf-8') as f:
            teks = f.read().lower()
        
        kata = re.findall(r'\b\w+\b', teks)
        unik = sorted(set(kata))
        print("Kata-kata unik:")
        print('\n'.join(unik))
    except FileNotFoundError:
        print(f"File '{namafile}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


tampilkan_kata_unik(input("Masukkan nama file teks: "))
