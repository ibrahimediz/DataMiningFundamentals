from pandas import DataFrame,read_csv
from pymongo import MongoClient
class DBTool:
    def __init__(self,adres,mbaglanti,**kwargs):
        self.adres = adres
        self.mbaglanti = mbaglanti
        self.kayitlar = []
        self.client = None
        self.db = None
        self.col = None
        for key,value in kwargs.items():
            if key == "db":
                self.db = value
            if key == "col":
                self.col = value
        else:
            if not (self.db and self.col):
                self.db = "barkodkayitlar"
                self.col = "barkod26072023"


    def baglan(self):
        self.client = MongoClient(self.mbaglanti)
        self.db = self.client[self.db]
        self.col = self.db[self.col]

    def csvDonustur(self,delimiter=";"): # 1
        self.df = read_csv(self.adres,delimiter=delimiter)
        for barkod in self.df.barkod_no.unique():
             kayit = []
             kayit.insert(0,barkod)
             digerSutunlar= self.df.columns[1:]
             for sutun in digerSutunlar:
                 kayit.append(list(self.df[self.df["barkod_no"] == barkod][sutun]))
             self.kayitlar.append(kayit)

    def mongodbEkleList(self,liste):
        sonuc = self.col.insert_many(liste)

    def mongodbEkleTek(self,kayit):
        sonuc = self.col.insert_one(kayit)


    def listeDonustur(self):
        jsonKayitlar = []
        dfJson = self.csv2json(param=1)
        for i in range(dfJson.shape[0]):
            jsonKayit = {"_id":dfJson.index[i]}
            for item in self.df.columns[1:]:
                jsonKayit[item] = dfJson.iloc[i,:][item]
            jsonKayitlar.append(jsonKayit)
        return jsonKayitlar

    def csv2json(self,jsadres="",param=0):
        dfJson = DataFrame(self.kayitlar).set_index(0)
        dfJson.columns = self.df.columns[1:]
        if param and not jsadres:
            return dfJson
        dfJson.to_json(jsadres,orient="index")
        
if __name__== "__main__":
    adres = "/workspace/DataMiningFundamentals/Documents/01_Libraries/Data/data2.csv"
    baglanti = "mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority"
    obj = DBTool(adres,baglanti)
    obj.baglan()
    obj.csvDonustur()
    jkayitlar = obj.listeDonustur()
    obj.mongodbEkleList(jkayitlar)


# baglanti = "mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority"
# import pymongo 
# client = pymongo.MongoClient(baglanti)
# for item in client.list_database_names():
#     db = client[item]
#     for item2 in db.list_collection_names():
#         db.drop_collection(item2)
#     else:
#         client.drop_database(item)

