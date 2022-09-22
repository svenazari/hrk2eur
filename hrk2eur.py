#Konvertiranje Kune u Euro prema fiksnom tečaju.
#Za korištenje je potrebno imati instaliran Python 3.
#Made by: SvenAzari
#https://github.com/svenazari

cur = float(input("IZNOS = ").replace(',','.')) #iznos za konverziju

rate = 7.53450 #fiksni tečaj za konverziju

eur = round(cur / rate, 2) #konverzija u euro
hrk = round(cur * rate, 2) #konverzija u kuna

#ispis
print("* * *")
print(str(cur) + " HRK = " + str(eur) + " EUR")
print(str(cur) + " EUR = " + str(hrk) + " HRK")
