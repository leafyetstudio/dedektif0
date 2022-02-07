import os
import time
import random 
import hashlib
import socket
import sys
import urllib.request
import urllib.parse
os.system("clear")
print(''' \033[91m
     _          _      _    _   _  __ _____ 
    | |        | |    | |  | | (_)/ _|  _  |
  __| | ___  __| | ___| | _| |_ _| |_| |/' |
 / _` |/ _ \/ _` |/ _ \ |/ / __| |  _|  /| |  \033[95m
| (_| |  __/ (_| |  __/   <| |_| | | \ |_/ /
 \__,_|\___|\__,_|\___|_|\_\\__ |_|_|  \___/ 

\033[94m
0-)Çıkış
1-)Ip araçları
2-)Notlar
3-)Kullanıcı adından sosyal medya
4-)Diğer,ek seçenekler
5-)Kriptografi
6-)Sitelerden bilgi topla

''')
dedektif = input("Seçiminizi yapınız > ")
if(dedektif=="0"):
	sys.exit()
if(dedektif=="1"):
	print('''\033[95m
0-)Ana menü
1-)Ip adresinden bilgi topla
2-)Site Ip bul

	''')
	dedektifip = input("Seçiminizi yapınız:")
	if(dedektifip=="1"):
		import urllib.parse
		import urllib.request
		import os
		ip = input("Ip giriniz > ")
		son = ("http://ip-api.com/json/"+ip)
		son2 = ("https://api.iplocation.net/?ip="+ip)
		print("\n SONUÇ: \n")
		urllib.request.urlretrieve(son, "sonuc.json")
		import json
		yazilmis = open("sonuc.json")
		jsonveri = yazilmis.read()
		veriler = json.loads(jsonveri)
		print("Durum: "+veriler["status"])
		print("Ülke: "+veriler["country"])
		print("Ülke Kodu: "+veriler["countryCode"])
		print("Bölge Numarası: "+veriler["region"])
		print("Şehir: "+veriler["city"])
		print("Posta Kodu: "+veriler["zip"])
		print("Saat Dilimi: "+veriler["timezone"])
		print("İnternet Sağlayıcısı: "+veriler["isp"])
		print("Org: "+veriler["org"])
		print("As: "+veriler["as"])
		print("Hedef: "+veriler["query"])
		print("\n ------------------Json verileri------------------ \n \n"+jsonveri)
		os.system("rm -rf sonuc.json")


	elif(dedektifip=="0"):
		os.system("python3 dedektif.py")

	elif(dedektifip=="2"):
		import socket as s
		host = input("Site linki giriniz = ")
		try:
			ip = s.gethostbyname(host)
			print("\033[92m \n Girdiğiniz Sitenin Ip Adresi : "+ip)
		except:
			print("\033[91m \n Hatalı site girdiniz veya da site bulunamadı.Urlyi girerken http/https veya da www yazmayın.Örnek kullanım: ipchat.rf.gd ")
	

elif(dedektif=="2"):
	import os
	notdosya = open("dedektifnot.txt","a")
	print('''\033[94m
          ,,aadd8888888ba,
       .o8P""'         `""Y8o.
     .88"'       _____     `"88.
   .dP'        /~ /   ~\      `Yb.	Merhaba! Dedektif Defterine Hoşgeldiniz! 
  .8P        j' f ,   ~/'       "8.
 .8"         |\  d   7'          "8.	Seçenekler:
.8|          |   H  /|            |8
o8           | \`H / |             8b	0-)Ana menü
88           |   H / |             8)	
88           | \ N   |             8)	1-)Not Ekle
88           |\ `H / |            .8P	
Y8            \  H' /             o8'	2-)Notları Oku
`8|             \H/              a8'	
 `8o             H              a8'	3-)Notları Temizle
   Yb.           H            .od'	
    "8o          V          .dP'
      "V8o,,.          ,,od8"
         ``""YY8888888PP""'
	''')
	notsecim = input("Hangisini Seçiyorsunuz > ")
	
	if(notsecim=="1"):
		notyaz = input("Notunuzu Yazınız > ")
		notdosya.write(notyaz+" \n")
		print("\033[92mNot Ekleme Başarılı")
	elif(notsecim=="0"):
		os.system("python3 dedektif.py")
	elif(notsecim=="2"):
		yazilmis = open("dedektifnot.txt")	
		print("İşte Notlar: \n")
		print("\033[1m")
		print(yazilmis.read())
	elif(notsecim=="3"):
		sil = input("Gerçekten tüm notları silmek istiyor musunuz? e/h ")
		if(sil=="e"):
			notiki = open("dedektifnot.txt","w+")
			notiki.write(" ")
			print("\033[92mNotlar Temizlendi")
		elif(sil=="h"):
			print("İşlem iptal edildi.")
		else:
			print("İşlem iptal edildi.")

	


