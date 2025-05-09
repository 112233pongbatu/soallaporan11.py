def hitung_nilai_rata2():
    total, count = 0, 0
    
    while (user_input := input("Masukkan bilangan (jika 'done' berarti selesai): ")) != "done":
        try:
            total += float(user_input)
            count += 1
        except ValueError:
            print("Input tidak valid.")
    
    print("Rata-ratanya:", total / count if count > 0 else "Tidak ada bilangan.")

hitung_nilai_rata2()
