import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
import os

os.system("cls")
print("Working...")

data = pd.read_excel("python/Voorbeeld_Divisie.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")

#Informatievraag 1



#Informatievraag 2



#Informatievraag 3
zwartBoek = .............................................
file3 = open("files/zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.pretty(zwartBoek, type="zwartboek"))
file3.close()


#Informatievraag 4









print("Done!")