elif(dedektif=="3"):
	hesapbul = input("\033[93mKullanıcı Adı Giriniz > ")
	print("")
	print("\033[93mFACEBOOK >  ","https://www.facebook.com/"+hesapbul)
	print("")
	print("INSTAGRAM >  ","https://www.instagram.com/"+hesapbul)
	print("")
	print("TWITTER >  ","https://www.twitter.com/"+hesapbul)
	print("")
	print("YOUTUBE >  ","https://www.youtube.com/"+hesapbul)
	print("")
	print("BLOGGER >  ","https://"+hesapbul+".blogspot.com")
	print("")
	print("REDDIT >  ","https://www.reddit.com/user/"+hesapbul)
	print("")
	print("GITHUB >  ","https://www.github.com/"+hesapbul)
	print("")
	print("STEAM >  ","https://steamcommunity.com/id/"+hesapbul)
	print("")
	print("VK >  ","https://vk.com/"+hesapbul)
	print("")
	print("SPOTIFY >  ","https://open.spotify.com/user/"+hesapbul)
	print("")
	print("WATTPAD >  ","https://www.wattpad.com/user/"+hesapbul)
	print("")
	print("WORDPRESS >  ","https://"+hesapbul+".wordpress.com")
	print("")
	print("PINTEREST >  ","https://www.pinterest.com/"+hesapbul)
	print("")
	print("TUMBLR >  ","https://"+hesapbul+".tumblr.com")
	print("")
	print("FLICKR >  ","https://www.flickr.com/people/"+hesapbul)
	print("")
	print("SOUNDCLOUD >  ","https://soundcloud.com/"+hesapbul)
	print("")

elif(dedektif=="4"):
	print('''\033[92m
0-)Ana menü
1-)Avrupa numara kodu sorgula
2-)Dosya içerisinde arama işlemleri (linux)

	''')
	diger = input("Seçiminizi yapınız:")
	if(diger=="1"):
		import phonenumbers
		from phonenumbers import geocoder
		numara = input("Numara giriniz +1xxx şeklinde: ")
		telno = phonenumbers.parse(numara)
		print(geocoder.description_for_number(telno,"tr"))
	if(diger=="0"):
		os.system("python3 dedektif.py")
	if(diger=="2"):
		print("""
1-)Dosyada kelime ile bütünleşen sözcükleri listele
2-)Dosyada cümle ile birlikte kelime bul
3-)Harf duyarsız dosyada kelime ile bütünleşen sözcükleri listele

""")
		dosyaislemleri=input("Seçiminizi giriniz:")
		kelime = input("Hedef kelimeyi giriniz:")
		dosya = input("Arama yapılacak dosya yolu giriniz:")
		if(dosyaislemleri=="1"):
			os.system("grep -i "+kelime+" "+dosya)
		if(dosyaislemleri=="2"):
			os.system("grep -i -n "+kelime+" "+dosya)
		if(dosyaislemleri=="3"):
			os.system("grep "+kelime+" "+dosya)





