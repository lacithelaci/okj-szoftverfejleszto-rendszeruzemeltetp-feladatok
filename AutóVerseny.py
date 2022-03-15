class Verseny:
    def __init__(self,csapat,versenyzo,eletkor,palya,korido,kor):
        self.csapat = csapat
        self.versenyzo = versenyzo
        self.eletkor = eletkor
        self.palya = palya
        self.korido = korido
        self.kor = int(kor)

    def __repr__(self):
        return f"{self.csapat} {self.versenyzo} {self.eletkor} {self.palya} {self.korido} {self.kor}"
    def ms(self):
        a=self.korido
        return int(a[3:5])*60+int(a[6:8])
lista=[]
f=open("autoverseny.csv",encoding="UTF-8")
e=f.readline()
for i in f:
    i=i.strip().split(";")
    lista.append(Verseny(*i))
print("3. feladat:",len(lista))

for i in lista:
    if i.versenyzo=="Fürge Ferenc" and i.palya=="Gran Prix Circuit" and i.kor==3:
        print("4. feladat:",str(i.ms())+" másodperc")
print("5. feladat")
versenyzo=input("Kérek egy versenyző nevet")
legjobb=[i.ms() for i in lista if i.versenyzo==versenyzo]
if len(legjobb)!=0:
    a=min(legjobb)
    for i in lista:
        if i.versenyzo==versenyzo and i.ms()==a:
            print(f"6. feladat {i.palya} {i.korido}")
            break
else:
    print("Nincs ilyen versenyző az állományban")