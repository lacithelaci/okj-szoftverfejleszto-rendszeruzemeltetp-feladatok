class Snooker:
    def __init__(self,hely,nev,orszag,nyeremeny):
        self.hely = hely
        self.nev = nev
        self.orszag = orszag
        self.nyeremeny = int(nyeremeny)
    def __repr__(self):
        return f"{self.hely} {self.nev} {self.orszag} {self.nyeremeny}"
lista=[]
f=open("snooker.txt")
elso=f.readline()
for i in f:
    i=i.strip().split(";")
    lista.append(Snooker(*i))
print(f"3. feladat: A világranglistán {len(lista)} versenyző szerepel")
nyert=[i.nyeremeny for i in lista]
print(f"4. feladat: A versenyzők átlagos {sum(nyert)/len(nyert):.2f} fontot kerestek")
print("5. feladat")
kina=[i.nyeremeny for i in lista if i.orszag=="Kína"]
max=max(kina)
for i in lista:
    if i.orszag=="Kína" and max==i.nyeremeny:
        print(f"\tHelyezes: {i.hely}\n\tNév: {i.nev}\n\tOrszág: {i.orszag}\n\tNyeremény: {i.nyeremeny*380:,} Ft")
norveg=False
for i in lista:
    if i.orszag=="Norvégia":
        norveg=True
if norveg:
    print("6. feladat: A versenyzők között van norvég versenyző")
else:
    print("6. feladat: A versenyzők között nincs norvég versenyző")
print("7. feladat: Statisztika")
szotar={}
for i in lista:
    szotar[i.orszag]=szotar.get(i.orszag,0)+1
for index,i in szotar.items():
    if i>4:
        print(f"\t{index} - {i} fő")