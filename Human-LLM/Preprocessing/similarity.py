import os
import difflib
from concurrent.futures import ThreadPoolExecutor

def similarity_ratio(file1_path, file2_path):
    """
    Verilen iki dosyanın benzerlik oranını hesaplar.
    """
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        text1 = f1.read()
        text2 = f2.read()
    
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio()

def process_file_pair(file1_path, file2_path, threshold, result_file):
    """
    Verilen iki dosyanın benzerlik oranını kontrol eder ve gerekiyorsa birini siler.
    """
    similarity = similarity_ratio(file1_path, file2_path)
    if similarity >= threshold:
        os.remove(file2_path)
        with open(result_file, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{file2_path} dosyası, {file1_path} dosyasıyla %{similarity*100:.2f} oranında benzerlik gösterdiği için silindi.\n")

def delete_similar_files(threshold, result_file):
    """
    Çalışma dizinindeki "Ham" adlı dosyanın içindeki .txt dosyalarını okur ve 
    belirlenen eşik değeri üzerinde benzerlik gösteren dosyaları siler.
    """
    directory = os.getcwd()  # Çalışma dizini
    new_directory = os.path.join(directory, 'ham')
    
    files = os.listdir(new_directory)
    txt_files = [file for file in files if file.endswith('.txt')]
    
    with ThreadPoolExecutor(max_workers=4) as executor:  # Paralel işlemler için ThreadPoolExecutor
        for i, file1 in enumerate(txt_files):
            for j, file2 in enumerate(txt_files):
                if i != j:
                    file1_path = os.path.join(new_directory, file1)
                    file2_path = os.path.join(new_directory, file2)
                    if os.path.exists(file1_path) and os.path.exists(file2_path):
                        executor.submit(process_file_pair, file1_path, file2_path, threshold, result_file)

# Kullanım örneği:
threshold = 0.99 # %90 benzerlik
result_file = "benzerlik_sonuclari4o.txt"
delete_similar_files(threshold, result_file)
