# import pandas as pd
# df = pd.read_csv("/workspace/DataMiningFundamentals/Documents/01_Libraries/Data/data2.csv",delimiter=";")
# kayitlar = []
# for barkod in df.barkod_no.unique():
#     kayit = []
#     # print(item)
#     kayit.insert(0,barkod)
#     digerSutunlar= df.columns[1:]
#     for sutun in digerSutunlar:
#         kayit.append(list(df[df["barkod_no"] == barkod][sutun]))
#     kayitlar.append(kayit)



# jsonKayitlar = []
# for i in range(dfJson.shape[0]):
#     jsonKayit = {"_id":dfJson.index[i]}
#     for item in df.columns[1:]:
#         jsonKayit[item] = dfJson.iloc[i,:][item]
#     jsonKayitlar.append(jsonKayit)

baglanti = "mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority"
import pymongo 
client = pymongo.MongoClient(baglanti)
# print(*client.list_database_names())
db = client["barkoddb"]
col = db["barkod24072023"]
# sonuc = col.insert_many(jsonKayitlar)
# print(sonuc.inserted_ids)

print(*col.find({"_id":"CZ01770755015"}))
sorguSonuc = col.find_one({"_id":"CZ01770755015"})
print(sorguSonuc["gonderi_durum_id"])
# [11, 813, 7, 3, 1, 3, 11]