elif(dedektif=="5"):
	print('''\033[96m
0-)Ana menü
1-)Yazı şifrele
2-)Dosya şifrele
3-)Parola oluşturucu
4-)Dedektografi
	''')
	dedektifkrip = input("Seçiminizi Yapınız:")
	if(dedektifkrip=="1"):
		import hashlib
		import argparse	
		sifreleyici = hashlib.md5()
		sifre2 = hashlib.sha1()
		sifre3 = hashlib.sha224()
		sifre4 = hashlib.sha256()
		sifre5 = hashlib.sha384()
		sifre6 = hashlib.sha512()
		metin = input("Metin Giriniz > ")
		sifreleyici.update(metin.encode("utf-8"))
		cikti = sifreleyici.hexdigest()
		cikti2 = sifre2.hexdigest()
		cikti3= sifre3.hexdigest()
		cikti4 = sifre4.hexdigest()
		cikti5 = sifre5.hexdigest()
		cikti6 = sifre6.hexdigest()
		print(" ")
		print("MD5 > %s" % cikti)
		print(" ")
		print("SHA1 > %s" % cikti2)
		print(" ")
		print("SHA224 > %s" % cikti3)
		print(" ")
		print("SHA256 > %s" % cikti4)
		print(" ")
		print("SHA384 > %s" % cikti5)
		print(" ")
		print("SHA512 > %s" % cikti6)
		print(" ")
	if(dedektifkrip=="0"):
		os.system("python3 dedektif.py")

	if(dedektifkrip=="2"):
		import py_compile
		derle = input("Program Yolunu Giriniz > ")
		py_compile.compile(derle)


	if(dedektifkrip=="3"):
		import random 
		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890.!+-"
		while 1:
			password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
			password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(0,password_uzunluk):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("Senin için oluşturduğum şifre :" , password)


	if(dedektifkrip=="4"):
		import os
		print(''' 
		\33[92m
		  ad8888888888ba
		 dP'         `"8b, 
		 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
		 8  8'd`8           "88baadP""""YbaaadP"""YbdP""Yb
		 8  8 t 8              """        """      ""    8b
		 8  8,0,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
		 8  `"""'       ,d8""     1-Şifrele
		 Yb,         ,ad8"        2-Şifreyi Çöz
		  "Y8888888888P"
		''')
		secim = input("Seçiminizi yapınız > ")
		if(secim=="1"):
			dosyayolu = input("Dosya Yolunu Belirtiniz > ")
			yazilar = open(dosyayolu)
			veri = yazilar.read()
			veri19 = veri.replace("print","5Fg%FaD8++")
	
			veri1 = veri19.replace("import os","^^#294^ert%+'1")
			veri2 = veri1.replace("import socket","+'^'!trweS1a54")
			veri3 = veri2.replace("random.choice","m+^!lkdw%A")
			veri4 = veri3.replace("import random","l(Ed+S'wa^'")
			veri5 = veri4.replace("elif(","%+^i+se/e}0y!ou+^!")
			veri6 = veri5.replace("def","%&dagbfaFFFsaw")
			veri7 = veri6.replace("class","GAGF53DA221")
			veri8 = veri7.replace("else","242BGAD32FEF53")
			veri9 = veri8.replace("import urllib.request","7E6Q-dw!aY^o'")
			veri10 = veri9.replace("input(","1F'dA4^12&")
			veri11 = veri10.replace("float","92324232213")
			veri12 = veri11.replace("os.system","&&76fr}R5")
			veri13 = veri12.replace("import time","\gwalj//2CxZ")
			veri14 = veri13.replace("import requests","*1)92DfH/c")
			veri15 = veri14.replace("except","}23!ERtdaBFV")
			veri16 = veri15.replace("time.sleep","{da^2sda'^da^")
			veri17 = veri16.replace("while True:","-2'!3gf+51")
			veri18 = veri17.replace("for i in range","yU32kL:q")
			veri20 = veri18.replace("<html>","DWM32D3S&%DW")
			veri21 = veri20.replace("</html>","ODW+'2GH")
			veri22 = veri21.replace("<meta","KFE21{ad4")
			veri23 = veri22.replace("<title>","dwm36Uwda")
			veri24 = veri23.replace("</title>","D_DW]D^17W")
			veri25 = veri24.replace("<head>","KD{W/A+Mdw")
			veri26 = veri25.replace("<body>","5232fagw+da'^")
			veri27 = veri26.replace("</body>","LDW21f42nw")
			veri28 = veri27.replace("<p>","GAF32PDW+DLW")
			veri29 = veri28.replace("</p>","K90E2FADW")
			veri30 = veri29.replace("<?php","MDW^AD6TY")
			veri31 = veri30.replace("?>","JDK3dw^1wd")
			veri32 = veri31.replace("<script>","GFA^4dwA")
			veri33 = veri32.replace("</script>","42B24DJ21F")
			veri34 = veri33.replace("<table>","ld-a'L+DA")
			veri35 = veri34.replace("</table>","Kdwa%32VV")
			veri36 = veri35.replace("<div","kLDA^rBaE")
			veri37 = veri36.replace("</div","4$da32^fa")
			veri38 = veri37.replace("<br>","Lda^!ws'")
			veri39 = veri38.replace("<a href","lfDAw22ES+'1")
			veri40 = veri39.replace("</head>","2DfFAFa+3D")

			yazilarson = open("encsuccess.txt","w+")
			yazilarson.write(veri40)
			print("Başarılı,dosya bulunduğunuz dizine oluşturuldu")


		if(secim=="2"):
			dosyayolu = input("Dosya Yolunu Belirtiniz > ")
			yazilar = open(dosyayolu)
			veri = yazilar.read()
			veri19 = veri.replace("5Fg%FaD8++","print")
	
			veri1 = veri19.replace("^^#294^ert%+'1","import os")
			veri2 = veri1.replace("+'^'!trweS1a54","import socket")
			veri3 = veri2.replace("m+^!lkdw%A","random.choice")
			veri4 = veri3.replace("l(Ed+S'wa^'","import random")
			veri5 = veri4.replace("%+^i+se/e}0y!ou+^!","elif(")
			veri6 = veri5.replace("%&dagbfaFFFsaw","def")
			veri7 = veri6.replace("GAGF53DA221","class")
			veri8 = veri7.replace("242BGAD32FEF53","else")
			veri9 = veri8.replace("7E6Q-dw!aY^o'","import urllib.request")
			veri10 = veri9.replace("1F'dA4^12&","input(")
			veri11 = veri10.replace("92324232213","float")
			veri12 = veri11.replace("&&76fr}R5","os.system")
			veri13 = veri12.replace("\gwalj//2CxZ","import time")
			veri14 = veri13.replace("*1)92DfH/c","import requests")
			veri15 = veri14.replace("}23!ERtdaBFV","except")
			veri16 = veri15.replace("{da^2sda'^da^","time.sleep")
			veri17 = veri16.replace("-2'!3gf+51","while True:")
			veri18 = veri17.replace("yU32kL:q","for i in range")
			veri20 = veri18.replace("DWM32D3S&%DW","<html>")
			veri21 = veri20.replace("ODW+'2GH","</html>")
			veri22 = veri21.replace("KFE21{ad4","<meta")
			veri23 = veri22.replace("dwm36Uwda","<title>")
			veri24 = veri23.replace("D_DW]D^17W","</title>")
			veri25 = veri24.replace("KD{W/A+Mdw","<head>")
			veri26 = veri25.replace("5232fagw+da'^","<body>")
			veri27 = veri26.replace("LDW21f42nw","</body>")
			veri28 = veri27.replace("GAF32PDW+DLW","<p>")
			veri29 = veri28.replace("K90E2FADW","</p>")
			veri30 = veri29.replace("MDW^AD6TY","<?php")
			veri31 = veri30.replace("JDK3dw^1wd","?>")
			veri32 = veri31.replace("GFA^4dwA","<script>")
			veri33 = veri32.replace("42B24DJ21F","</script>")
			veri34 = veri33.replace("ld-a'L+DA","<table>")
			veri35 = veri34.replace("Kdwa%32VV","</table>")
			veri36 = veri35.replace("kLDA^rBaE","<div")
			veri37 = veri36.replace("4$da32^fa","</div>")
			veri38 = veri37.replace("Lda^!ws'","<br>")
			veri39 = veri38.replace("lfDAw22ES+'1","<a href")
			veri40 = veri39.replace("2DfFAFa+3D","</head>")

			yazilarson = open("decsuccess.txt","w+")
			yazilarson.write(veri40)
			print("Başarılı,dosya bulunduğunuz dizine oluşturuldu")


