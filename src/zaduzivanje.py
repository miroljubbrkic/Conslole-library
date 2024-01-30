import datetime


#-------------------------------
#---------- M E N I ------------
#-------------------------------

def zadraz(zaduzenja,knjige,clanovi):
    while True:
        validno = False
        while not validno:
            pitanje = input("1 - zaduzivanje, 2 - razduzivanje, 0 - izadji: ")
            if pitanje == "1":
                validno = True
                knjiga123(knjige,clanovi,zaduzenja)
            elif pitanje == "2":
                validno = True
                pretragaKORISNIKA(clanovi,zaduzenja,knjige)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")



#------------------------------------------------
#---------PRETRAGA KNJIGE ZA ZADUZIVANJE---------
#------------------------------------------------

def knjiga123(knjige,clanovi,zaduzenja):

    pretraga = input("Ovde mozete pretraziti knjige: ")
    print("----------------")
    nadjeno = False
    lista_knjiga = []
    KNJIGA = {}
    for knjiga in knjige:
        if pretraga.lower() in knjiga["ISBN"].lower() or pretraga.lower() in knjiga["naslov"].lower() or pretraga.lower() in knjiga["autor"].lower() or pretraga.lower() in knjiga["godina"]:
            if int(knjiga["slobodno"]) > 0:
                rbr = knjiga["ISBN"].split("-")
                print("Redni broj: {}\nISBN: {}\nNaslov: {}\nAutor: {}\nGodina izdanja: {}\nSlobodno: {} knjiga(e)".format(rbr[0],knjiga["ISBN"],knjiga["naslov"],knjiga["autor"],knjiga["godina"],knjiga["slobodno"]))
                print("----------------")
                lista_knjiga.append(knjiga)
                nadjeno = True

    if nadjeno == True:
        rbr = input("Unesite redni broj knjige za zaduzivanje: ")
        nadjeno = False
        for k in lista_knjiga:
            if rbr == k["ISBN"].split("-")[0]:
                KNJIGA = k
                nadjeno = True
                print("Izabrali ste knjigu: ")
                print(KNJIGA)
                korisnik(KNJIGA,clanovi,zaduzenja,knjige)
        if nadjeno == False:
            validno = False
            while not validno:
                pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
                if pitanje == "1":
                    validno = True
                    knjiga123(knjige,clanovi,zaduzenja)
                elif pitanje == "0":
                    validno = True
                    return
                else:
                    print("Unos nije validan!")

    if nadjeno == False:
        print("Nije nadjena ni jedna knjiga ili nema slobodnih!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                knjiga123(knjige,clanovi,zaduzenja)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")


#-----------------------------------------------------
#-------- PRETRAGA KORISNIKA ZA ZADUZIVANJE ----------
#-----------------------------------------------------

def korisnik(KNJIGA,clanovi,zaduzenja,knjige):

    pretraga = input("Ovde mozete pretraziti korisnike: ")
    print("----------------")
    nadjeno = False
    lista_korisnika = []
    KORISNIK = {}
    for clan in clanovi:
        if pretraga in clan["id"] or pretraga.lower() in clan["ime"] or pretraga.lower() in clan["prezime"] or pretraga.lower() in clan["username"]:
            if "K" in clan["id"] and clan["aktivnost"] == True:
                rbr = clan["id"].split("-")[1]
                print("Redni broj: {}\nid: {}\nIme: {}\nPrezime: {}\nKorisnicko ime: {}".format(rbr,clan["id"],clan["ime"],clan["prezime"],clan["username"]))
                print("----------------")
                lista_korisnika.append(clan)
                nadjeno = True

    if nadjeno == True:
        nadjeno = False
        rbr = input("Unesite redni broj korisnika za zaduzivanje: ")
        for c in lista_korisnika:
            if c["id"].split("-")[1] == rbr:
                KORISNIK = c
                nadjeno = True
                print("Izabrali ste korisnika: ")
                print(KORISNIK)

                zaduzenja.append({"ISBN":KNJIGA["ISBN"],"zaduzeno":str(datetime.date.today()),"razduzeno":"","id":KORISNIK["id"]})
                for knjiga in knjige:
                    if knjiga["ISBN"] == KNJIGA["ISBN"]:
                        knjiga["slobodno"] = str(int(KNJIGA["slobodno"]) - 1) 

                print("Zaduzivanje uspesno izvrseno!")
                return

        if nadjeno == False:
            validno = False
            while not validno:
                pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
                if pitanje == "1":
                    validno = True
                    korisnik(KNJIGA,clanovi,zaduzenja,knjige)
                elif pitanje == "0":
                    validno = True
                    return
                else:
                    print("Unos nije validna!")

    if nadjeno == False:
        print("Nije nadjena ni jedan korisnik!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                korisnik(KNJIGA,clanovi,zaduzenja,knjige)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!") 



