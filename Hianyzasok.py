class Hianyzas:
    def __init__(self,nev,osztaly,elso,utolso,mulasztott):
        self.nev = nev
        self.osztaly = osztaly
        self.elso = int(elso)
        self.utolso = int(utolso)
        self.mulasztott = int(mulasztott)
f=open("szeptember.csv", "r",)
haszontalan_sor=f.readline()
lista=[]
for i in f:
    i=i.strip().split(";")
    lista.append(Hianyzas(*i))
mulasztott_ora=[i.mulasztott for i in lista]
print("2.feladat")
a=sum(mulasztott_ora)
print(f"Összes mulasztott órák száma: {sum(mulasztott_ora)} óra.")
print("3. feladat")
nap=int(input("Kérem adjon meg egy napot:"))
nev=input("Tanuló neve:")
print("4. feladat")
hianyzott=False
for i in lista:
    if i.nev==nev:
        hianyzott=True
if hianyzott:
    print("A tanuló hiányzott szeptemberben")
else:
    print("A tanuló nem hiányzottszeptemberben")
print(f"5. feladat: Hiányzók 2017.09.{nap}-n:")
hianyzok=[]
for i in lista:
    if i.elso==nap:
        hianyzok.append(f"{i.nev} {i.osztaly}")
if len(hianyzok)==0:
    print("Nem volt hiányzó")
else:
    for i in hianyzok:
        print(i)
szotar={}
for i in lista:
    szotar[i.osztaly]=szotar.get(i.osztaly,0)+i.mulasztott
xd=open("osszesites.csv","w",encoding="UTF-8")
for index,i in szotar.items():
    xd.write(f"{index} {i}\n")
