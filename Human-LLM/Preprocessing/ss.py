"""
#2li
import os
from PIL import Image, ImageDraw, ImageFont

def koddan_kutuphaneleri_cikar(kod_yolu):
    try:
        with open(kod_yolu, 'r') as dosya:
            kod_satirlari = dosya.readlines()
    except Exception as e:
        print(f"Hata: {e}")
        return []

    yeni_kod_satirlari = []
    for satir in kod_satirlari:
        satir = satir.rstrip()
        if not satir or satir.startswith("import") or satir.startswith("from"):
            continue
        yeni_kod_satirlari.append(satir.expandtabs(4))

    return yeni_kod_satirlari

def ekran_goruntusu_al(kod_klasoru, goruntu_klasoru):
    if not os.path.exists(goruntu_klasoru):
        os.makedirs(goruntu_klasoru)
    font = ImageFont.truetype("times.ttf", 50)
    for klasor in os.listdir(kod_klasoru):
        klasor_yolu = os.path.join(kod_klasoru, klasor)
        
        if os.path.isdir(klasor_yolu):  # Eğer klasör ise
            out_klasor_adi = klasor + "_out"
            out_klasor_yolu = os.path.join(goruntu_klasoru, out_klasor_adi)
            os.makedirs(out_klasor_yolu, exist_ok=True)  # Klasörü oluştur veya varsa geç
            
            for dosya in os.listdir(klasor_yolu):
                if dosya.endswith(".py"):  # Eğer dosya .py uzantılı ise
                    kod_yolu = os.path.join(klasor_yolu, dosya)
                    kod = koddan_kutuphaneleri_cikar(kod_yolu)
                    if not kod:
                        continue

                    kod_metni = '\n'.join(kod)

                    # Kodu iki parçaya böl
                    kod_satir_sayisi = len(kod)
                    bolme_noktasi = min(kod_satir_sayisi, 67)  # İlk 62 satırı al, ancak kod 62 satırdan kısa ise tüm kodu al
                    kod_metni_bol1 = '\n'.join(kod[:bolme_noktasi])
                    kod_metni_bol2 = '\n'.join(kod[bolme_noktasi:])

                    # Sol tarafta göstermek için görüntü oluştur
                    img1 = Image.new('RGB', (1600, 1600), color=(255, 255, 255))
                    d1 = ImageDraw.Draw(img1)
                    d1.text((0, 0), kod_metni_bol1, fill=(0, 0, 0), font=font)

                    # Birleştirilmiş görüntü oluştur
                    combined_img = Image.new('RGB', (1600, 1600), color=(255, 255, 255))

                    # Sol taraftaki görüntüyü birleştirilmiş görüntüye ekle
                    combined_img.paste(img1, (0, 0))


                    # Görüntüyü kaydet
                    goruntu_adi = os.path.splitext(dosya)[0] + ".png"
                    goruntu_yolu = os.path.join(out_klasor_yolu, goruntu_adi)
                    try:
                        combined_img.save(goruntu_yolu)
                    except Exception as e:
                        print(f"Hata: {e}\n {goruntu_yolu}")

if __name__ == "__main__":
    kod_klasoru = "in"
    goruntu_klasoru = "out"
    ekran_goruntusu_al(kod_klasoru, goruntu_klasoru)

"""
"""
#2li
import os
from PIL import Image, ImageDraw, ImageFont

def koddan_kutuphaneleri_cikar(kod_yolu):
    try:
        with open(kod_yolu, 'r') as dosya:
            kod_satirlari = dosya.readlines()
    except Exception as e:
        print(f"Hata: {e}")
        return []

    yeni_kod_satirlari = []
    for satir in kod_satirlari:
        satir = satir.rstrip()
        if not satir or satir.startswith("import") or satir.startswith("from"):
            continue
        yeni_kod_satirlari.append(satir.expandtabs(4))

    return yeni_kod_satirlari

def ekran_goruntusu_al(kod_klasoru, goruntu_klasoru):
    if not os.path.exists(goruntu_klasoru):
        os.makedirs(goruntu_klasoru)
    font = ImageFont.truetype("times.ttf", 8)
    for klasor in os.listdir(kod_klasoru):
        klasor_yolu = os.path.join(kod_klasoru, klasor)
        
        if os.path.isdir(klasor_yolu):  # Eğer klasör ise
            out_klasor_adi = klasor + "_out"
            out_klasor_yolu = os.path.join(goruntu_klasoru, out_klasor_adi)
            os.makedirs(out_klasor_yolu, exist_ok=True)  # Klasörü oluştur veya varsa geç
            
            for dosya in os.listdir(klasor_yolu):
                if dosya.endswith(".py"):  # Eğer dosya .py uzantılı ise
                    kod_yolu = os.path.join(klasor_yolu, dosya)
                    kod = koddan_kutuphaneleri_cikar(kod_yolu)
                    if not kod:
                        continue

                    kod_metni = '\n'.join(kod)

                    # Kodu iki parçaya böl
                    kod_satir_sayisi = len(kod)
                    bolme_noktasi = min(kod_satir_sayisi, 67)  # İlk 62 satırı al, ancak kod 62 satırdan kısa ise tüm kodu al
                    kod_metni_bol1 = '\n'.join(kod[:bolme_noktasi])
                    kod_metni_bol2 = '\n'.join(kod[bolme_noktasi:])

                    # Sol tarafta göstermek için görüntü oluştur
                    img1 = Image.new('RGB', (400, 800), color=(255, 255, 255))
                    d1 = ImageDraw.Draw(img1)
                    d1.text((0, 0), kod_metni_bol1, fill=(0, 0, 0), font=font)

                    # Sağ tarafta göstermek için görüntü oluştur
                    img2 = Image.new('RGB', (400, 800), color=(255, 255, 255))
                    d2 = ImageDraw.Draw(img2)
                    d2.text((0, 0), kod_metni_bol2, fill=(0, 0, 0), font=font)

                    # Birleştirilmiş görüntü oluştur
                    combined_img = Image.new('RGB', (800, 800), color=(255, 255, 255))

                    # Sol taraftaki görüntüyü birleştirilmiş görüntüye ekle
                    combined_img.paste(img1, (0, 0))

                    # Sağ taraftaki görüntüyü birleştirilmiş görüntüye ekle
                    combined_img.paste(img2, (400, 0))

                    # Görüntüyü kaydet
                    goruntu_adi = os.path.splitext(dosya)[0] + ".png"
                    goruntu_yolu = os.path.join(out_klasor_yolu, goruntu_adi)
                    try:
                        combined_img.save(goruntu_yolu)
                    except Exception as e:
                        print(f"Hata: {e}")

if __name__ == "__main__":
    kod_klasoru = "in"
    goruntu_klasoru = "out"
    ekran_goruntusu_al(kod_klasoru, goruntu_klasoru)
"""
"""
#3lu

import os
from PIL import Image, ImageDraw, ImageFont

def koddan_kutuphaneleri_cikar(kod_yolu):
    try:
        with open(kod_yolu, 'r') as dosya:
            kod_satirlari = dosya.readlines()
    except Exception as e:
        print(f"Hata: {e}")
        return []

    yeni_kod_satirlari = []
    for satir in kod_satirlari:
        satir = satir.rstrip()
        if not satir or satir.startswith("import") or satir.startswith("from"):
            continue
        yeni_kod_satirlari.append(satir.expandtabs(4))

    return yeni_kod_satirlari

def ekran_goruntusu_al(kod_klasoru, goruntu_klasoru):
    if not os.path.exists(goruntu_klasoru):
        os.makedirs(goruntu_klasoru)
    font = ImageFont.truetype("times.ttf", 8)
    for klasor in os.listdir(kod_klasoru):
        klasor_yolu = os.path.join(kod_klasoru, klasor)
        
        if os.path.isdir(klasor_yolu):  # Eğer klasör ise
            out_klasor_adi = klasor + "_out"
            out_klasor_yolu = os.path.join(goruntu_klasoru, out_klasor_adi)
            os.makedirs(out_klasor_yolu, exist_ok=True)  # Klasörü oluştur veya varsa geç
            
            for dosya in os.listdir(klasor_yolu):
                if dosya.endswith(".py"):  # Eğer dosya .py uzantılı ise
                    kod_yolu = os.path.join(klasor_yolu, dosya)
                    kod = koddan_kutuphaneleri_cikar(kod_yolu)
                    if not kod:
                        continue

                    kod_metni = '\n'.join(kod)

                    # Kodu iki parçaya böl
                    kod_satir_sayisi = len(kod)
                    bolme_noktasi = min(kod_satir_sayisi, 100)  # İlk 62 satırı al, ancak kod 62 satırdan kısa ise tüm kodu al
                    kod_metni_bol1 = '\n'.join(kod[:bolme_noktasi])
                    kod_metni_bol2 = '\n'.join(kod[bolme_noktasi:bolme_noktasi*2])
                    kod_metni_bol3 = '\n'.join(kod[bolme_noktasi*2:])

                    # Sol tarafta göstermek için görüntü oluştur
                    img1 = Image.new('RGB', (400, 1200), color=(255, 255, 255))
                    d1 = ImageDraw.Draw(img1)
                    d1.text((0, 0), kod_metni_bol1, fill=(0, 0, 0), font=font)

                    # Sağ tarafta göstermek için görüntü oluştur
                    img2 = Image.new('RGB', (400, 1200), color=(255, 255, 255))
                    d2 = ImageDraw.Draw(img2)
                    d2.text((0, 0), kod_metni_bol2, fill=(0, 0, 0), font=font)

                    # Sağ tarafta göstermek için görüntü oluştur
                    img3 = Image.new('RGB', (400, 1200), color=(255, 255, 255))
                    d3 = ImageDraw.Draw(img3)
                    d3.text((0, 0), kod_metni_bol3, fill=(0, 0, 0), font=font)






                    # Birleştirilmiş görüntü oluştur
                    combined_img = Image.new('RGB', (1200, 1200), color=(255, 255, 255))

                    # Sol taraftaki görüntüyü birleştirilmiş görüntüye ekle
                    combined_img.paste(img1, (0, 0))

                    # Sağ taraftaki görüntüyü birleştirilmiş görüntüye ekle
                    combined_img.paste(img2, (400, 0))

                     # Sağ taraftaki görüntüyü birleştirilmiş görüntüye ekle
                    combined_img.paste(img3, (800, 0))

                    # Görüntüyü kaydet
                    goruntu_adi = os.path.splitext(dosya)[0] + ".png"
                    goruntu_yolu = os.path.join(out_klasor_yolu, goruntu_adi)
                    try:
                        combined_img.save(goruntu_yolu)
                    except Exception as e:
                        print(f"Hata: {e}")

if __name__ == "__main__":
    kod_klasoru = "in"
    goruntu_klasoru = "out"
    ekran_goruntusu_al(kod_klasoru, goruntu_klasoru)
"""

