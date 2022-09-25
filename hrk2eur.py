#Konvertiranje Kune u Euro prema fiksnom tečaju.
#Za korištenje je potrebno imati instaliran Python 3.
#Made by: SvenAzari
#https://github.com/svenazari

from os import system, name

def clear (): #čišćenje ekrana
  if name == 'nt':
      _ = system('cls')
  else:
      _ = system('clear')

def conversion ():
    clear () #očisti ekran
    cur = float(input("IZNOS = ").replace(',','.')) #iznos za konverziju

    rate = 7.53450 #fiksni tečaj za konverziju 

    eur = round(cur / rate, 2) #konverzija u euro
    hrk = round(cur * rate, 2) #konverzija u kuna

    #ispis
    print("* * *")
    print(str(cur) + " HRK = " + str(eur) + " EUR")
    print(str(cur) + " EUR = " + str(hrk) + " HRK")
    print("* * *")

    fuex () #pozovi funkciju za odabir novog unosa ili izlaza

def fuex (): #izlaz
  ex = float(input ("[1 (novi unos), 2 (izlaz)]: "))
  if ex == 1:
    conversion ()
  elif ex == 2:
    clear ()
    exit ()
  else:
    print ("Pogrešan unos!")
    fuex ()

conversion ()