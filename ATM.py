giris = ("Bankamıza hoşgeldiniz,\nPARA YATIRMAK için '1' bas\nPARA ÇEKMEK için '2' bas\nBAKİYE SORGULAMAK için '3'bas \nKUR ÇEVİRİCİ için '4'bas \nÇIKIŞ yapmak için '5' basınız")
print(giris)

sonsuzluk = 1

bakiye = 0


while sonsuzluk == 1:
   soru = input ("")

   if soru == "5":
      print("ÇIKIŞ YAPILIYOR... BİZİ TERİCH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ")
      sonsuzluk = 0

   elif soru == "1":
      print("YATIRMAK İSTEDİĞİN TUTARI TUŞLA")
      yatirilan_tutar = int(input())
      bakiye += yatirilan_tutar
      print("BAKİYE EKLEME BAŞARILI")
      print (giris)


   elif soru == "2":
      print("ÇEKMEK İSTEDİĞİN TUTARI TUŞLA")
      cekilen_tutar = int(input())
      bakiye -= cekilen_tutar
      print("PARANIZ HAZIRLANIYOR...")
      print(giris)

   elif soru == "3":
      print(f"Bakiyeniz {bakiye} TL")