#4lu

import os
from PIL import Image, ImageDraw, ImageFont

def koddan_kutuphaneleri_cikar(kod_yolu):
    try:
        with open(kod_yolu, 'r') as dosya:
            kod_satirlari = dosya.readlines()
    except Exception as e:
        print(f"Hata: {e}")
        return []

    yeni_kod_satirlari = []
    for satir in kod_satirlari:
        satir = satir.rstrip()
        if not satir or satir.startswith("import") or satir.startswith("from"):
            continue
        yeni_kod_satirlari.append(satir.expandtabs(4))

    return yeni_kod_satirlari

def ekran_goruntusu_al(kod_klasoru, goruntu_klasoru):
    if not os.path.exists(goruntu_klasoru):
        os.makedirs(goruntu_klasoru)
    font = ImageFont.truetype("times.ttf", 10)
    for klasor in os.listdir(kod_klasoru):
        klasor_yolu = os.path.join(kod_klasoru, klasor)
        
        if os.path.isdir(klasor_yolu):  # Eğer klasör ise
            out_klasor_adi = klasor + "_out"
            out_klasor_yolu = os.path.join(goruntu_klasoru, out_klasor_adi)
            os.makedirs(out_klasor_yolu, exist_ok=True)  # Klasörü oluştur veya varsa geç
            
            for dosya in os.listdir(klasor_yolu):
                if dosya.endswith(".py"):  # Eğer dosya .py uzantılı ise
                    kod_yolu = os.path.join(klasor_yolu, dosya)
                    kod = koddan_kutuphaneleri_cikar(kod_yolu)
                    if not kod:
                        continue

                    kod_metni = '\n'.join(kod)

                    # Kodu iki parçaya böl
                    kod_satir_sayisi = len(kod)
                    bolme_noktasi = min(kod_satir_sayisi, 123)  # İlk 62 satırı al, ancak kod 62 satırdan kısa ise tüm kodu al

                    if kod_satir_sayisi < bolme_noktasi*4 :
                        
                        kod_metni_bol1 = '\n'.join(kod[:bolme_noktasi])
                        kod_metni_bol2 = '\n'.join(kod[bolme_noktasi:bolme_noktasi*2])
                        kod_metni_bol3 = '\n'.join(kod[bolme_noktasi*2:bolme_noktasi*2+bolme_noktasi])
                        kod_metni_bol4 = '\n'.join(kod[bolme_noktasi*2+bolme_noktasi:])

                        # Sol tarafta göstermek için görüntü oluştur
                        img1 = Image.new('RGB', (400, 1600), color=(255, 255, 255))
                        d1 = ImageDraw.Draw(img1)
                        d1.text((0, 0), kod_metni_bol1, fill=(0, 0, 0), font=font)

                        # Sağ tarafta göstermek için görüntü oluştur
                        img2 = Image.new('RGB', (400, 1600), color=(255, 255, 255))
                        d2 = ImageDraw.Draw(img2)
                        d2.text((0, 0), kod_metni_bol2, fill=(0, 0, 0), font=font)

                        # Sağ tarafta göstermek için görüntü oluştur
                        img3 = Image.new('RGB', (400, 1600), color=(255, 255, 255))
                        d3 = ImageDraw.Draw(img3)
                        d3.text((0, 0), kod_metni_bol3, fill=(0, 0, 0), font=font)
                        
                        
                        # Sağ tarafta göstermek için görüntü oluştur
                        img4 = Image.new('RGB', (400, 1600), color=(255, 255, 255))
                        d4 = ImageDraw.Draw(img4)
                        d4.text((0, 0), kod_metni_bol4, fill=(0, 0, 0), font=font)






                        # Birleştirilmiş görüntü oluştur
                        combined_img = Image.new('RGB', (1600, 1600), color=(255, 255, 255))

                        # Sol taraftaki görüntüyü birleştirilmiş görüntüye ekle
                        combined_img.paste(img1, (0, 0))

                        # Sağ taraftaki görüntüyü birleştirilmiş görüntüye ekle
                        combined_img.paste(img2, (400, 0))

                        # Sağ taraftaki görüntüyü birleştirilmiş görüntüye ekle
                        combined_img.paste(img3, (800, 0))
                        
                        # Sağ taraftaki görüntüyü birleştirilmiş görüntüye ekle
                        combined_img.paste(img4, (1200, 0))

                        # Görüntüyü kaydet
                        goruntu_adi = os.path.splitext(dosya)[0] + ".png"
                        goruntu_yolu = os.path.join(out_klasor_yolu, goruntu_adi)
                        try:
                            combined_img.save(goruntu_yolu)
                        except Exception as e:
                            print(f"Hata: {e}")

if __name__ == "__main__":
    kod_klasoru = "C:/Users/ervas/OneDrive/Masaüstü/ayrılmıs/Ortakformat low/ham"
    goruntu_klasoru = "C:/Users/ervas/OneDrive/Masaüstü/ayrılmıs/lowss/ham"
    ekran_goruntusu_al(kod_klasoru, goruntu_klasoru)

