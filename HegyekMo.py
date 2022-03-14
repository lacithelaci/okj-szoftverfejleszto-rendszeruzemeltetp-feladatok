class Hegyek:
    def __init__(self,csucs,hegy,magas):
        self.csucs = csucs
        self.hegy = hegy
        self.magas = int(magas)
    def __repr__(self):
        return f"{self.csucs} {self.hegy} {self.magas}"
    def lab(self):
        return self.magas*3.280839895
lista=[]
f=open("hegyekMo.txt",encoding="UTF-8")
elso_sor=f.readline()
for i in f:
    i=i.strip().split(";")
    lista.append(Hegyek(*i))
print(f"3. feladat: Hegycsúcsok száma: {len(lista)} db")
magassag=[i.magas for i in lista]
print(f"4. feladat: Hegycsúcsok átlagos magassága: {sum(magassag)/len(magassag):.2f} m")
print(f"5. feladat A legmagasabb hegycsúcs adatai:")
masz=max(magassag)
for i in lista:
    if masz==i.magas:
        print(f"Név:{i.csucs}\nHegység: {i.hegy}\nMagasság: {masz} m")
print("6. feladat")
b="Börzsöny"
magas=int(input("kérek egy magasságot"))
vege=False
for i in lista:
    if i.hegy==b and magas<i.magas:
        print(f"Van {magas}-nál nagyobb Hegycsúcs a {b}-ben")
        vege=True
        break
if vege==False:
    print(f"Nincs {magas}m-nél nagyobb Hegycsúcs a {b}-ben")
db=0
for i in lista:
    if i.lab()>3000:
        db+=1
print(f"7. feladat: 3000 lábnál magasabb hegycsúcsok száma:",db)
print("8. feladat")
szotar={}
for i in lista:
    szotar[i.hegy]=szotar.get(i.hegy,0)+1
for index,i in szotar.items():
    print(f"{index} - {i}")
print("9. feladat: bukk-videk.txt")
f=open("bukk-videk.txt","w",encoding="UTF-8")
f.write(f"Hegycsúcs neve;Magasság láb")
for i in lista:
    if i.hegy=="Bükk-vidék":
        f.write(f"{i.csucs};{round(i.lab(),2)}\n")