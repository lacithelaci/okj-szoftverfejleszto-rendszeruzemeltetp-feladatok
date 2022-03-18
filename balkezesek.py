class Bal:
    def __init__(self,nev,elso,utolso,suly,magas):
        self.nev = nev
        self.elso = elso
        self.utolso = utolso
        self.suly = int(suly)
        self.magas = int(magas)
    def __repr__(self):
        return f"{self.nev} {self.elso} {self.utolso} {self.suly} {self.magas}"
    def ev(self):
        return int(self.elso[0:4])
    def ev2(self):
        return int(self.utolso[0:4])
f=open("balkezesek.csv")
elso_sor = f.readline()
lista=[]
for i in f:
    i = i.strip().split(";")
    lista.append(Bal(*i))
print("3. feladat:",len(lista))
print("4. feladat")
for i in lista:
    if i.utolso[0:7]=="1999-10":
        print(f"{i.nev} {round(i.magas*2.54,1)} cm")
print("5. feladat")
bekert=int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
while bekert < 1990 or bekert > 1999:
    bekert = int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
lista2=[i.suly for i in lista if int(i.elso[0:4])<= bekert <= int(i.utolso[0:4])]
print(f"6. feladat: {sum(lista2)/len(lista2):.2f} font")


