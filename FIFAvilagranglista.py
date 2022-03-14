class Fifa:
    def __init__(self,csapat,hely,valtozas,pont):
        self.csapat = csapat
        self.hely = hely
        self.valtozas = int(valtozas)
        self.pont = int(pont)
    def __repr__(self):
        return f"{self.csapat} {self.hely} {self.valtozas} {self.pont}"
f=open("fifa.txt",encoding="UTF-8")
elso_sor=f.readline()
lista=[]
for i in f:
    i=i.strip().split(";")
    lista.append(Fifa(*i))
print(f"3. feladat: A listán {len(lista)} csapat szerepel")
pontok=[i.pont for i in lista]
print(f"4. feladat: {sum(pontok)/len(pontok):.2f} pont")
print("5. feladat: A legtöbbet javító csapat: ")
javitas=[i.valtozas for i in lista]
maxvaltozas=max(javitas)
for i in lista:
    if maxvaltozas==i.valtozas:
        print(f"Helyezés: {i.hely}\nCsapat: {i.csapat}\nPontszám: {i.pont}")
print("6. feladat:",end=" ")
van2="nincs"
for i in lista:
    if i.csapat=="Magyarország":
        van2="van"
print(f"A csapatok között {van2} Magyarország")
print("7. feladat: Statisztika")
szotar={}
for i in lista:
    szotar[i.valtozas]=szotar.get(i.valtozas,0)+1
for index,i in szotar.items():
    if i>1:
        print(f"{index} helyet változott csapat: {i} csapat")