#--------------------------------------------------------       
#---------- PRETRAGA KORISNIKA ZA RAZDUZIVANJE ----------
#--------------------------------------------------------

def pretragaKORISNIKA(clanovi,zaduzenja,knjige):

    pretraga = input("Ovde mozete pretraziti korisnike: ")
    print("----------------")
    nadjeno = False
    lista_korisnika = []
    KORISNIK = {}
    for clan in clanovi:
        if pretraga in clan["id"] or pretraga.lower() in clan["ime"] or pretraga.lower() in clan["prezime"] or pretraga.lower() in clan["username"]:
            if "K" in clan["id"] and clan["aktivnost"] == True:
                rbr = clan["id"].split("-")[1]
                print("Redni broj: {}\nid: {}\nIme: {}\nPrezime: {}\nKorisnicko ime: {}".format(rbr,clan["id"],clan["ime"],clan["prezime"],clan["username"]))
                print("----------------")
                lista_korisnika.append(clan)
                nadjeno = True
    
    if nadjeno == False:
        print("Nije pronadjen ni jedan korsinik!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                pretragaKORISNIKA(clanovi,zaduzenja,knjige)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")

    if nadjeno == True:
        nadjeno = False
        validno = False
        while not validno:
            rbr = input("Unesite redni broj korisnika za zaduzivanje ili 0  za nazad: ")
            for c in lista_korisnika:
                if c["id"].split("-")[1] == rbr:
                    KORISNIK = c
                    nadjeno = True
                    validno = True
                    print("Izabrali ste korisnika: ",KORISNIK["ime"]," ",KORISNIK["prezime"])
                    pretragaZAD(zaduzenja,KORISNIK,clanovi,knjige)      #name knjige is not defined
                if rbr == "0":
                    validno = True
                    return
                if nadjeno == False:
                    print("Unos nije validan!")



#---------------------------------------------------------
#---------- PRETRAGA ZADUZENJA ZA RAZDUZIVANJE -----------
#---------------------------------------------------------

def pretragaZAD(zaduzenja,KORISNIK,clanovi,knjige):

    nadjeno = False
    i = 1
    zad_za_raz = []
    for zad in zaduzenja:
        if KORISNIK["id"] == zad["id"] and zad["razduzeno"] == "":
            print("------------")
            print("Redni broj: {}\nISBN knjige: {}\nzaduzeno: {}\nrazduzeno: {}\nID korisnika: {}".format(i,zad["ISBN"],zad["zaduzeno"],zad["razduzeno"],zad["id"]))
            zad_za_raz.append({"rbr":str(i),"ISBN":zad["ISBN"],"zaduzeno":zad["zaduzeno"],"razduzeno":zad["razduzeno"],"id":zad["id"]})
            i = i + 1
            nadjeno = True

    if nadjeno == False:
        print("Izabrani korisnik nema zaduzenja!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                pretragaKORISNIKA(clanovi,zaduzenja,knjige)
            elif pitanje == "0":
                validno = True
                zadraz()
            else:
                print("Unos nije validan!")

    if nadjeno == True:
        nadjeno = False
        validno = False
        while not validno:
            rbr = input("Unesite redni broj zaduzenja ili 0 za nazad: ")
            zaduzeni = {}
            for z in zad_za_raz:
                if rbr == z["rbr"]:
                    validno = True
                    zaduzeni = z
                    del zaduzeni["rbr"]
                    index = zaduzenja.index(zaduzeni)
                    nadjeno = True
                    zaduzeni["razduzeno"] = str(datetime.date.today())
                    zaduzenja[index] = zaduzeni
                    print("Korisnik uspesno razduzen!")
                    zadraz(zaduzenja,knjige,clanovi)
            if rbr == "0":
                validno = True
                pretragaKORISNIKA(clanovi,zaduzenja,knjige)
            if nadjeno == False:
                print("Unos nije validan!")

