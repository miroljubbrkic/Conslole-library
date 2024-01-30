import datetime
from zaduzivanje import*

#from main import*


#--------------------------------------------------
#-------------- MENI ZA BIBLIOTEKARA --------------
#--------------------------------------------------

def B_meni(izabran,clanovi,zaduzenja,knjige):
    while True:
        validno = False
        while not validno:
            pitanje = input(
        """
        1 - Izmena/unos knjiga
        2 - Izmena/unos clanova
        3 - Izmena prijavljenog
        4 - Zaduzivanje/razduzivanje
        5 - rashodovanje
        6 - Brisanje korisnika
        0 - nazad :

        """)

            if pitanje == "1":
                validno = True
                unos_izmena_knjiga(knjige,izabran)
            elif pitanje == "2":
                validno = True
                unos_izmena_clanova(clanovi,izabran)
            elif pitanje == "3":
                validno = True
                trenutni(izabran,clanovi)
            elif pitanje == "4":
                validno = True
                zadraz(zaduzenja,knjige,clanovi)
            elif pitanje == "5":
                validno = True
                rashodovanje(knjige)
            elif pitanje == "6":
                validno = True
                brisanjeClana(clanovi)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")



#------------------------------------------------------
#------------- MENI UNOS/IZMENA CLANOVA ---------------
# #---------------------------------------------------- 

