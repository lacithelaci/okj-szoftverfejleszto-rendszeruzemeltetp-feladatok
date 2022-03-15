class Eu:
    def __init__(self,orszag,datum):
        self.orszag = orszag
        self.datum = datum
    def __repr__(self):
        return f"{self.orszag} {self.datum}"
    def csatlakozas(self):
        a=self.datum
        return int(a[0:4])
    def honap(self):
        a=self.datum
        return a[5:7]
f=open("EUcsatlakozas.txt")
lista=[]
for i in f:
    i=i.strip().split(";")
    lista.append(Eu(*i))
print(f"3. feladat: EU tagállamainak száma: {len(lista)} db")
db=0
for i in lista:
    if i.csatlakozas()==2007:
        db+=1
print(f"4. feladat: 2007-ben {db} ország csatlakozott.")
for i in lista:
    if i.orszag=="Magyarország":
        print("5. feladat: Magyarország csatlakozásának dátuma:",i.datum)
majus="nem volt"
for i in lista:
    if i.honap()=="05":
        majus="volt"
print(f"6. feladat: Májusban {majus} csatlakozás!")
lista=sorted(lista,key=lambda i:i.datum)
print("7. feladat: Legutoljára csatlakozott ország: "+lista[-1].orszag)
print("8. feladat: Statisztika")
halmaz=set()
for i in lista:
    halmaz.add(i.csatlakozas())
for i in halmaz:
    db=0
    for j in lista:
        if i==j.csatlakozas():
            db+=1
    print(f"\t{i} - {db} ország")