elif(dedektif=="6"):
	print('''\033[93m
0-)Ana menü
1-)Hedef sitedeki tüm linkleri ve yönlendirmeleri topla
2-)Hedef sitedeki yazıları topla
3-)Hedef sitedeki resim yollarını ve etiketlerini topla
4-)Site kaynak kodu göster

Not:Sitelerden veri almak için sitenin erişim izni vermesi gerek.
	''')	
	dedektifsite = input("Seçiminizi yapınız:")
	if(dedektifsite=="1"):
		import requests
		from bs4 import BeautifulSoup
		header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Dedektif X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Dedektif0/48.0.2564.116 Zero/537.36'}
		print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
		hedefsite = input("Hedef Url Giriniz: ")
		hedefl = requests.get(hedefsite,headers=header_kod)
		hedefg = hedefl.content
		guzelcorba = BeautifulSoup(hedefg,"html.parser")
		for i in guzelcorba.find_all("a"):
    			print(i)
    			print("\n ################################################################ \n")
	if(dedektifsite=="0"):
		os.system("python3 dedektif.py")
	if(dedektifsite=="4"):
		print("Site Adresini https://google.com şeklinde giriniz")
		site_adresi = input("Site Adresini Giriniz > ")
		html = urllib.request.urlopen(site_adresi)
		print(html.read())
		print("\n\nSİTE KODLARI YUKARIDA\n")
	if(dedektifsite=="2"):
		import requests
		from bs4 import BeautifulSoup
		header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Dedektif X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Dedektif0/48.0.2564.116 Zero/537.36'}
		print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
		hedefsite = input("Hedef Url Giriniz: ")
		hedefl = requests.get(hedefsite,headers=header_kod)
		hedefg = hedefl.content
		guzelcorba = BeautifulSoup(hedefg,"html.parser")
		for i in guzelcorba.find_all("html" and "p"):
    			print(i.text)
    			print("\n ################################################################ \n")

	if(dedektifsite=="3"):
		import requests
		from bs4 import BeautifulSoup
		header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Dedektif X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Dedektif0/48.0.2564.116 Zero/537.36'}
		print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
		hedefsite = input("Hedef Url Giriniz: ")
		hedefl = requests.get(hedefsite,headers=header_kod)
		hedefg = hedefl.content
		guzelcorba = BeautifulSoup(hedefg,"html.parser")
		for i in guzelcorba.find_all("img"):
    			print(i)
    			print("\n ################################################################ \n")