import time
import random
import math

class Bilgisayar():
    def __init__(self,pcdurumu="Kapalı",işletim_sistemi=["windows10"],model="dell",uygulamalar = ["Google Chrome","Opera","The Witcher 3:WildHunt"]):
        self.pcdurumu=pcdurumu
        self.işletim_sistemi=işletim_sistemi
        self.model=model
        self.uygulamalar=uygulamalar
    def açma(self):
        if(self.pcdurumu=="Açık"):
            print("bilgisiyar zaten açık...")
            time.sleep(1)
        else:
            print("bilgisiyar açılıyor...")
            time.sleep(1)
            self.pcdurumu="Açık"
            print("Bilgisiyar açıldı...")
    def kapatma(self):
        if(self.pcdurumu=="Kapalı"):
            print("Pc zaten kapalı")
        else:
            print("Bilgisiyar kapatılıyor...")
            time.sleep(1)
            self.pcdurumu="Kapalı"
            print("Bilgisiyar kapatıldı...")
    def hesap_makinesi(self):
        if (self.pcdurumu == "Açık" or self.pcdurumu == "açık"):
            print("""****************************************
            HESAP MAKİNESİv2.5
            ****************************************
            İŞLEMLER
            ****************************************
            1 = TOPLAMA
            2 = ÇIKARMA
            3 = ÇARPMA
            4 = BÖLME
            5 = FAKTÖRİYEL ALMA
            6 = ÜS ALMA
            7 = KAREKÖK BULMA
            ****************************************""")
            işlem=input("işlem giriniz:")
            toplama=0
            if(işlem=="1"):
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayıların toplamı:{}".format(sayi1+sayi2))
            elif(işlem=="2"):
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayıların farkı:{}".format(sayi1-sayi2))
            elif (işlem == "3"):
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayıların çarpımı:{}".format(sayi1 * sayi2))
            elif (işlem == "4"):
                sayi1 = int(input("Sayı Giriniz:"))
                sayi2 = int(input("Sayı Giriniz"))
                print("Sayıların bölümü:{}".format(sayi1 / sayi2))
            elif (işlem == "5"):
                sayi1 = int(input("Sayı Giriniz:"))
                print("{} sayısının faktoriyeli:{}".format(sayi1,math.factorial(sayi1)))
            elif (işlem == "6"):
                sayi1 = int(input("Sayı Giriniz:"))
                üs=int(input("alınacak üssü giriniz"))
                print("{} sayısının üssü:{} dir.".format(sayi1,sayi1**üs))
            elif (işlem == "7"):
                sayi1 = int(input("Sayı Giriniz:"))
                karakök=sayi1**0.5
                print("{} sayisinin karakökü:{}".format(karakök))
            else:
                print("invalid value")
        else:
            print("lütfen bilgisiyarınızı açınız")
    def sayi_tahmin_oyunu(self):
        if(self.pcdurumu == "Açık" or self.pcdurumu == "açık"):
            sayi1 = int(input("Sayı Giriniz:"))
            sayi2 = int(input("Sayı Giriniz"))
            print("Sayı aralığımız:{}-{} dir.".format(sayi1,sayi2))
            print("Rastgele sayı seçiliyor...")
            rastgele_sayı=random.randint(sayi1,sayi2)
            print("Sayı seçildi good luck :)")
            print("5 -Tahmin hakkınız var...")
            while True:
                hak=5
                tahmin=int(input("Tahmninizi giriniz:"))
                if tahmin < rastgele_sayı:
                    print("Yanlış Tahmin :)")
                    print("Bence Daha Büyük Bir Sayı Yazmanız Haklarınız Korumanıza Yardımcı Olacaktır:)")
                    hak -= 1
                    print("Kalan Hakkınız:{}".format(hak))
                elif tahmin > rastgele_sayı:
                    print("Yanlış Tahmin Bu İşte Yenisiniz Sanırım :)")
                    print("Sizce de Sayı Fazla Büyük Değil Mi ?")
                    hak -= 1
                    print("Kalan Hakkınız:{}".format(hak))
                elif tahmin == rastgele_sayı:
                    print("Doğru Tahmin!!")
                    print("Talimatlarımla Başardınız Efendim :)")
                    break
                elif hak == 1:
                    print("Son Hakkınız Kaldı Biraz Dikkatli Olun Derim :) ")
                elif hak == 0:
                    print("Dikkatli Olun Demiştim Hakkınız Kalmadı :)))")
                    print("Oyun Kapatılıyor...")
                    time.sleep(1)
                    print("Oyun Kapatıldı")
                    break
        else:
            print("bilgisiyarınızı açınız..")
    def __len__(self):
        return len(self.işletim_sistemi)
    def __str__(self):
        return """
                Bilgisiyar özellikleri
                model:{}
                işletim sistemi:{}
                pc durumu:{}
                uygulama listesi:{}
                ...................""".format(self.model,self.işletim_sistemi,self.pcdurumu,self.uygulamalar)
    def işletim_sistemi_kaldır(self):
        if (self.pcdurumu == "Açık" or self.pcdurumu == "açık"):
            if(len(self.işletim_sistemi)==1):
                print("Mevcut İşletim Sistemi = {}".format(self.işletim_sistemi[0]))
                işlem = input("İşletim Sisteminizi Kaldırmak İstiyor musunuz?:")
                if(işlem == "Evet" or işlem == "evet"):
                    print("{} Kaldırılıyor Lütfen Bekleyiniz...".format(self.işletim_sistemi[0]))
                    time.sleep(2)
                    self.işletim_sistemi.pop(0)
                    print("Mevcut İşletim Sisteminiz Kaldırıldı Yeni Bir İşletim Sistemi İçin 'İşletim Sistemi Yükle' Seçeneğini Seçebilirsiniz.")
                elif(işlem == "Hayır" or işlem == "hayır"):
                    print("Çıkış Yapılıyor...")
                    time.sleep(1)
                    print("Çıkış Yapıldı.")
                else:
                    print("Geçersiz işlem")
            else:
                print("herhangi bir işletim sistemi bulunamadı...")
        else:
            print("Bilgisayar Kapalı İşlem Yapmak İçin Lütfen Açınız")
    def işletim_sistemi_yükle(self):
        if(self.pcdurumu == "açık" or self.pcdurumu == "Açık"):
            if self.işletim_sistemi == list():
                seçim = input(" Bir Tane işletim sistemi Edinmek İster misiniz?:")
                if(seçim=="Evet" or seçim=="evet"):
                    işletim_sistemleri=["Mac","windows 7","SteamOS","linux"]
                    print("yüklenebilecek işletim sistemleri:")
                sayac=0
                for i in işletim_sistemleri:
                    print("Numara:{}|işletim sistemi:{}".format(sayac,i))
                    sayac+=1
                işlem=input("lütfen yüklemek istediğiniz işletim sisteminin numarasını giriniz:")
                if(işlem=="0"):
                    print("{} yükleniyor lütfen bekleyiniz..".format(işletim_sistemleri[0]))
                    time.sleep(1)
                    self.işletim_sistemi.append("Mac")
                    print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletim_sistemleri[0],self.işletim_sistemi[0]))
                if(işlem=="1"):
                    print("{} yükleniyor lütfen bekleyiniz..".format(işletim_sistemleri[1]))
                    time.sleep(1)
                    self.işletim_sistemi.append("windows 7")
                    print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletim_sistemleri[1],self.işletim_sistemi[1]))
                if(işlem=="2"):
                    print("{} yükleniyor lütfen bekleyiniz..".format(işletim_sistemleri[2]))
                    time.sleep(1)
                    self.işletim_sistemi.append("SteamOS")
                    print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletim_sistemleri[2],self.işletim_sistemi[2]))
                if(işlem=="3"):
                    print("{} yükleniyor lütfen bekleyiniz..".format(işletim_sistemleri[3]))
                    time.sleep(1)
                    self.işletim_sistemi.append("linux")
                    print("{} Başarıyla Yüklendi\nMevcut İşletim Sisteminiz:{}".format(işletim_sistemleri[3],self.işletim_sistemi[3]))
            elif(len(self.işletim_sistemi)>0):
                print("Zaten Bir İşletim Sisteminiz Bulunmakta Yenisini Kurmak İçin Mevcut Olanı Kaldırmanız Gerek")
                print("Programdan Çıkış Yapılıyor...")
                time.sleep(1)
                print("Çıkış Yapıldı.")
        else:
            print("bu işlem için bilgisiyarınızın açık olması gerekmektedir.")
    def bilgilerimi_göster(self):
        if self.pcdurumu == "Açık" or self.pcdurumu == "açık":
            print(
                "---------------------------\nBilgisayar Özellikleri\n---------------------------\nModel:{}\nİşletim Sistemi:{}\nPc Durumu:{}\nUygulama Listesi{}\n---------------------------".format(
                    self.model, self.işletim_sistemi, self.pcdurumu, self.uygulamalar))
        else:
            print("bu işlem için bilgisiyarınızın açık olması gerekmektedir.")
bilgisayar=Bilgisayar()
print("""-----------------------------------------
    Bilgisayar İşlemleri
    -----------------------------------------
    1 = AÇMA
    2 = KAPAMA
    3 = HESAP MAKİNESİ
    4 = BİLGİLER
    5 = İŞLETİM SİSTEMİ  KALDIR
    6 = İŞLETİM SİSTEMİ YÜKLE
    7 = SAYI TAHMİN OYUNU
    -----------------------------------------""")
while True:
    karar = input("İşlem Giriniz:")
    if(karar == "1"):
        bilgisayar.açma()
    elif(karar == "2"):
        bilgisayar.kapatma()
    elif(karar == "3"):
        bilgisayar.hesap_makinesi()
    elif(karar == "4"):
        bilgisayar.bilgilerimi_göster()
    elif(karar == "5"):
        bilgisayar.işletim_sistemi_kaldır()
    elif(karar == "6"):
        bilgisayar.işletim_sistemi_yükle()
    elif(karar == "7"):
        bilgisayar.sayi_tahmin_oyunu()
    elif(karar == "q"):
        print("Bilgisayar Durduruluyor...")
        break
    else:
        print("Geçersiz İşlem Girildi")














