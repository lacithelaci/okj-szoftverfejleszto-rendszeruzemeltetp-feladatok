class Berek:
    def __init__(self,nev,nem,reszleg,belepes,ber):
        self.nev = nev
        self.nem = nem
        self.reszleg = reszleg
        self.belepes = int(belepes)
        self.ber =int(ber)
    def __repr__(self):
        return f"{self.nev} {self.nem} {self.reszleg} {self.belepes} {self.ber}"
lista=[]
f=open("berek2020.txt",encoding="UTF-8")
elso_sor=f.readline()
for i in f:
    i=i.strip().split(";")
    lista.append(Berek(*i))
print(f"3. feladat: Dolgozók száma: {len(lista)} fő")
berek=[i.ber for i in lista]
print(f"4. feladat: Bérek átlaga: {((sum(berek)/len(berek))/1000):.1f} eFT")
print("5. feladat")
a=input("Kérem egy részleg nevét")
print("6. feladat")
reszleg=[i.ber for i in lista if i.reszleg==a]
if len(reszleg)==0:
    print("A megadott részleg nem létezik a cégnél")
if len(reszleg)!=0:
    b=max(reszleg)
    for i in lista:
        if b==i.ber and a==i.reszleg:
            print(f"Név: {i.nev}\nNeme: {i.nem}\nBelépés: {i.belepes}\nBér: {(b):,}")
print("7. feladat: Statisztika")
szotar={}
for i in lista:
    szotar[i.reszleg]=szotar.get(i.reszleg,0)+1
for index,i in szotar.items():
    print(f"{index} - {i} fő")