def unos_izmena_clanova(clanovi,izabran):
    while True:
        validno = False
        while not validno:
            pitanje = input("1 - izmena clanova, 2 - dodavanje clanova, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                editCLANOVA(clanovi)
            elif pitanje == "2":
                validno = True
                addClana(clanovi)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")



#-----------------------------------------------------
#------------- MENI UNOS/IZMENA KNJIGA ---------------
# #--------------------------------------------------- 

def unos_izmena_knjiga(knjige,izabran):
    while True:
        validno = False
        while not validno:
            pitanje = input("1 - izmena knjiga, 2 - dodavanje knjiga, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                editKNNJIGA(knjige,izabran)
            elif pitanje == "2":
                validno = True
                addKNJIGA(knjige)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")



#--------------------------------------------
#----------I Z M E N A   K NJ I G A----------
#--------------------------------------------

def editKNNJIGA(knjige,izabran):
    print("--- IZMENA KNJIGA ---")
    idd = input("Unesite id knjige za izmenu (sa ili bez crtica): ")
    nadjeno = False
    for knjiga in knjige:
        if idd == knjiga["ISBN"] or idd == "".join(knjiga["ISBN"].split("-")):
            nadjeno = True
            pitanje = input("Izmenite:\n1 - naslov,\n2 - autor,\n3 - godina,\n4 - ukupno,\n0 - nazad: ")
            validno = False
            while not validno:
                
                if pitanje == "1":
                    validno = True
                    dalje = True
                    while dalje:
                        dalje = False
                        knjiga["naslov"] = input("Unesite naslov: ")
                        if knjiga["naslov"] == "":
                            dalje = True
                            print("Morate uneti naslov!")
                        
                        else:
                            print("Izmena je uspesno izvrsena!")
                            return
                            
                    
                elif pitanje == "2":
                    validno = True
                    dalje = False
                    while not dalje:
                        knjiga["autor"] = input("Unesite autora: ")
                        if knjiga["autor"] == "":
                            prijava("Morate uneti autora!")
                        else:
                            dalje = True
                            print("Izmena je uspesno izvrsena!")
                            return                    
                            

                elif pitanje == "3":
                    validno = True
                    dalje = False
                    while not dalje:
                        knjiga["godina"] = input("Unesite godinu izdanja: ")
                        if knjiga["godina"].isdigit():
                            dalje = True
                            print("Izmena je uspesno izvrsena!")
                            return
                        else:
                            print("Morate uneti godinu!")
                            
                elif pitanje == "4":
                    validno = True
                    dalje = False
                    while not dalje:
                        Nukupno = input("Unesite ukupan broj knjiga: ")
                        if Nukupno.isdigit() and int(Nukupno) >= int(knjiga["ukupno"]):
                            dalje = True
                            razl = int(Nukupno) - int(knjiga["ukupno"])
                            knjiga["ukupno"] = Nukupno
                            knjiga["slobodno"] = str(int(knjiga["slobodno"]) + razl)
                            print("Izmena je uspesno izvrsena!")
                            return
                        else:
                            print("Ako zelite da smanjite broj knjiga idite u opciju rashodovanje!")
                            return

                elif pitanje == "0":
                    validno = True
                    return
                else:
                    print("Unos nije validan!")
    if nadjeno == False:
        print("Ne postoji ni jedna knjiga sa unetim id-om!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                editKNNJIGA(knjige,izabran)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")



#-------------------------------------------------
#----------D O D A V A NJ E   K NJ I G A----------
#-------------------------------------------------

def addKNJIGA(knjige):
    print("--- DODAVANJE KNJIGA ---")
    now = datetime.datetime.now()
    idd = str(len(knjige)+1) + "-" + str(now.year)
    validno = False
    while not validno:
        naslov = input("Unesite naslov: ")
        if naslov == "":
            print("Morate uneti naslov!")
        else:
            validno = True

    validno = False
    while not validno:
        autor = input("Unesite autora: ")
        if autor == "":
            print("Morate uneti autora!")
        else:
            validno = True

    validno = False
    while not validno:
        godina = input("Unesite godinu: ")
        if godina.isdigit():
            validno = True
        else:
            print("Morate uneti godinu!")

    validno = False
    while not validno:
        ukupno = input("Unesite ukupan broj knjiga: ")
        if ukupno.isdigit():
            validno = True
        else:
            print("Morate uneti broj!")

    knjige.append({"ISBN": idd,"naslov": naslov,"autor": autor,"godina": godina,"ukupno": ukupno,"slobodno": ukupno})



#-----------------------------------------------
#----------I Z M E N A   C L A N O V A----------
#-----------------------------------------------

def editCLANOVA(clanovi):
    print("--- IZMENA CLANOVA ---")
    idd = input("Unesite id clana kojeg zelite da izmenite (sa ili bez crtica): ")

    nadjeno = False
    for clan in clanovi:
        if idd == clan["id"] or idd == "".join(clan["id"].split("-")):
            nadjeno = True
            dalje = False
            while not dalje:
                pitanje = input("1 - ime, 2 - prezime, 3 - korisnicko ime, 4 - lozinka, 5 - aktivacija, 0 - nazad: ")
                if pitanje == "1":
                    dalje = True
                    validno = False
                    while not validno:
                        clan["ime"] = input("Unesite novo ime: ")
                        if clan["ime"] == "":
                            print("Morate uneti ime!")
                        else:
                            validno = True
                            print("Izmena je uspesno izvrsena!")
                            editCLANOVA(clanovi)
                
                elif pitanje == "2":
                    dalje = True
                    validno = False
                    while not validno:
                        clan["prezime"] = input("Unesite novo prezime: ")
                        if clan["prezime"] == "":
                            print("Morate uuneti prezime!")
                        else:
                            validno = True
                            print("Izmena je uspesno izvrsena!")
                            editCLANOVA(clanovi)

                elif pitanje == "3":
                    dalje = True
                    username = input("Unesite novo korisnicko ime: ")
                    razl = True
                    for i in clanovi:
                        if username == i["username"] or username == "":
                            razl = False
                            print("Korisnicko ime je vec u upotrebi")
                            validno = False
                            while not validno:
                                pitanje = input("1 - pokusajte ponovo, 0 - nazada: ")
                                if pitanje == "0":
                                    print("Odustali ste od prijave!")
                                    validno = True
                                    return
                                elif pitanje == "1":
                                    validno = True
                                    editCLANOVA(clanovi)
                                else:
                                    print("Unos nije validan!")
                    if razl == True:
                        clan["username"] = username
                        print("Izmena je uspesno izvrsena!")
                        editCLANOVA(clanovi)

                elif pitanje == "4":
                    dalje = True
                    validno = False
                    while not validno:
                        clan["lozinka"] = input("Unesite novu lozinku: ")
                        if clan["lozinka"] == "":
                            print("Morate uneti lozinku!")
                        else:
                            print("Izmena je uspesno izvrsena!")
                            return

                elif pitanje == "5":
                    dalje = True
                    if clan["aktivnost"] == False:
                        validno = False
                        while not validno:
                            y = input("Da li zelite da aktivirate clana (da/ne): ")
                            if y.lower() == "da":
                                clan["aktivnost"] =True
                                print("Izmena je uspesno izvrsena")
                                validno = True
                            elif y.lower() == "ne":
                                print("Clan nije aktiviran!")
                                validno = True
                            else:
                                print("Unos nije validan!")
                        return
                    else:
                        print("Clan je vec aktivan!")
                        return

                elif pitanje == "0":
                    dalje = True
                    return
                
                else:
                    print("Unos nije validan!")

    if nadjeno == False:
        print("Ne postoji ni jedan korisnik sa unetim id-om!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazada: ")
            if pitanje == "1":
                validno = True
                editCLANOVA(clanovi)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")



#------------------------------------------------   
#----------D O D A V A NJ E   C L A N A----------    
#------------------------------------------------                            

def addClana(clanovi):
    print("--- DODAVANJE CLANA ---")

    validno = False
    while not validno:
        ime = input("Unesite ime: ")
        if ime == "":
            print("Morate uneti ime!")
        else:
            validno = True

    validno = False
    while not validno:
        prezime = input("Unesite prezime: ")
        if prezime == "":
            print("Morate uneti prezime!")
        else:
            validno = True
            
    aktivnost = True

    validno = False
    
    while not validno:
        dalje = True
        username = input("Unesite korisnicko ime: ")
        for clan in clanovi:
            if clan["username"] == username or username == "":
                print("Korisnicko ime je vec iskorisceno ili nije uneseno!")
                dalje = False
        if dalje == True:
            validno = True
                
    validno = False
    now = datetime.datetime.now()
    while not validno:
        ko = input("Koga zelite da kreirate b - bibliotekar, k - korisnik: ")
        if ko.lower() == "b":
            idd = "B" + "-" + str(len(clanovi)+1) + "-" + str(now.year)
            validno = True
        elif ko.lower() == "k":
            idd = "K" + "-" + str(len(clanovi)+1) + "-" + str(now.year) 
            validno = True
        else:
            print("Unos nije validan!")

    validno = False
    while not validno:
        lozinka = input("Unesite lozinku: ")
        if lozinka == "":
            print("Morate uneti lozniku!")
        else:
            validno = True

    clanovi.append({"id":idd,"ime":ime,"prezime":prezime,"aktivnost":aktivnost,"username":username,"lozinka":lozinka}) 
    print("Uspesno je dodat clan")



#--------------------------------------------------------
#----------I Z M E N A   P R I J A V LJ E N O G----------
#--------------------------------------------------------

def trenutni(izabran,clanovi):
    print("--- IZMENA PRIJAVLJENOG ---")
    nadjeno = True
    dalje = False
    while not dalje:
        pitanje = input("1 - ime, 2 - prezime, 3 - korisnicko ime, 4 - lozinka, 0 - nazad: ")
        if pitanje == "1":
            dalje = True
            validno = False
            while not validno:
                izabran["ime"] = input("Unesite novo ime: ")
                if izabran["ime"] == "":
                    print("Morate uneti ime!")
                else:
                    validno = True
                    print("Izmena je uspesno izvrsena!")
                    return
        
        elif pitanje == "2":
            dalje = True
            validno = False
            while not validno:
                izabran["prezime"] = input("Unesite novo prezime: ")
                if izabran["prezime"] == "":
                    print("Morate uuneti prezime!")
                else:
                    validno = True
                    print("Izmena je uspesno izvrsena!")
                    return

        elif pitanje == "3":
            dalje = True
            username = input("Unesite novo korisnicko ime: ")
            razl = True
            for i in clanovi:
                if username == i["username"] or username == "":
                    razl = False
                    print("Korisnicko ime je vec u upotrebi")
                    validno = False
                    while not validno:
                        pitanje = input("1 - pokusajte ponovo, 0 - nazada: ")
                        if pitanje == "0":
                            print("Odustali ste od prijave!")
                            validno = True
                            return
                        elif pitanje == "1":
                            validno = True
                            trenutni(izabran,clanovi)
                        else:
                            print("Unos nije validan!")
            if razl == True:
                izabran["username"] = username
                print("Izmena je uspesno izvrsena!")
                return

        elif pitanje == "4":
            dalje = True
            validno = False
            while not validno:
                izabran["lozinka"] = input("Unesite novu lozinku: ")
                if izabran["lozinka"] == "":
                    print("Morate uneti lozinku!")
                else:
                    print("Izmena je uspesno izvrsena!")
                    return

        elif pitanje == "0":
            dalje = True
            return
        
        else:
            print("Unos nije validan!")
    


#----------------------------------------------
#----------B R I S A NJ E   C L A N A----------
#----------------------------------------------

def brisanjeClana(clanovi):
    print("--- BRISANJE KORISNIKA ---")
    clanovi_za_brisanje = []
    for clan in clanovi:
        if clan["aktivnost"] == True and "K" in clan["id"]:
            print(" {}. {} {}".format(clan["id"].split("-")[1], clan["ime"], clan["prezime"]))
            clanovi_za_brisanje.append(clan)
    bris = input("Unesite redni broj clana kojeg zelite da obrisete: ")
    nadjeno = False
    for i in clanovi_za_brisanje:
        if bris == i["id"].split("-")[1]:     
            nadjeno = True
    if nadjeno == True:
        for clan in clanovi:
            if clan["id"].split("-")[1] == bris:
                clan["aktivnost"] = False
                print("Izmena je uspesno izvrsena!")
    if nadjeno == False:
        print("Nije pronadjen ni jedan korisnik pod unetim rednim brojem!")
        validno = False
        while not validno:
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                brisanjeClana(clanovi)
            elif pitanje == "0":
                validno = True
                return
            else:
                print ("Unos nije validan!")



#------------------------------------------
#----------R A S H O D O V A NJ E----------
#------------------------------------------

def rashodovanje(knjige):
    print("--- RASHODOVANJE ---")
    idd = input("Unesite id knjige za rashodovanje: ")
    nadjeno = False
    for knjiga in knjige:
        if idd == knjiga["ISBN"]:
            rshd = input("Unesite broj knjiga koje se rashoduju: ")
            if int(rshd) <= int(knjiga["slobodno"]):
                knjiga["ukupno"] = str(int(knjiga["ukupno"]) - int(rshd))
                knjiga["slobodno"] = str(int(knjiga["slobodno"]) - int(rshd))
                nadjeno = True
                print("Knjiga je rashodovana!")
    if nadjeno == False:
        validno = False
        while not validno:
            print("Ne postoji knjiga sa unetim id-om ili nema slobodnih knjiga!")
            pitanje = input("1 - pokusajte ponovo, 0 - nazad: ")
            if pitanje == "1":
                validno = True
                rashodovanje(knjige)
            elif pitanje == "0":
                validno = True
                return
            else:
                print("Unos nije validan!")
