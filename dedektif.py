import os
import time
import random 
import hashlib
import socket
import urllib.request
import urllib.parse
os.system("clear")
print(''' \033[94m


            .-.____________________.-.
     ___ _.' .-----.    _____________|
    /_._/   (      |   /_____________|
      /      `  _ ____/     
     |_      .\(  ||           
    .'  `-._/__`_//        _      _            _   _            _____ 
  .'       |              | |    | |          | | (_)          |  _  |
 /        / 		__| | ___| |_ ___  ___| |_ ___   _____ | |/' | \033[91m
/        | 	       / _` |/ _ \ __/ _ \/ __| __| \ \ / / _ \|  /| | 
|        '   	      | (_| |  __/ ||  __/ (__| |_| |\ V /  __/\ |_/ /
|         \	       \__,_|\___|\__\___|\___|\__|_| \_/ \___| \___/ 	               
`-._____.-'

\033[95m    		Yapımcılar:Sexettin&Furkan Kerem

\033[91m
1-)Ip araçları
2-)Notlar
3-)Kullanıcı adından sosyal medya
4-)Diğer,ek seçenekler
5-)Kriptografi
6-)Sitelerden bilgi topla

''')
dedektif = input("Seçiminizi yapınız > ")
if(dedektif=="1"):
	print('''
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
		os.system("cat sonuc.json")
		os.system("rm -rf sonuc.json")




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
	notdosya = open("xsnot.txt","a")
	print('''\033[94m
          ,,aadd8888888ba,
       .o8P""'         `""Y8o.
     .88"'       _____     `"88.
   .dP'        /~ /   ~\      `Yb.	Merhaba! Dedektif Defterine Hoşgeldiniz! (xsnot)
  .8P        j' f ,   ~/'       "8.
 .8"         |\  d   7'          "8.	Seçenekler:
.8|          |   H  /|            |8
o8           | \`H / |             8b
88           |   H / |             8)	1-)Not Ekle
88           | \ N   |             8)
88           |\ `H / |            .8P	2-)Notları Oku
Y8            \  H' /             o8'
`8|             \H/              a8'	3-)Notları Temizle
 `8o             H              a8'
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
	elif(notsecim=="2"):
		yazilmis = open("xsnot.txt")	
		print("İşte Notlar: \n")
		print("\033[1m")
		print(yazilmis.read())
	elif(notsecim=="3"):
		sil = input("Gerçekten tüm notları silmek istiyor musunuz? e/h ")
		if(sil=="e"):
			notiki = open("xsnot.txt","w+")
			notiki.write(" ")
			print("\033[92mNotlar Temizlendi")
		elif(sil=="h"):
			print("İşlem iptal edildi.")
		else:
			print("İşlem iptal edildi.")
	else:
		print("\033[91mYanlış seçim,program tekrar başlatılıyor...")
		os.system("python3 xsnot.py")
	


elif(dedektif=="3"):
	hesapbul = input("Kullanıcı Adı Giriniz > ")
	print("")
	print("\033[92mFACEBOOK >  ","https://www.facebook.com/"+hesapbul)
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
	print('''

1-)Tc son 2 hane bul
2-)Telefon numarasından şehir bul (TRde demo)

	''')
	diger = input("Seçiminizi yapınız:")
	if(diger=="1"):
		tcno = input("TC Kimlik No İlk 9 Hanesini Giriniz: ")
		a, b, toplamDokuz = 0, 0, 0
		for i in range(9):
		    toplamDokuz = toplamDokuz+int(tcno[i])
		    if i%2 == 0:
		        a = a+7*int(tcno[i])
		    elif i%2 == 1:
		        b = b+int(tcno[i])
		    if i == 8:
		        haneOn = (a-b)%10
		        haneOnBir = (haneOn+toplamDokuz)%10
		        print(tcno+str(haneOn)+str(haneOnBir))

	elif(diger=="2"):
		import phonenumbers
		from phonenumbers import geocoder
		numara = input("Numara giriniz +90xxx şeklinde: ")
		telno = phonenumbers.parse(numara)
		print(geocoder.description_for_number(telno,"tr"))


elif(dedektif=="5"):
	print('''
1-)Yazı şifrele
2-)Md5 Hash cracker (brute)
3-)Dosya şifrele
4-)Zip şifre kırıcı
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

	if(dedektifkrip=="3"):
		import py_compile
		derle = input("Program Yolunu Giriniz > ")
		py_compile.compile(derle)

	if(dedektifkrip=="2"):
		wlist = input("Wordlist dizini ve adını giriniz: ")
		hcrack = input("Md5 giriniz: ")
	
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içinden bulunamadı")
	if(dedektifkrip=="4"):
		print("\033[92m")
		os.system("clear")
		print('''
     .--------.
    / .------. 
   | |        
  _| |________| |_
.' |_|        |_| '. Wordlistiniz var mı? 
'._____ ____ _____.'
|     .'____'.     | (Yok seçeneği işaretlenirse program sizin için oluşturacak)
'.__.'.'    '.'.__.'
'.__  |Zero00|  __.| 1-) Wordlistim var
|   '.'.____.'.'   | 
'.____'.____.'____.' 2-) Wordlistim yok
'.________________.'


		''')
		aaaas = input("Seç > ")

		if(aaaas=="2"):
			import random 
			import pyzipper
			import os
		
			chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")

			password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
			password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(0,password_uzunluk):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				#print(password)
				passworda = (password+"\n")
				dosya = open("wlist.txt","a")
				dosya.write(passworda)


			wordlist = ("wlist.txt")

			file = input("Zip dosya yolunu belirtiniz > ")	
			icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")
	
			fileobject = pyzipper.AESZipFile(file)

			with open(wordlist,"rb") as wordlist:
				for word in wordlist:
					try:
						fileobject.pwd = word.strip()
						fileobject.read(icdosya)
					except:
						print("\033[93mŞifre denendi = ",word.decode().strip())
						continue
					else:
						print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
						os.system("rm -rf wlist.txt")
						exit(0)
				
			os.system("rm -rf wlist.txt")
			print("\033[91mŞifre Bulunamadı")

		elif(aaaas=="1"):
			import pyzipper
			import os
			os.system("pip install pyzipper")
			wordlist = input("Wordlist Yolunu Belirtiniz > ")

			file = input("Zip dosya yolunu belirtiniz > ")	
			icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")

			fileobject = pyzipper.AESZipFile(file)

			with open(wordlist,"rb") as wordlist:
				for word in wordlist:
					try:
						fileobject.pwd = word.strip()
						fileobject.read(icdosya)
					except:
						print("\033[93mŞifre denendi = ",word.decode().strip())
						continue
					else:
						print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
						exit(0)
			print("\033[91mŞifre Bulunamadı")


elif(dedektif=="6"):
	print('''
1-)Sitedeki tüm linkleri çek

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


