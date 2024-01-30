from bibliotekar import trenutni

#--------- K O R I S N I C K I  M E N I ----------------
def K_meni(izabran,clanovi,zaduzenja,knjige):
    while True:
        validno = False
        while not validno:
            pitanje = input(
            """
            1 - pregled zaduzenih knjiga
            2 - pretrazivanje knjiga
            3 - izmena podataka
            0 - nazad (prijava):

            """)
            if pitanje == "0":
                return
            elif pitanje == "1":
                validno = True
                pregled_zaduzenja(zaduzenja,izabran)
            elif pitanje == "2":
                validno = True
                pretraga_knjiga(knjige)
            elif pitanje == "3":
                validno = True
                trenutni(izabran,clanovi)

#------------- P R E G L E D  Z A D U Z E N J A ------------
def pregled_zaduzenja(zaduzenja,izabran):
    i = 1
    zad_za_raz = []
    for zad in zaduzenja:
        if zad["id"] == izabran["id"] and zad["razduzeno"] == "":
            print("------------")
            print("Redni broj: {}\nISBN knjige: {}\nzaduzeno: {}\nrazduzeno: {}\nID korisnika: {}".format(i,zad["ISBN"],zad["zaduzeno"],zad["razduzeno"],zad["id"]))
            zad_za_raz.append({"rbr":str(i),"ISBN":zad["ISBN"],"zaduzeno":zad["zaduzeno"],"razduzeno":zad["razduzeno"],"id":zad["id"]})
            i = i + 1
    validno = False
    while not validno:
        pitanje = input("pritisnite 0 za nazad: ")
        if pitanje == "0":
            validno = True
            return
        else:
            print("Unos nije validan!")
    
#--------- P R E T R A Z I V A  N J E  K NJ I G A --------------
def pretraga_knjiga(knjige):
    pretraga = input("Ovde mozete pretraziti knjige: ")
    print("----------------")
    nadjeno = False
    lista_knjiga = []
    KNJIGA = {}
    i = 1
    for knjiga in knjige:
        if pretraga.lower() in knjiga["naslov"].lower() or pretraga.lower() in knjiga["autor"].lower():
            if int(knjiga["slobodno"]) > 0:
                nadjeno = True
                rbr = knjiga["ISBN"].split("-")
                print("Redni broj: {}\nISBN: {}\nNaslov: {}\nAutor: {}\nGodina izdanja: {}\nSlobodno: {} knjiga(e)".format(str(i),knjiga["ISBN"],knjiga["naslov"],knjiga["autor"],knjiga["godina"],knjiga["slobodno"]))
                i = i + 1
                print("-----------------------")

    if nadjeno == True:
        validno = False
        while not validno:
            pitanje = input("0 - nazad: ")
            if pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")

    
    if nadjeno == False:
        print("Nije pronadjena ni jedna knjiga")
        pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
        validno = False
        while not validno:
            if pitanje == "1":
                validno = True
                pretraga_knjiga(knjige)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")
