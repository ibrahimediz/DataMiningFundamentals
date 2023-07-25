dosya = open("ornekdata/data2.csv","r+",encoding="UTF-8")
liste = dosya.readlines()
print(*liste[0].split(";"),sep="\n")
basliklar = liste[0].split(";")
datalar = dict.fromkeys(basliklar,[])
for item in liste[1:]:
    kayitlar = item.split(";")
    for anahtar,kayit in zip(datalar.keys(),kayitlar):
        _liste = datalar[anahtar].copy()
        _liste.append(kayit)
        datalar[anahtar] = _liste

datalar = dict.fromkeys(basliklar,[])
sozluk = {}
for item in datalar["barkod_no"]:
    
    sozluk[item] = {}
