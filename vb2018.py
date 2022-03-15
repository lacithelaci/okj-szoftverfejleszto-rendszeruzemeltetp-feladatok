class VB:
    def __init__(self,varos,nev1,nev2,ferohely):
        self.varos = varos
        self.nev1 = nev1
        self.nev2 = nev2
        self.ferohely = int(ferohely)
    def __repr__(self):
        return f"{self.varos} {self.nev1} {self.nev2} {self.ferohely}"
f=open("vb2018.txt")
lista=[]
ures=f.readline()
for i in f:
    i=i.strip().split(";")
    lista.append(VB(*i))
print(f"3. feladat Stadionok száma: {len(lista)}")
print("4. felada: A legkisebb férőhely:")
szam=[i.ferohely for i in lista]
min=min(szam)
for i in lista:
    if min==i.ferohely:
        print(f"Város: {i.varos}\nStadion neve:{i.nev1}\nFérőhely {min}")
print("5. feladat: Átlagos férőhelyszám :",round(sum(szam)/len(szam),1))
ketnev=[i.nev2 for i in lista if i.nev2!="n.a."]
print(f"6. feladat: 2 néven is ismert stadionok száma: {len(ketnev)}")
print("7. feladat: Kérem a város nevét:")
a=input()
while(len(a)<3):
    a=input()
helyszin=False
for i in lista:
    if a==i.varos:
        helyszin=True
if helyszin:
    print("8. feladat: A megadott város VB helyszín")
else:
    print("8. feladat: A megadott város nem VB helyszín")
a=set()
for i in lista:
    a.add(i.varos)
print(f"9. feladat: {len(a)} különböző városban voltak mérkőzések")
