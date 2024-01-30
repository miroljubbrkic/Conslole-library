import json

#------------- UCITAVANJE KNJIGA IZ FAJLA ------------------

def proveri_knjige(knjige):
    try:
        with open("data/knjige.json","r",encoding="utf-8") as f:
            sveknjige = json.load(f)
            for knjiga in sveknjige:
                knjige.append(knjiga)
    except FileNotFoundError:
        noveKnjige = [
        {"ISBN": "1-2000","naslov": "Na Drini cuprija","autor": "Ivo Andric","godina": "2014","ukupno": "22","slobodno": "21"},
        {"ISBN": "2-2014","naslov": "Zivot i prikljucenija","autor": "Dositej Obradovic","godina": "2007","ukupno": "13","slobodno": "13"},
        {"ISBN": "3-2017","naslov": "Uspeh sto da ne","autor": "Dzek Kenfild","godina": "2012","ukupno": "20","slobodno": "0"},
        {"ISBN": "4-2019","naslov": "Pink panteri","autor": "Vladimir Lamar","godina": "2015","ukupno": "10","slobodno": "9"},
        {"ISBN": "5-2016","naslov": "aaaa","autor": "bbbb","godina": "2008","ukupno": "222","slobodno": "222"},
        {"ISBN": "6-2003","naslov": "oop1","autor": "Dejan Zivkovic","godina": "2019","ukupno": "40","slobodno": "40"}
        ]
        knjige.extend(noveKnjige)



#------------- UCITAVANJE CLANOVA IZ FAJLA ------------------

def proveri_clanove(clanovi):
    try:
        with open("data/clanovi.json","r",encoding="utf-8") as f:
            sviclanovi = json.load(f)
            for clan in sviclanovi:
                clanovi.append(clan)
    except FileNotFoundError:
        noviclanovi = [
        {"id": "B-1-2018","ime": "Miroljub","prezime": "Brkic","aktivnost": True,"username": "miroljubbr","lozinka": "qwerty"},
        {"id": "K-2-2018","ime": "Voja","prezime": "VESELINOVIC","aktivnost": True,"username": "vojav","lozinka": "54321"},
        {"id": "K-3-2019","ime": "qwerty","prezime": "qwerty","aktivnost": True,"username": "qwerty","lozinka": "asdf"},
        {"id": "K-4-2019","ime": "123","prezime": "123","aktivnost": True,"username": "123","lozinka": "123"}
        ]
        clanovi.extend(noviclanovi)


#------------- UCITAVANJE KNZADUZENJA IZ FAJLA ------------------

def proveri_zaduzenja(zaduzenja):
    try:
        with open("data/zaduzenja.json","r",encoding="utf-8") as f:
            svazaduzenja = json.load(f)
            for zaduzenje in svazaduzenja:
                zaduzenja.append(zaduzenje)
    except FileNotFoundError:
        novazaduzenja = [
        {"ISBN": "4-2019","zaduzeno": "2019-03-01","razduzeno": "","id": "K-3-2019"},
        {"ISBN": "1-2000","zaduzeno": "2019-03-01","razduzeno": "2019-03-02","id": "K-2-2018"},
        {"ISBN": "4-2019","zaduzeno": "2019-03-01","razduzeno": "","id": "K-2-2018"},
        {"ISBN": "1-2000","zaduzeno": "2019-04-24","razduzeno": "","id": "K-2-2018"}
        ]
        zaduzenja.extend(novazaduzenja)

#---------- MEMORISANJE KNJIGA --------------
def zapisi_knjige(knjige):
    with open("data/knjige.json","w",encoding="utf-8") as f:
        json.dump(knjige,f,indent=4)

#------------ MEMORISANJE CLANOVA -----------
def zapisi_clanove(clanovi):
    with open("data/clanovi.json", "w", encoding="utf-8") as f:
        json.dump(clanovi, f,indent=4)

#---------- MEMORISANJE ZADUZENJA -----------
def zapisi_zaduzenja(zaduzenja):
    with open("data/zaduzenja.json", "w", encoding="utf-8") as f:
        json.dump(zaduzenja, f,indent=4)


