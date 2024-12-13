import os
import pyperclip

# Belirtilen klasör adı
klasor_adi = "code"  # Klasör adını belirtiniz.

# Klasördeki tüm dosyaları al
dosya_listesi = os.listdir(klasor_adi)
txt_dosyalari = [dosya for dosya in dosya_listesi if dosya.endswith('.txt')]

for txt_dosya in txt_dosyalari:
    try:
        dosya_yolu = os.path.join(klasor_adi, txt_dosya)
        
        with open(dosya_yolu, 'r') as onceki_dosya:
            onceki_metin = onceki_dosya.read()

        # Önceden belirlenmiş metin
        prompt1 = "Please compose a Python script that replicates the functionality described above"
        prompt2 = "Please rewrite the provided code to resemble a human-written version"
        prompt3 = "Please refactor the code to enhance its clarity and readability"

        # Önceki metin ile kullanıcıdan alınan metni birleştir
        birlesmis_metin = f"{onceki_metin} {prompt1} "
        print("*************************************")
        print("*************************************")
        print("*************************************")
        print(" V1 Birleştirilmiş metin:")
        print(birlesmis_metin)
        pyperclip.copy(birlesmis_metin)

        yeni_dosya_adi = "v1_" + txt_dosya

      
        print("Python kodunu girin (Çıkmak için 'q' tuşuna basın):")

        kod_satirlari = []
        while True:
            satir = input()
            if satir.strip() == 'q':
                break
            kod_satirlari.append(satir)

        kod = '\n'.join(kod_satirlari)

        kullanici_metni = input("Lütfen bir metin girin: ")

        with open(yeni_dosya_adi, 'w') as yeni_dosya:
            yeni_dosya.write(kod)

        birlesmis_metin = f"{kod} {prompt2} "
        print("*************************************")
        print("*************************************")
        print("*************************************")
        print("V2 Birleştirilmiş metin:")
        print(birlesmis_metin)
        pyperclip.copy(birlesmis_metin)

        yeni_dosya_adi = "v2_" + txt_dosya
        
        print("Python kodunu girin (Çıkmak için 'q' tuşuna basın):")

        kod_satirlari = []
        while True:
            satir = input()
            if satir.strip() == 'q':
                break
            kod_satirlari.append(satir)

        kod = '\n'.join(kod_satirlari)

        kullanici_metni = input("Lütfen bir metin girin: ")

        with open(yeni_dosya_adi, 'w') as yeni_dosya:
            yeni_dosya.write(kod)

        birlesmis_metin = f"{kod} {prompt3} "
        print("*************************************")
        print("*************************************")
        print("*************************************")
        print("V3 Birleştirilmiş metin:")
        print(birlesmis_metin)
        pyperclip.copy(birlesmis_metin)

        yeni_dosya_adi = "v3_" + txt_dosya
        
        print("Python kodunu girin (Çıkmak için 'q' tuşuna basın):")

        kod_satirlari = []
        while True:
            satir = input()
            if satir.strip() == 'q':
                break
            kod_satirlari.append(satir)

        kod = '\n'.join(kod_satirlari)

        kullanici_metni = input("Lütfen bir metin girin: ")

        with open(yeni_dosya_adi, 'w') as yeni_dosya:
            yeni_dosya.write(kod)

        birlesmis_metin = f"{onceki_metin} {prompt2} "
        print("*************************************")
        print("*************************************")
        print("*************************************")
        print("V4 Birleştirilmiş metin:")
        print(birlesmis_metin)
        pyperclip.copy(birlesmis_metin)

        yeni_dosya_adi = "v4_" + txt_dosya
        
        print("Python kodunu girin (Çıkmak için 'q' tuşuna basın):")

        kod_satirlari = []
        while True:
            satir = input()
            if satir.strip() == 'q':
                break
            kod_satirlari.append(satir)

        kod = '\n'.join(kod_satirlari)

        kullanici_metni = input("Lütfen bir metin girin: ")

        with open(yeni_dosya_adi, 'w') as yeni_dosya:
            yeni_dosya.write(kod)

        birlesmis_metin = f"{kod} {prompt3} "
        print("*************************************")
        print("*************************************")
        print("*************************************")
        print("V5 Birleştirilmiş metin:")
        print(birlesmis_metin)
        pyperclip.copy(birlesmis_metin)

        yeni_dosya_adi = "v5_" + txt_dosya
        
        print("Python kodunu girin (Çıkmak için 'q' tuşuna basın):")

        kod_satirlari = []
        while True:
            satir = input()
            if satir.strip() == 'q':
                break
            kod_satirlari.append(satir)

        kod = '\n'.join(kod_satirlari)

        kullanici_metni = input("Lütfen bir metin girin: ")

        with open(yeni_dosya_adi, 'w') as yeni_dosya:
            yeni_dosya.write(kod)

        print(f"{yeni_dosya_adi} adlı dosya başarıyla kaydedildi.")

    except Exception as hata:
        print("Bir hata oluştu:", hata)
