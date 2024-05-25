#min, max ve in kullanımı 
#sum ve kullanımı
#for döngüsü ile listeyi yazdırmak 
#enumerate
#listeyi stringe çevirmek ve join metodu
#stringi listeye çevirmek ve split metodu
renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

sayilar=[1,2,5,17,19,23,95]

print(min(sayilar))#min en kucuk max en buyuk sayiyi verir

#fakat Strin listede min yada max yaparsak
#alfabetik olarak en ileri yada en geriyi verir

print(max(renkler))

print(sum(sayilar))#listedeki sayilari toplar

for renk in renkler:
    print(renk)
    #teker teker renkleri yazdirir
    
    #enumarate listeyi numaralandirmaya yarar
print(list(enumerate(renkler)))

#eger sifirdan değilde 3. indexten başlamasını istersek

print(list(enumerate(renkler,start=2)))

print("Siyah" in renkler) #siyah renkler listesinde var mı

print("Siyah" not in renkler)#yok mu

stringrenkler="".join(renkler)

print(stringrenkler)

stringrenkler="--".join(renkler)

print(type(stringrenkler))

print(stringrenkler)

renkler2=stringrenkler.split("--")

print(renkler2)

    
