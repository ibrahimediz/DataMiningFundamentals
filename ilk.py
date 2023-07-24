liste = ["Cevaplar","Serkan","Gül","Saniye","Sinan","Hatice","Tevfik","Mehmed","Şengül"]
import shutil
import os
fileName = "ornek.ipynb"
for item in liste:
    if not os.path.exists(os.path.join("Exercises",item)):
        os.mkdir(os.path.join("Exercises",item))
    open(os.path.join("Exercises",item,fileName),"w+")
