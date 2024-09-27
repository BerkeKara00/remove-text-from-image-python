# Görsel Üzerinden Metin Silme

Bu projede görsel üzerindeki metinlerin maskeleme yöntemiyle görsel üzerinden silinmesi işlemi gerçekleştiriliyor.
Kullanıcıdan dinamik bir şekilde silmek istediği kelimelerin indeksini ve maskelenecek alanı genişletmek için float bir değer alıyoruz.



### indeks mantığı

İndeks mantığında kullanıcı görseldeki bütün kelimeleri silmek isterse -1 değerini giriyor.
Eğer ki bütün kelimeleri değil de özel olarak silmek istediği kelimeler varsa kelimenin bulunduğu indeksin numarasını girerek o kelimeyi silebiliyor.
Ancak bazı görsellerde görsel içinde fazla resim olduğu zaman bu resimleri de kelime olarak algılayabiliyor bu yüzden indekslerin yeri karışık olabiliyor. Örneğin kullanıcı 0,1 olarak indexleri girdiğinde ilk iki kelimenin silinmesi gerekiyor.Çoğunda bu durum gerçekleşirken bazılarında gerçekleşmiyor. Bu durumda her görsel için ayrı ayrı denemeler yaparak indeksleri bulmak durumunda kalıyoruz. 

![a1.png](Yeniklasor%2Fa1.png)

### Maskeleme alanının genişliği mantığı
Maskeleme alanının genişliği mantığında ise maskelenecek alanın etrafında bir poligon oluşturuyoruz. Orta noktalarını bularak seçilen kelimenin ya da bütün  metinin üzerini maskeyle kapatarak görünmez olmasını sağlıyoruz. Poligonu oluştururken sabit bir scale değeri koyunca bazı resimlerde yazı boyutları farklılığından kelimenin üzeri tam olarak kapanmıyor. Bu durumda kullanıcıdan dinamik olarak bir float değeri alarak maskenin kelimeleri tam olarak kapatabilmesini sağlayabiliyoruz.
Burada göründüğü gibi kelime tam olarak kapanmıyor. Bu yüzden maskeleme genişliği değeri olarak daha yüksek bir değer kullanıyoruz (1.1 gibi).


![a2.png](Yeniklasor%2Fa2.png)


### Kullanıcının girdiği değerler ve çıktı sonucu örnekleri



![img_3.png](Yeniklasor%2Fimg_3.png)
![a4.png](Yeniklasor%2Fa4.png)
![a5.png](Yeniklasor%2Fa5.png)
![a6.png](Yeniklasor%2Fa6.png)



### Verileri "data" klasöründen çekerek "cikti" klasörüne kaydediyoruz.



