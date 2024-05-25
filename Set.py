#küme yani set
#setler listeler gibi indexe sahip değildir
#setlerde herhangi bir eleman silinemez
#setlerde eleman ekleme yapamaz
#setlerde eleman silme yapamaz


kume={"Siyah","Beyaz","Yeşil","Mavi","Sari","Rouge","Rose","Vert"}

print(type(kume))#set

#sirasız bir veri yapisina sahiptir.
#yani her yazdirdigimizda karisik gelir

print(kume)

kume.add("Pembe")

print(kume)
kume.discard("Beyaz")

