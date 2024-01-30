import json
from ucitavanje import *
from bibliotekar import *
from korisnik import *

clanovi = []
knjige = []
zaduzenja = []

#-------- P O C E T N I  M E N I -----------------
def MENI():
    while True:
        pitanje = input("1 - log in, 0 - ugasi: ")
        if pitanje == "1":
            prijava(clanovi)
        elif pitanje == "0":
            zapisi_clanove(clanovi)
            zapisi_knjige(knjige)
            zapisi_zaduzenja(zaduzenja)
            print("ZAVRSEN RAD!")
            return

#-------- P R I J A V A ---------------------------
def prijava(clanovi):
    print("--- PRIJAVA NA SISTEM ---")
    
    pronadjen = False
    while not pronadjen: 
        username = input("Unesite korisnicko ime: ")
        lozinka = input("Uneiste lozinku: ")     
        for izabran in clanovi:
            if izabran["username"] == username and izabran["lozinka"] == lozinka and izabran["aktivnost"] == True:
                if "B" in izabran["id"]:
                    print("Prijavljen je bibliotekar: {} {}".format(izabran["ime"],izabran["prezime"]))
                    pronadjen = True
                    B_meni(izabran,clanovi,zaduzenja,knjige) 

                elif "K" in izabran["id"]:
                    print("Prijavljen je clan: {} {}".format(izabran["ime"],izabran["prezime"]))
                    pronadjen = True
                    K_meni(izabran,clanovi,zaduzenja,knjige)

        if pronadjen == False:
            print("Nije pronadjen ni jedan clan sa unetim parametrima!")
            validno = False
            while not validno:
                pitanje = input("1 - pokusajte ponovo, 0 - odustajem od prijave: ")
                if pitanje == "1":
                    validno = True
                    continue
                elif pitanje == "0":
                    validno = True
                    print("Odustali ste od prijave!")
                    return
                else:
                    print("Unos nije validan!")
   


proveri_clanove(clanovi)
proveri_knjige(knjige)
proveri_zaduzenja(zaduzenja)

MENI()

