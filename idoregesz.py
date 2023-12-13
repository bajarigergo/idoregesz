import idoregesz
import listak

penz = 0
kulcs = False
elet = 5
lepes = 0
def kezdes(kiiras):
    return kiiras[0]

def bemenet():
    parancs = str(input(">"))
    return str(parancs)

# def eldont(parancs:str):
#     x = parancs.split()
#     ige = parancs[0]
#     if parancs[1] in listak.helyszinek:
#         helyszin = parancs[1]
#         return helyszin and ige
#     elif parancs[1] in listak.helyszinek:
#         fonev = parancs[1]
#         return fonev and ige

def lepes_1(parancs:str):
    idoregesz.lepes = 0
    idoregesz.elet = 5
    idoregesz.kulcs = False
    idoregesz.penz = 0
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige =="megy" and helyszin in listak.kezdes:
        print(listak.kiiras[1])
        lepes_2(bemenet())
    else:
        lepes_1(bemenet())

def lepes_2(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige =="megy" and helyszin=="kut" or helyszin=="kút":
        print(listak.kiiras[2])
        lepes_3(bemenet())
    elif ige =="megy" and helyszin in listak.kut:
        print(listak.kiiras[4])
        lepes_4(bemenet())
    elif ige == "megy" and helyszin =="kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_2(bemenet())

def lepes_3(parancs:str):
    x = parancs.split()
    ige = x[0]
    fonev = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige =="felvesz" and fonev == "penz" or fonev == "pénz":
        idoregesz.penz == 1
        print(listak.kiiras[3])
        lepes_4(bemenet())
    elif ige == "megy" and helyszin =="kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_3(bemenet())

def lepes_4(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige =="megy" and helyszin in listak.mezo:
        print(listak.kiiras[4])
        lepes_5(bemenet())
    elif ige == "megy" and helyszin == "kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_4(bemenet())

def lepes_5(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige =="megy" and helyszin == "vartemplom" or helyszin == "vártemplom":
        print(listak.kiiras[5])
        lepes_6(bemenet())
    elif ige=="megy" and helyszin=="kamra":
        print(listak.kiiras[8])
        lepes_9(bemenet())
    elif ige == "megy" and helyszin=="ajto" or helyszin=="ajtó":
        print(listak.kiiras[13])
        lepes_13(bemenet())
    elif ige == "megy" and helyszin == "kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_5(bemenet())

def lepes_6(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige == "hasznal" or ige == "használ" and helyszin == "penz" or helyszin == "pénz" and penz>0:
        print(listak.kiiras[6])
        idoregesz.penz -=1
        lepes_7(bemenet())
    elif ige == "megy" and helyszin == "kamra":
        print(listak.kiiras[8])
        lepes_9(bemenet())
        print(listak.kiiras[8])
    elif ige == "megy" and helyszin == "ajto" or helyszin == "ajtó":
        print(listak.kiiras[13])
        lepes_13(bemenet())
    elif ige == "megy" and helyszin == "kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_6(bemenet())

def lepes_7(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige == "felvesz" and helyszin == "kulcs":
        print(listak.kiiras[7])
        idoregesz.kulcs = True
        lepes_6(bemenet())
    elif ige == "megy" and helyszin == "kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_7(bemenet())

def lepes_9(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige == "eszik" and helyszin == "etel" or helyszin == "étel":
        print(listak.kiiras[11])
        idoregesz.lepes == 0
        idoregesz.elet == 10
        lepes_9(bemenet())
    elif ige == "megy" and helyszin == "faajto" or helyszin == "faajtó":
        print(listak.kiiras[9])
        lepes_14(bemenet())
    elif ige == "megy" and helyszin == "ajto" or helyszin == "ajtó":
        print(listak.kiiras[12])
    elif ige == "megy" and helyszin == "kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
    else:
        lepes_9()

def lepes_14(parancs:str):
    x = parancs.split()
    ige = x[0]
    helyszin = x[1]
    if idoregesz.lepes > 3:
        idoregesz.elet -= 1
    if idoregesz.elet == 0:
        print("Elfogyott az életerőd, Vége a játéknak")
    if ige == "hasznal" or ige == "használ" and helyszin == "kulcs" and idoregesz.kulcs == True:
        print(f"{listak.kiiras[10]}\n\tGratulálunk nyertél!!")
    elif ige == "hasznal" or ige == "használ" and helyszin == "kulcs" and idoregesz.kulcs == False:
        print(listak.kiiras[13])
    elif ige == "megy" and helyszin == "kezdes" or helyszin == "kezdés":
        print(listak.kiiras[1])
        lepes_1(bemenet())
