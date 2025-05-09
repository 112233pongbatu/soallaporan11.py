def tiga_bilangan_terbesar(data):
    hasil = []
    for x in data:
        if len(hasil) < 3:
            hasil.append(x)
        elif x > min(hasil):
            hasil[hasil.index(min(hasil))] = x
    return sorted(hasil, reverse=True)

bilangan = [30, 45, 4, 92,27, 17]
print(tiga_bilangan_terbesar(bilangan))  
