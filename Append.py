#append metodu Listenin en SONUNA eleman ekler
#insert metodu indexi verdiğimiz yere ekler
#remove metodu 
#extend listeye birden fazla eleman ekler
#pop metodu listenin en sonundaki elemanı siler ve bize soyler
#reverse metodu listeyi tersinden sıralar
#sort ve sorted metotları sırlama yapar

renkler = ["Siyah","Beyaz","Yeşil","Mavi","Sari","Rouge","Rose","Violet","Vert"]

print(renkler)

renkler.append("Gri")#Listenin en SONUNA Gri ekler

print(renkler)

renkler.insert(0,"Yavruagzi")#0.indexe yavruagzini ekler

print(renkler)

renkler.remove("Sari")#Sari elemanı siler

print(renkler)

renkler2=["Turuncu","Pembe"]

renkler.extend(renkler2)#renkler listesine renkler2 listesini ekler.

print(renkler)

silinen=renkler.pop()

print(silinen)

renkler.reverse()

print(renkler)



