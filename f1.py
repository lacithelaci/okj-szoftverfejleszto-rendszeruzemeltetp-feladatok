#Készítette Szemán László
#idő: 00:16:40
class Kosar():
    def __init__(self,hazai,idegen,hpont,vpont,helyszin,ido):
        self.hazai = hazai
        self.idegen = idegen
        self.hpont = hpont
        self.vpont = vpont
        self.helyszin = helyszin
        self.ido = ido
    def __repr__(self):
        return f"{self.hazai} {self.idegen} {self.hpont} {self.vpont} {self.helyszin} {self.ido}"
lista= []
f=open("eredmenyek.txt",encoding="UTF-8")
for xd,i in enumerate(f):
    if xd!=0:
        i=i.strip().split(";")
        lista.append(Kosar(*i))
print(lista)
print("3. feladat:",end=" ")
a="Real Madrid"
hm=0
vm=0
for i in lista:
    if i.hazai==a:
        hm+=1
    if i.idegen==a:
        vm+=1
print(f"{a} hazai: {hm} vendég: {vm} ")
print("4. feladat: Volt döntetlen?",end=" ")
dontetlen=False
for i in lista:
    if i.vpont==i.hpont:
        dontetlen=True
if dontetlen:
    print("volt")
else:
    print("nem ")
b="Barcelona"
for i in lista:
    if i.hazai.count(b):
        b=i.hazai
print(f"5. feladat: barcelonai csapat neve: {b}")
print("6. feladat:")
a="2004-11-21"
for i in lista:
    if i.ido==a:
        print(f"{i.hazai}-{i.idegen} ({i.hpont}:{i.vpont})")
print("7.feladat:")
szotar={}
for i in lista:
    szotar[i.helyszin]=szotar.get(i.helyszin,0)+1
for xd,i in szotar.items():
    if i>=20:
        print(f"{xd}: {i}")