liste = ["Cevaplar","Serkan","Gül","Saniye","Sinan","Hatice","Tevfik","Mehmed","Şengül"]
import shutil
import os
fileName = "02_Manipulation.ipynb"
for item in liste:
    if not os.path.exists(os.path.join("Exercises",item)):
        os.mkdir(os.path.join("Exercises",item))
    if not os.path.exists(os.path.join("Exercises",item,"data")):
        os.mkdir(os.path.join("Exercises",item,"data"))
    sourcePath = "/workspace/DataMiningFundamentals/Documents/01_Libraries/Data/50_Startups.csv"
    destPath = os.path.join("Exercises",item,"data","50_Startups.csv")
    shutil.copy(sourcePath,destPath)
    open(os.path.join("Exercises",item,fileName),"w+")
