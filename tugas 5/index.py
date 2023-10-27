nama = ["B 3730 ENZ", "BEAT", "120 cc", "Putih"]

nama.append("15 juta")
nama.append("Roda 2")

nama.insert(2,"Honda")
nama.insert(3,"Sepeda motor")

print(nama)

#match case
itung = input("1 untuk persegi, 2 untuk lingkaran, 3 untuk segitiga")
match itung:
    case 1 | "1"| "persegi":
        s = int(input("masukan panjang sisi"))
        luas = s*s
        print(luas)
    case 2 | "2"| "lingkaran":
        r = int(input("masukan panjang jari-jari"))
        luas = 3,14 * r * r
        print(luas)
    case 3 | "3" | "lingkaran":
        a = int(input("masukan panjang alas"))
        t = int(input("masukan tinggi"))
        luas = 0.5 * a * t 
        print(luas)
    case _ :
        print("anda salah memilih")