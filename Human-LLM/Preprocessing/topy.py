import os

def convert_txt_to_py(directory):
    # Belirtilen dizindeki tüm dosyaları listele
    for filename in os.listdir(directory):
        # Eğer dosya bir .txt dosyası ise
        if filename.endswith(".txt"):
            # Tam dosya yolunu oluştur
            txt_file_path = os.path.join(directory, filename)
            # Aynı isimde .py dosya yolunu oluştur
            py_file_path = os.path.splitext(txt_file_path)[0] + '.py'
            
            # .txt dosyasını oku ve içeriği .py dosyasına yaz
            with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                content = txt_file.read()
            
            with open(py_file_path, 'w', encoding='utf-8') as py_file:
                py_file.write(content)
            
            print(f"Converted {filename} to {os.path.basename(py_file_path)}")

# Dönüştürme işlemi yapılacak dizin yolunu belirtin
directory = 'in'  # Buraya dönüştürmek istediğiniz klasörün yolunu girin
convert_txt_to_py(directory)
