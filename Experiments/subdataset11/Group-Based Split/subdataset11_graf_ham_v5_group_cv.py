#!/usr/bin/env python3
# subdataset11_graf_ham_v5_group_cv
# subdataset11 (graf) -- Ham / V5 -- Group-Based Split
# Calistirma:  python3 subdataset11_graf_ham_v5_group_cv.py                 (bu bilgisayarda WSL'de; sonuclar yanindaki sonuclar/ klasorune)
#              python3 subdataset11_graf_ham_v5_group_cv.py --sadece-ayrim  (egitim yok, yalniz veri ayrimi)
#              python3 subdataset11_graf_ham_v5_group_cv.py --onizleme 3    (modelin gordugu goruntulerden ornek kaydeder, egitim yok)
# Colab:       %run "/content/drive/MyDrive/<yeni_kod'un Drive'daki yeri>/subdataset11/Group-Based Split/subdataset11_graf_ham_v5_group_cv.py"
#              (%run ile calisinca Drive'i kendisi baglar; !python ile calistirilirsa once drive.mount yapilmali)
#              Veri: DRIVE_VERI_YOLU (Drive'daki veri klasoru; .zip de olabilir, o zaman /content'e bir kez acilir)
#              Sonuclar bu dosyanin yanindaki sonuclar/ klasorune (Drive'a) yazilir.
#
# Eski notebook'a gore degisenler: modele ozgu ImageNet on islemesi; taban donuk, yalniz son blok egitilir (BatchNorm'lu
# modellerde BN istatistikleri sabit); L2 0.01 -> 1e-4 (loss saf cross-entropy duzeyinde, ayrica "ce" izlenir); erken durdurma val_ce
# patience 4 + ReduceLROnPlateau; giris 320x320, kirpma YOK, antialias kucultme; goruntuler kosu basina bir kez acilir;
# metrikler macro/micro/weighted + sinif bazli + MCC/AUC/CE; tahminler ve egitim gecmisi kaydedilir; mixed precision;
# ayarlar degisirse eski CV sonuclari kullanilmaz; Adam clipnorm=1.0; dogrulamada tek sinifa cokme olursa egitim
# lr/10 ile bir kez tekrarlanir; testte %95 bootstrap guven araligi ve kumelerin sinif dagilimi kaydedilir.
# Sinif agirligi: class_weight='balanced' (egitim kaybina; dogrulama kaybi ve metrikler agirliksiz).
import argparse
import gc
import hashlib
import json
import platform
import re
import sys
import time
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import (GroupShuffleSplit, StratifiedGroupKFold, StratifiedKFold,
                                     train_test_split)
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, classification_report, confusion_matrix,
                             log_loss, matthews_corrcoef, precision_recall_fscore_support, roc_auc_score)

BETIK_SURUMU = "2026-10-02f"

# =================================================================================================================
# BU KOSUNUN AYARLARI
# =================================================================================================================
SUBDATASET = 11
SINIFLAR = ['ham', 'v5']                # etiket = listedeki sira (0 = ham)
AYRIM = "group"                     # "group" = Group-Based Split, "snippet" = Snippet-Level Split
TUR, LLM = "graf", "GPT-4o"
PROCESS = "2 = (3-1-5)  Benzerlik + High-format + AST-Graf"
VERI_YOLLARI = ['C:\\Users\\Murat Çoban\\Desktop\\Bitirme çalışması\\Kullanılan Veriler\\GRAF\\GRAF4O HIGH', 'C:\\Users\\murat.coban\\Desktop\\Bitirme çalışması\\Kullanılan Veriler\\GRAF\\GRAF4O HIGH']
ALT_KLASOR_EKI = ""
HARIC_RE = None   # ham klasorunde olup adi LLM surumu olan (yanlis yerlesmis) dosyalar listeye alinmaz
DRIVE_VERI_YOLU = '/content/drive/MyDrive/yukseklisans/Bitirme/GRAF/GRAF/GRAF4O HIGH'   # Colab: Drive'daki veri klasoru (ya da .zip)
ELLE_VERI_YOLU = None   # baska bir bilgisayarda veri baska yerdeyse buraya yazin, ornek: r"D:\Veri\GRAF 3.5 HIGH"

MODEL_ADI = "InceptionV3"
ON_ISLEME = "tf"              # caffe: VGG/ResNet, tf: Inception/MobileNet/NASNet, torch: DenseNet, ham: EfficientNet
ACTIVATION = "sigmoid"
DROPOUT_RATE = 0.2
LEARNING_RATE = 0.0001
EGITIM_BASLANGIC = None         # taban modelde bu adla baslayan ilk katmandan sona kadar egitilir
SON_KATMAN = 30                    # EGITIM_BASLANGIC yoksa: egitilecek son taban katman sayisi
IMG = 320
EPOCHS, PATIENCE, LR_PATIENCE, BATCH = 20, 4, 2, 16
L2 = 1e-4
MIXED = True
DENSE_BIRIM = 512
TEST_ORANI, VAL_ORANI, CV_KAT, IC_VAL_ORANI, RANDOM_SEED = 0.15, 0.15, 5, 0.15, 42
AYNI_ICERIGI_BIRLESTIR = True
MIN_ESLESME_ORANI = 0.25
MAKS_AILE_ORANI = 0.75
ORAN_TOLERANSI = 0.03
# =================================================================================================================

_p = argparse.ArgumentParser()
_p.add_argument("--sadece-ayrim", action="store_true")
_p.add_argument("--onizleme", type=int, default=0)
_p.add_argument("--veri", help="veri klasoru (verilirse once bu kullanilir; Windows ya da Linux yolu)")
_K = _p.parse_args()

KLASOR = {"snippet": "Snippet-Level Split", "group": "Group-Based Split"}
N_SINIF = len(SINIFLAR)
IKILI = N_SINIF == 2
SINIF_ADLARI = ["Ham"] + [s.upper() for s in SINIFLAR[1:]]
GRUP = AYRIM == "group"
SINIF_ADI = MODEL_ADI
NAME = "subdataset11_graf_ham_v5_group_cv"


def _resolve(win_path: str) -> Path:
    """Windows'ta oldugu gibi; WSL/Linux'ta 'C:\\...' yolunu '/mnt/c/...' yapar."""
    if platform.system() == "Windows":
        return Path(win_path)
    m = re.match(r"^([A-Za-z]):\\(.*)$", win_path)
    if m:
        return Path(f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92), '/')}")
    return Path(win_path)


# ---- Colab mi, bu bilgisayar mi? ----
try:
    import google.colab  # noqa: F401
    COLAB = True
except ImportError:
    COLAB = False
if COLAB:
    if not Path("/content/drive/MyDrive").is_dir():
        try:
            from google.colab import drive
            drive.mount("/content/drive")
        except Exception as _e:
            sys.exit(f"Drive baglanamadi ({_e}). Dosyayi %run ile calistirin ya da once bir hucrede "
                     f"from google.colab import drive; drive.mount('/content/drive') yapin.")
    _yol = Path(_K.veri) if _K.veri else Path(DRIVE_VERI_YOLU or "/yok")   # --veri: ornegin /content'e kopyalanmis veri
    if not _yol.exists() and DRIVE_VERI_YOLU:    # yol tutmazsa: ayni adli klasoru Bitirme altinda ara (klasor tasindiysa)
        _ust = Path("/content/drive/MyDrive/yukseklisans/Bitirme")
        _bulunan = [d for desen in (f"*/{_yol.name}", f"*/*/{_yol.name}", f"*/*/*/{_yol.name}")
                    for d in sorted(_ust.glob(desen)) if d.is_dir()]
        if _bulunan:
            print(f"DRIVE_VERI_YOLU bulunamadi, ayni adli klasor kullaniliyor: {_bulunan[0]}", flush=True)
            _yol = _bulunan[0]
    if _yol.is_dir():
        _kok = _yol                                      # veri Drive'da klasor olarak duruyor
    elif _yol.suffix.lower() == ".zip" and _yol.is_file():
        _zip = _yol
        _kok = Path(f"/content/veri/subdataset{SUBDATASET}")   # zip yerel diske bir kez acilir
        if not (_kok / ".acildi").exists():
            print("Veri zip'i aciliyor:", _zip, flush=True)
            with zipfile.ZipFile(_zip) as _z:
                _z.extractall(_kok)
            (_kok / ".acildi").touch()
    else:
        sys.exit(f"Veri bulunamadi: DRIVE_VERI_YOLU = {DRIVE_VERI_YOLU!r}. Dosyanin basindaki bu satira Drive'daki "
                 f"veri klasorunun (ya da .zip'in) yolunu yazin.")
    _tamam = lambda d: all((d / f"{s}{ALT_KLASOR_EKI}").is_dir() for s in SINIFLAR)  # noqa: E731
    _aday = [_kok] if _tamam(_kok) else [d for d in sorted(_kok.rglob("*")) if d.is_dir() and _tamam(d)]
    assert _aday, f"Sinif klasorleri ({SINIFLAR}) {_kok} altinda bulunamadi"
    VERI_KOK = _aday[0]
    CIKTI_KOK = Path(__file__).resolve().parent / "sonuclar"
else:
    # sira: elle yazilan yol -> bu dosyanin yerine gore (Masaustu\Bitirme\yeni_kod\... ise
    # Masaustu\Bitirme calismasi\Kullanilan Veriler\...) -> bilinen kullanici yollari
    _goreli = VERI_YOLLARI[0].split("Kullanılan Veriler" + chr(92), 1)[1].replace(chr(92), "/")
    _adaylar = ([_resolve(_K.veri)] if _K.veri else []) + \
               ([_resolve(ELLE_VERI_YOLU)] if ELLE_VERI_YOLU else []) + \
               [Path(__file__).resolve().parents[4] / "Bitirme çalışması" / "Kullanılan Veriler" / _goreli] + \
               [_resolve(v) for v in VERI_YOLLARI]
    VERI_KOK = next((v for v in _adaylar if v.is_dir()), None)
    if VERI_KOK is None:
        sys.exit("Veri klasoru bulunamadi. Dosyanin basindaki ELLE_VERI_YOLU satirina veri klasorunun yolunu yazin. "
                 "Denenen yollar:\n  " + "\n  ".join(map(str, _adaylar)))
    CIKTI_KOK = Path(__file__).resolve().parent / "sonuclar"
SINIF_DIR = {s: VERI_KOK / f"{s}{ALT_KLASOR_EKI}" for s in SINIFLAR}
# ---- sd11 guvenlik kontrolu: ham graflar YENIDEN URETILMIS 400x400 olanlar olmali (eski 1600x1600 degil) ----
from PIL import Image as _Image
_boy = {s: sorted({_Image.open(p).size for p in sorted(SINIF_DIR[s].glob("*.png"))[:30]}) for s in SINIFLAR}
if _boy["ham"] != _boy[SINIFLAR[1]]:
    sys.exit(f"DURDU: ham goruntu boyutu {_boy['ham']} != {SINIFLAR[1]} {_boy[SINIFLAR[1]]}. "
             f"ham klasorunde 2026-10-04'te yeniden uretilen 400x400 graflar olmali (Desktop\\yeni graf\\ham).")
print("Goruntu boyutlari:", _boy, flush=True)
SONUC_DIR = CIKTI_KOK / NAME
SONUC_DIR.mkdir(parents=True, exist_ok=True)

AYARLAR = {
    "betik_surumu": BETIK_SURUMU, "subdataset": SUBDATASET, "siniflar": SINIFLAR, "ayrim": AYRIM,
    "veri_klasoru_adi": VERI_KOK.name, "model": MODEL_ADI, "activation": ACTIVATION, "dropout": DROPOUT_RATE,
    "learning_rate": LEARNING_RATE, "son_katman": None if EGITIM_BASLANGIC else SON_KATMAN,
    "egitim_baslangic": EGITIM_BASLANGIC, "taban": "donuk, yalniz son katmanlar egitilir",
    "haric_re": HARIC_RE, "kucultme": "bilinear antialias, uint8, kosu basina bir kez acilir",
    "on_isleme": ON_ISLEME, "epochs": EPOCHS, "patience": PATIENCE, "erken_durdurma": "val_ce (min)",
    "lr_azaltma": {"monitor": "val_ce", "factor": 0.5, "patience": LR_PATIENCE}, "batch": BATCH,
    "img": IMG, "dense": DENSE_BIRIM, "l2": L2, "mixed_precision": MIXED,
    "test_orani": TEST_ORANI, "val_orani": VAL_ORANI, "cv_kat": CV_KAT, "ic_val_orani": IC_VAL_ORANI,
    "clipnorm": 1.0, "cokme_kontrolu": "dogrulamada tek sinif payi >= 0.95 ise lr/10 ile 1 tekrar",
    "sinif_agirligi": "balanced (her egitimde o egitimin egitim kumesinden; yalniz egitim kaybina)",
    "seed": RANDOM_SEED, "min_eslesme": MIN_ESLESME_ORANI if GRUP else None,
    "maks_aile": MAKS_AILE_ORANI if GRUP else None,
}
AYAR_OZETI = hashlib.md5(json.dumps(AYARLAR, sort_keys=True).encode()).hexdigest()[:12]


class _Tee:
    """Ekrana yazilani calisma.log dosyasina da yazar."""
    def __init__(self, akim, dosya):
        self.akim, self.dosya = akim, dosya

    def write(self, s):
        self.akim.write(s)
        self.dosya.write(s)
        self.dosya.flush()

    def flush(self):
        self.akim.flush()
        self.dosya.flush()


_log = open(SONUC_DIR / "calisma.log", "a", encoding="utf-8")
_o, _e = sys.stdout, sys.stderr
while hasattr(_o, "akim"):      # Colab %run: onceki kosunun yonlendirmesi varsa ac (ust uste binmesin)
    _o = _o.akim
while hasattr(_e, "akim"):
    _e = _e.akim
sys.stdout = _Tee(_o, _log)
sys.stderr = _Tee(_e, _log)
print(f"\n{'=' * 100}\n{time.strftime('%Y-%m-%d %H:%M:%S')}  {NAME}  (ayar ozeti {AYAR_OZETI})")

if (SONUC_DIR / "sonuc.json").exists() and not _K.sadece_ayrim:
    print("sonuc.json zaten var -> bu kosu tamamlanmis, atlaniyor. Yeniden kosmak icin klasoru silin:", SONUC_DIR)
    sys.exit(0)

AYAR_DOSYA = SONUC_DIR / "ayarlar.json"
if AYAR_DOSYA.exists():
    eski = json.loads(AYAR_DOSYA.read_text(encoding="utf-8"))
    if eski.get("ayar_ozeti") != AYAR_OZETI:
        sys.exit(f"DURDU: bu klasordeki onceki kosu FARKLI ayarlarla yapilmis ({eski.get('ayar_ozeti')} != {AYAR_OZETI}). "
                 f"Eski CV sonuclari yenileriyle karismasin diye devam edilmiyor. Klasoru silin ya da tasiyin: {SONUC_DIR}")
AYAR_DOSYA.write_text(json.dumps({**AYARLAR, "ayar_ozeti": AYAR_OZETI}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Veri    : {VERI_KOK}")
print(f"Siniflar: {SINIF_ADLARI}   Ayrim: {KLASOR[AYRIM]}")
print(f"Model   : {MODEL_ADI}  activation={ACTIVATION}  dropout={DROPOUT_RATE}  lr={LEARNING_RATE:g}  "
      f"egitilen={'taban ' + EGITIM_BASLANGIC + '* sonrasi' if EGITIM_BASLANGIC else f'son {SON_KATMAN} katman'}  "
      f"on isleme={ON_ISLEME}  L2={L2:g}")
print(f"Egitim  : en fazla {EPOCHS} epoch, erken durdurma val_ce patience {PATIENCE}, batch {BATCH}, "
      f"{IMG}x{IMG} (kirpma yok), mixed precision {MIXED}")
print(f"Cikti   : {SONUC_DIR}")

# ---------------------------------------------------------------------------------------------------------------
# Veri: listele + etiketle (etiket = SINIFLAR listesindeki sira: 0 = ham)
# ---------------------------------------------------------------------------------------------------------------
def list_images(folder):
    exts = (".png", ".jpg", ".jpeg")
    return sorted([p for p in Path(folder).glob("*") if p.suffix.lower() in exts], key=lambda p: p.name)


for s in SINIFLAR:
    assert SINIF_DIR[s].is_dir(), f"Klasor bulunamadi: {SINIF_DIR[s]}"
sinif_dosyalari = {s: list_images(SINIF_DIR[s]) for s in SINIFLAR}
haric = []
if HARIC_RE:
    haric = [p.name for p in sinif_dosyalari["ham"] if re.match(HARIC_RE, p.name)]
    sinif_dosyalari["ham"] = [p for p in sinif_dosyalari["ham"] if not re.match(HARIC_RE, p.name)]
    print(f"Ham klasorunde olup adi LLM surumu olan {len(haric)} dosya listeye ALINMADI (veri degismez): {haric}")
for k, s in enumerate(SINIFLAR):
    print(f"{SINIF_ADLARI[k]:3s} (etiket {k}): {len(sinif_dosyalari[s])} goruntu")
files = [p for s in SINIFLAR for p in sinif_dosyalari[s]]
paths = np.array([str(p) for p in files])
labels = np.concatenate([np.full(len(sinif_dosyalari[s]), k) for k, s in enumerate(SINIFLAR)]).astype(int)
dosya_adlari = [p.name for p in files]
n = len(files)
print(f"Toplam {n} goruntu")


def dagilim(ix):
    return " ".join(f"{ad}={int((labels[ix] == k).sum())}" for k, ad in enumerate(SINIF_ADLARI))


# ---------------------------------------------------------------------------------------------------------------
# Veri ayrimi
# ---------------------------------------------------------------------------------------------------------------
idx_all = np.arange(n)
aile_bilgi = {}
if GRUP:
    def dosya_ozeti(p):
        with open(p, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    icerikler = np.array([dosya_ozeti(p) for p in files])

    # Aile anahtari: [<dis sira>_][v<n>_[v<m>_]][bosluk]<sira>_content_<yazar>_<repo>_<dosya>.py[_cleaned] + uzanti
    #                -> <yazar>_<repo>_<dosya>   (eski notebook'larla ayni kural)
    AD_RE = re.compile(r"^(?:(?P<dis>\d+)_)?(?:vs?(?P<surum>[1-5])_?\s*)*(?P<sira>\d+)_content_(?P<govde>.+)$")

    def aile_anahtari(dosya_adi):
        s = re.sub(r"\.(png|jpg|jpeg|txt)$", "", str(dosya_adi).strip(), flags=re.IGNORECASE)
        m = AD_RE.match(s)
        if m is None:
            return None, None
        govde = re.sub(r"(?:\.py\w*)+$", "", m.group("govde"), flags=re.IGNORECASE)
        return re.sub(r"\s+", "", govde).lower(), m.group("surum")

    cozum = [aile_anahtari(ad) for ad in dosya_adlari]
    cozulemeyen = [ad for ad, (a, _) in zip(dosya_adlari, cozum) if not a]
    assert not cozulemeyen, f"KONTROL 1: {len(cozulemeyen)} dosya adi aile kalibina uymuyor: {cozulemeyen[:5]}"
    anahtarlar = np.array([a for a, _ in cozum])
    ad_surumleri = [s for _, s in cozum]

    def aileleri_olustur(deger_dizileri):
        ebeveyn = list(range(n))

        def bul(i):
            while ebeveyn[i] != i:
                ebeveyn[i] = ebeveyn[ebeveyn[i]]
                i = ebeveyn[i]
            return i

        for dizi in deger_dizileri:
            ilk = {}
            for i, deger in enumerate(dizi.tolist()):
                if deger in ilk:
                    a, b = bul(i), bul(ilk[deger])
                    if a != b:
                        ebeveyn[max(a, b)] = min(a, b)
                else:
                    ilk[deger] = i
        kokler = [bul(i) for i in range(n)]
        numara = {kok: k for k, kok in enumerate(sorted(set(kokler)))}
        return np.array([numara[kok] for kok in kokler])

    yalniz_ad_aileleri = aileleri_olustur([anahtarlar])
    families = aileleri_olustur([anahtarlar, icerikler]) if AYNI_ICERIGI_BIRLESTIR else yalniz_ad_aileleri

    tab = pd.DataFrame({"aile": families, "etiket": labels}).groupby("aile")["etiket"]
    sinif_sayisi = tab.nunique()
    ham_var = tab.min() == 0
    n_aile = int(len(sinif_sayisi))
    ham_ve_surum = int((ham_var & (sinif_sayisi >= 2)).sum())
    eslesme_orani = ham_ve_surum / n_aile
    aile_bilgi = {"aile_sayisi": n_aile, "ham_ve_surum_iceren_aile": ham_ve_surum,
                  "tum_sinifli_aile": int((sinif_sayisi == N_SINIF).sum()),
                  "yalniz_ham_aile": int((ham_var & (sinif_sayisi == 1)).sum()),
                  "ham_icermeyen_aile": int((~ham_var).sum()), "eslesme_orani": eslesme_orani,
                  "icerikle_birlesen_aile": int(len(np.unique(yalniz_ad_aileleri)) - n_aile)}
    print(f"Aile: {aile_bilgi}")
    assert eslesme_orani >= MIN_ESLESME_ORANI, \
        f"KONTROL 2: AILE ANAHTARI CALISMIYOR (eslesme %{100 * eslesme_orani:.1f} < %{100 * MIN_ESLESME_ORANI:.0f})"
    assert n_aile <= MAKS_AILE_ORANI * n, f"KONTROL 3: aile sayisi ({n_aile}) ornek sayisina ({n}) cok yakin"

    # KONTROL 4: anahtardan bagimsiz basit kuralla bulunan her ham-surum cifti ayni ailede olmali
    def basit_cekirdek(dosya_adi):
        s = re.sub(r"\s+", "", str(dosya_adi))
        s = re.sub(r"^\d+_(?=(?:v\d_)*\d+_content_)", "", s)
        return re.sub(r"^(?:v\d_)+", "", s)

    ham_konum = {}
    for i in np.where(labels == 0)[0]:
        ham_konum.setdefault(basit_cekirdek(dosya_adlari[i]), []).append(i)
    capraz_cift = capraz_ihlal = 0
    for i in np.where(labels != 0)[0]:
        for j in ham_konum.get(basit_cekirdek(dosya_adlari[i]), []):
            capraz_cift += 1
            capraz_ihlal += int(families[i] != families[j])
    print(f"KONTROL 4: basit kuralla ham-surum cifti {capraz_cift}, farkli aileye dusen {capraz_ihlal}")
    assert capraz_cift > 0 and capraz_ihlal == 0, "KONTROL 4 gecmedi: aile anahtari duzeltilmeli"

    supheli_etiket = [ad for ad, e, s in zip(dosya_adlari, labels, ad_surumleri)
                      if (e == 0 and s is not None) or (e != 0 and s != SINIFLAR[e].lstrip("v"))]
    aile_bilgi["klasor_ad_surumu_uyusmayan_dosya"] = len(supheli_etiket)
    print(f"Klasoru ile adindaki surum etiketi uyusmayan dosya (veri degistirilmez): {len(supheli_etiket)}")

    def sizinti_kontrol(kumeler, baslik):
        denetlenecek = [("aile", families), ("aile anahtari", anahtarlar)]
        if AYNI_ICERIGI_BIRLESTIR:
            denetlenecek.append(("icerik", icerikler))
        adlar = list(kumeler)
        for a in range(len(adlar)):
            for b in range(a + 1, len(adlar)):
                ia, ib = np.asarray(kumeler[adlar[a]]), np.asarray(kumeler[adlar[b]])
                assert not set(ia.tolist()) & set(ib.tolist()), f"{baslik}: {adlar[a]}/{adlar[b]} ayni ornek"
                for ne, dizi in denetlenecek:
                    ortak = set(dizi[ia].tolist()) & set(dizi[ib].tolist())
                    assert not ortak, f"SIZINTI ({baslik}): {adlar[a]}/{adlar[b]} ortak {ne}: {sorted(ortak)[:3]}"

    def ayir(indeksler, oran, seed):
        gss = GroupShuffleSplit(n_splits=1, test_size=oran, random_state=seed)
        a, b = next(gss.split(indeksler, labels[indeksler], groups=families[indeksler]))
        return indeksler[a], indeksler[b]

    dev_idx, test_idx = ayir(idx_all, TEST_ORANI, RANDOM_SEED)
    train_idx, val_idx = ayir(dev_idx, VAL_ORANI / (1.0 - TEST_ORANI), RANDOM_SEED)
    sizinti_kontrol({"egitim": train_idx, "dogrulama": val_idx, "test": test_idx}, "70/15/15")
    for ad, ix, hedef in (("dogrulama", val_idx, VAL_ORANI), ("test", test_idx, TEST_ORANI)):
        assert abs(len(ix) / n - hedef) <= ORAN_TOLERANSI, f"{ad} orani %{100 * len(ix) / n:.1f}"
    sgkf = StratifiedGroupKFold(n_splits=CV_KAT, shuffle=True, random_state=RANDOM_SEED)
    cv_katlari = [(dev_idx[tr], dev_idx[va])
                  for tr, va in sgkf.split(dev_idx, labels[dev_idx], groups=families[dev_idx])]
    for kat, (tr, va) in enumerate(cv_katlari, start=1):
        sizinti_kontrol({"kat egitim": tr, "kat degerlendirme": va, "test": test_idx}, f"CV kat {kat}")

    def ic_ayir(kat_egitim_idx, kat):
        return ayir(kat_egitim_idx, IC_VAL_ORANI, RANDOM_SEED + kat)
else:
    families = anahtarlar = None
    dev_idx, test_idx = train_test_split(idx_all, test_size=TEST_ORANI, random_state=RANDOM_SEED, stratify=labels)
    train_idx, val_idx = train_test_split(dev_idx, test_size=VAL_ORANI / (1.0 - TEST_ORANI),
                                          random_state=RANDOM_SEED, stratify=labels[dev_idx])
    skf = StratifiedKFold(n_splits=CV_KAT, shuffle=True, random_state=RANDOM_SEED)
    cv_katlari = [(dev_idx[tr], dev_idx[va]) for tr, va in skf.split(dev_idx, labels[dev_idx])]

    def sizinti_kontrol(kumeler, baslik):
        adlar = list(kumeler)
        for a in range(len(adlar)):
            for b in range(a + 1, len(adlar)):
                assert not set(np.asarray(kumeler[adlar[a]]).tolist()) & set(np.asarray(kumeler[adlar[b]]).tolist()), \
                    f"{baslik}: {adlar[a]}/{adlar[b]} ayni ornegi iceriyor"

    sizinti_kontrol({"egitim": train_idx, "dogrulama": val_idx, "test": test_idx}, "70/15/15")

    def ic_ayir(kat_egitim_idx, kat):
        return train_test_split(kat_egitim_idx, test_size=IC_VAL_ORANI, random_state=RANDOM_SEED + kat,
                                stratify=labels[kat_egitim_idx])

assert len(train_idx) + len(val_idx) + len(test_idx) == n
assert sorted(np.concatenate([va for _, va in cv_katlari]).tolist()) == sorted(dev_idx.tolist())
for ad, ix in (("Egitim", train_idx), ("Dogrulama", val_idx), ("Test", test_idx)):
    print(f"{ad:10s}: {len(ix):5d} (%{100 * len(ix) / n:.1f})  {dagilim(ix)}")
    assert len(np.unique(labels[ix])) == N_SINIF, f"{ad} kumesinde {N_SINIF} sinifin hepsi yok"
for kat, (tr, va) in enumerate(cv_katlari, start=1):
    assert len(np.unique(labels[tr])) == N_SINIF and len(np.unique(labels[va])) == N_SINIF
    print(f"Kat {kat}: egitim={len(tr)} ({dagilim(tr)})  degerlendirme={len(va)} ({dagilim(va)})")
print("Sizinti kontrolu GECTI.")

ayrim = pd.DataFrame({"dosya": dosya_adlari, "etiket": labels, "kume": ""})
if GRUP:
    ayrim["aile"] = families
    ayrim["aile_anahtari"] = anahtarlar
ayrim.loc[train_idx, "kume"] = "train"
ayrim.loc[val_idx, "kume"] = "val"
ayrim.loc[test_idx, "kume"] = "test"
ayrim["cv_kat"] = 0
for kat, (_, va) in enumerate(cv_katlari, start=1):
    ayrim.loc[va, "cv_kat"] = kat
if GRUP:
    assert ayrim.groupby("aile")["kume"].nunique().max() == 1, "bir aile birden fazla kumede"
ayrim.to_csv(SONUC_DIR / "veri_ayrimi.csv", index=False, encoding="utf-8-sig")
if _K.sadece_ayrim:
    print("--sadece-ayrim: veri ayrimi kaydedildi, egitim yapilmadi.")
    sys.exit(0)

# ---------------------------------------------------------------------------------------------------------------
# TensorFlow, model, egitim
# ---------------------------------------------------------------------------------------------------------------
import os  # noqa: E402

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")   # TF'nin bilgi/uyari dokumlerini kis
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402
import tensorflow as tf  # noqa: E402

gpus = tf.config.list_physical_devices("GPU")
for g in gpus:
    try:
        tf.config.experimental.set_memory_growth(g, True)
    except RuntimeError as e:
        print(e)
print("TensorFlow", tf.__version__, "| GPU:", gpus if gpus else "YOK (CPU)")
if MIXED and gpus:
    tf.keras.mixed_precision.set_global_policy("mixed_float16")
    print("Mixed precision: mixed_float16 (cikis katmani float32)")
TabanModel = getattr(tf.keras.applications, SINIF_ADI)

_CAFFE_ORT = tf.constant([103.939, 116.779, 123.68])
_TORCH_ORT = tf.constant([0.485, 0.456, 0.406])
_TORCH_STD = tf.constant([0.229, 0.224, 0.225])


def on_isle(img):
    """img: float32, 0-255, RGB. Modelin ImageNet egitimindeki on islemenin aynisi (keras preprocess_input)."""
    if ON_ISLEME == "caffe":
        return img[..., ::-1] - _CAFFE_ORT          # RGB -> BGR, kanal ortalamasi cikarilir
    if ON_ISLEME == "tf":
        return img / 127.5 - 1.0                    # [-1, 1]
    if ON_ISLEME == "torch":
        return (img / 255.0 - _TORCH_ORT) / _TORCH_STD
    return img                                      # EfficientNet: 0-255, olcekleme modelin icinde


def onizleme_kaydet(adet):
    hedef = SONUC_DIR / "onizleme"
    hedef.mkdir(exist_ok=True)
    rng = np.random.default_rng(RANDOM_SEED)
    for k, ad in enumerate(SINIF_ADLARI):
        for i in rng.choice(np.where(labels == k)[0], size=min(adet, int((labels == k).sum())), replace=False):
            img = _yukle_yol(tf.constant(paths[i])).numpy()
            tf.io.write_file(str(hedef / f"{ad}_{Path(dosya_adlari[i]).stem[:60]}.png"), tf.io.encode_png(img))
    print(f"Onizleme: {hedef} ({IMG}x{IMG})")


def etiket_dizisi(ix):
    if IKILI:
        return labels[ix].astype("float32").reshape(-1, 1)
    return np.eye(N_SINIF, dtype="float32")[labels[ix]]


def _yukle_yol(path):
    img = tf.io.decode_image(tf.io.read_file(path), channels=3, expand_animations=False)
    img.set_shape([None, None, 3])
    img = tf.image.resize(tf.cast(img, tf.float32), (IMG, IMG), antialias=True)
    return tf.cast(tf.clip_by_value(tf.round(img), 0.0, 255.0), tf.uint8)


def goruntuleri_yukle():
    """Butun goruntuler kosu basina BIR KEZ acilip kucultulur (uint8); egitimler buradan okur."""
    t0 = time.time()
    dizi = np.empty((n, IMG, IMG, 3), dtype=np.uint8)
    k = 0
    for parca in tf.data.Dataset.from_tensor_slices(paths).map(_yukle_yol, num_parallel_calls=tf.data.AUTOTUNE) \
            .batch(64).prefetch(2):
        dizi[k:k + len(parca)] = parca.numpy()
        k += len(parca)
    assert k == n
    print(f"Goruntuler acildi: {n} adet, {dizi.nbytes / 1e9:.1f} GB, {time.time() - t0:.0f} sn", flush=True)
    return dizi


GORUNTULER = None


def make_dataset(indices, training, seed=RANDOM_SEED):
    ds = tf.data.Dataset.from_tensor_slices((np.asarray(indices, dtype="int64"), etiket_dizisi(indices)))
    if training:
        ds = ds.shuffle(buffer_size=len(indices), seed=seed)
    ds = ds.batch(BATCH)

    def _al(ix, y):
        img = tf.numpy_function(lambda i: GORUNTULER[i], [ix], tf.uint8)
        img.set_shape([None, IMG, IMG, 3])
        return on_isle(tf.cast(img, tf.float32)), y

    return ds.map(_al, num_parallel_calls=tf.data.AUTOTUNE).prefetch(tf.data.AUTOTUNE)


_MODEL_BILGI_YAZILDI = False


def create_model(lr=None):
    base = TabanModel(weights="imagenet", include_top=False, input_shape=(IMG, IMG, 3))
    base.trainable = True
    if EGITIM_BASLANGIC:
        bas = next(i for i, l in enumerate(base.layers) if l.name.startswith(EGITIM_BASLANGIC))
    else:
        bas = len(base.layers) - SON_KATMAN if SON_KATMAN > 0 else len(base.layers)
    for layer in base.layers[:bas]:
        layer.trainable = False                     # taban donuk; yalniz sondaki katmanlar egitilir
    girdi = tf.keras.Input(shape=(IMG, IMG, 3))
    x = base(girdi, training=False)    # BatchNorm iceren modellerde (DenseNet/ResNet/Inception/MobileNet/NASNet/
                                       # EfficientNet) BN istatistikleri sabit kalir; VGG'de BN yok, etkisi yok
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(DENSE_BIRIM, activation=ACTIVATION,
                              kernel_regularizer=tf.keras.regularizers.l2(L2))(x)
    x = tf.keras.layers.Dropout(DROPOUT_RATE)(x)
    if IKILI:
        cikis = tf.keras.layers.Dense(1, activation="sigmoid", dtype="float32")(x)
        kayip, ce = "binary_crossentropy", tf.keras.metrics.BinaryCrossentropy(name="ce")
    else:
        cikis = tf.keras.layers.Dense(N_SINIF, activation="softmax", dtype="float32")(x)
        kayip, ce = "categorical_crossentropy", tf.keras.metrics.CategoricalCrossentropy(name="ce")
    model = tf.keras.Model(girdi, cikis)
    global _MODEL_BILGI_YAZILDI
    if not _MODEL_BILGI_YAZILDI:
        egitilen = sum(int(np.prod(w.shape)) for w in model.trainable_weights)
        toplam = sum(int(np.prod(w.shape)) for w in model.weights)
        print(f"Model: taban {len(base.layers)} katman, egitilen taban katmani {len(base.layers) - bas} "
              f"(ilk: {base.layers[bas].name if bas < len(base.layers) else '-'}); "
              f"egitilen parametre {egitilen:,} / {toplam:,}")
        _MODEL_BILGI_YAZILDI = True
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr or LEARNING_RATE, clipnorm=1.0), loss=kayip,
                  metrics=["accuracy", ce])
    return model


def olasilik_matrisi(cikti):
    cikti = np.asarray(cikti, dtype="float64")
    if IKILI:
        p = cikti.reshape(-1)
        return np.stack([1.0 - p, p], axis=1)
    return cikti


def metrikler(y_true, prob):
    y_pred = prob.argmax(axis=1)
    m = {"accuracy": float(accuracy_score(y_true, y_pred)),
         "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
         "mcc": float(matthews_corrcoef(y_true, y_pred)),
         "cross_entropy": float(log_loss(y_true, prob, labels=list(range(N_SINIF))))}
    for ort in ("macro", "micro", "weighted"):
        p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average=ort, zero_division=0,
                                                      labels=list(range(N_SINIF)))
        m.update({f"precision_{ort}": float(p), f"recall_{ort}": float(r), f"f1_{ort}": float(f1)})
    p, r, f1, destek = precision_recall_fscore_support(y_true, y_pred, average=None, zero_division=0,
                                                       labels=list(range(N_SINIF)))
    for k, ad in enumerate(SINIF_ADLARI):
        m.update({f"precision_{ad}": float(p[k]), f"recall_{ad}": float(r[k]), f"f1_{ad}": float(f1[k]),
                  f"destek_{ad}": int(destek[k])})
    try:
        m["roc_auc"] = float(roc_auc_score(y_true, prob[:, 1]) if IKILI else
                             roc_auc_score(y_true, prob, multi_class="ovr", average="macro"))
    except ValueError:
        m["roc_auc"] = float("nan")
    return m


def tahmin_tablosu(ix, prob, egitim):
    t = pd.DataFrame({"egitim": egitim, "dosya": [dosya_adlari[i] for i in ix], "gercek": labels[ix],
                      "tahmin": prob.argmax(axis=1)})
    for k, ad in enumerate(SINIF_ADLARI):
        t[f"olasilik_{ad}"] = prob[:, k]
    return t


COKME_ESIGI = 0.95      # dogrulamada tahminlerin bu kadari tek sinifa gidiyorsa "cokme" sayilir


def sinif_agirligi(ix):
    """class_weight='balanced' (sklearn): w_k = n / (K * n_k), o egitimin EGITIM kumesinin sinif sayilarindan.
    Yalniz egitim kaybina uygulanir; dogrulama kaybi (erken durdurma) ve raporlanan metrikler agirliksizdir."""
    from sklearn.utils.class_weight import compute_class_weight
    w = compute_class_weight("balanced", classes=np.arange(N_SINIF), y=labels[ix])
    return {int(k): float(v) for k, v in enumerate(w)}


def egit_ve_degerlendir(egitim_idx, erken_idx, degerlendirme_idx, seed, egitim_adi):
    """Egitir; model dogrulama kumesinde tek sinifa coktuyse ayni egitimi bir kez lr/10 ile tekrarlar."""
    lr = LEARNING_RATE
    agirlik = sinif_agirligi(egitim_idx)
    print("Sinif agirligi (balanced): " + "  ".join(f"{SINIF_ADLARI[k]}={v:.3f}" for k, v in agirlik.items()), flush=True)
    for deneme in (1, 2):
        tf.keras.backend.clear_session()
        gc.collect()
        tf.keras.utils.set_random_seed(seed)
        model = create_model(lr)
        geri_cagir = [
            tf.keras.callbacks.EarlyStopping(monitor="val_ce", mode="min", patience=PATIENCE,
                                             restore_best_weights=True),
            tf.keras.callbacks.ReduceLROnPlateau(monitor="val_ce", mode="min", factor=0.5,
                                                 patience=LR_PATIENCE, min_lr=1e-7, verbose=1),
        ]
        t0 = time.time()
        gecmis = model.fit(make_dataset(egitim_idx, training=True, seed=seed),
                           validation_data=make_dataset(erken_idx, training=False),
                           epochs=EPOCHS, callbacks=geri_cagir, verbose=2, class_weight=agirlik)
        egitim_sn = time.time() - t0
        val_prob = olasilik_matrisi(model.predict(make_dataset(erken_idx, training=False), verbose=0))
        pay = float(np.bincount(val_prob.argmax(axis=1), minlength=N_SINIF).max() / len(erken_idx))
        if pay < COKME_ESIGI or deneme == 2:
            break
        print(f"COKME: dogrulama tahminlerinin %{100 * pay:.0f}'i tek sinifta -> egitim lr {lr / 10:g} ile "
              f"bir kez tekrarlaniyor", flush=True)
        lr = lr / 10
        # ilk denemenin modeli GPU bellegini tutmasin: model, gecmis (History.model) ve geri cagirmalar
        # (EarlyStopping en iyi agirliklari saklar) birlikte silinir
        del model, gecmis, geri_cagir, val_prob
        tf.keras.backend.clear_session()
        gc.collect()
    h = pd.DataFrame(gecmis.history)
    h.insert(0, "epoch", np.arange(1, len(h) + 1))
    h.insert(0, "deneme", deneme)
    h.insert(0, "egitim", egitim_adi)

    prob = olasilik_matrisi(model.predict(make_dataset(degerlendirme_idx, training=False), verbose=0))
    sonuc = metrikler(labels[degerlendirme_idx], prob)
    sonuc.update({"val_" + k: v for k, v in metrikler(labels[erken_idx], val_prob).items()})
    en_iyi = int(h["val_ce"].idxmin())
    sonuc.update({"epoch_sayisi": len(h), "en_iyi_epoch": en_iyi + 1, "en_iyi_val_ce": float(h["val_ce"].min()),
                  "egitim_sn": round(egitim_sn, 1), "deneme": deneme, "kullanilan_lr": lr,
                  "sinif_agirligi": json.dumps({SINIF_ADLARI[k]: round(v, 4) for k, v in agirlik.items()}),
                  "val_en_buyuk_sinif_payi": pay})
    del model
    tf.keras.backend.clear_session()
    gc.collect()
    return sonuc, prob, val_prob, h


def ekle_csv(df, yol, sutunlar=None):
    if sutunlar is not None:
        df = df.reindex(columns=sutunlar)
    df.to_csv(yol, mode="a", header=not yol.exists(), index=False)


_ornek = metrikler(np.arange(N_SINIF), np.eye(N_SINIF))
CV_SUTUNLAR = (["kat", "n_egitim", "n_ic_dogrulama", "n_degerlendirme"] + list(_ornek) + ["val_" + k for k in _ornek]
               + ["epoch_sayisi", "en_iyi_epoch", "en_iyi_val_ce", "egitim_sn", "deneme", "kullanilan_lr", "sinif_agirligi",
                  "val_en_buyuk_sinif_payi", "hata"])


if _K.onizleme:
    onizleme_kaydet(_K.onizleme)
    create_model()      # model kurulumu ve egitilen katman/parametre sayisi denetimi (egitim yok)
    sys.exit(0)

GORUNTULER = goruntuleri_yukle()

# ---- 5 katli CV (tamamlanan katlar atlanir; ayarlar ayni oldugu ayarlar.json ile garanti) ----
CV_CSV = SONUC_DIR / "cv_kat_sonuclari.csv"
GECMIS_CSV = SONUC_DIR / "egitim_gecmisi.csv"
tamamlanan = set()
if CV_CSV.exists():
    onceki = pd.read_csv(CV_CSV)
    onceki = onceki[onceki["hata"].isna() | (onceki["hata"].astype(str).str.strip() == "")]
    tamamlanan = set(int(k) for k in onceki["kat"])
    print(f"Onceden tamamlanmis katlar: {sorted(tamamlanan)} (atlanacak)")

for kat, (kat_egitim_idx, kat_deger_idx) in enumerate(cv_katlari, start=1):
    if kat in tamamlanan:
        continue
    print(f"\n===== Kat {kat}/{CV_KAT}  {time.strftime('%H:%M:%S')} =====")
    ic_egitim_idx, ic_val_idx = ic_ayir(kat_egitim_idx, kat)
    sizinti_kontrol({"ic egitim": ic_egitim_idx, "ic dogrulama": ic_val_idx, "kat degerlendirme": kat_deger_idx,
                     "test": test_idx}, f"CV kat {kat} (ic dogrulama)")
    assert len(np.unique(labels[ic_egitim_idx])) == N_SINIF and len(np.unique(labels[ic_val_idx])) == N_SINIF
    satir = {"kat": kat, "n_egitim": len(ic_egitim_idx), "n_ic_dogrulama": len(ic_val_idx),
             "n_degerlendirme": len(kat_deger_idx)}
    try:
        sonuc, prob, _, h = egit_ve_degerlendir(ic_egitim_idx, ic_val_idx, kat_deger_idx, RANDOM_SEED + kat,
                                                f"kat{kat}")
        satir.update(sonuc)
        satir["hata"] = ""
        ekle_csv(h, GECMIS_CSV)
        ekle_csv(tahmin_tablosu(kat_deger_idx, prob, f"kat{kat}"), SONUC_DIR / "tahminler_cv.csv")
    except Exception as e:
        satir["hata"] = f"{type(e).__name__}: {e}"[:300]
        tf.keras.backend.clear_session()
        gc.collect()
    ekle_csv(pd.DataFrame([satir]), CV_CSV, CV_SUTUNLAR)
    print(f"Kat {kat}: accuracy={satir.get('accuracy', float('nan')):.4f}  F1(w/m)={satir.get('f1_weighted', float('nan')):.4f}/"
          f"{satir.get('f1_macro', float('nan')):.4f}  CE={satir.get('cross_entropy', float('nan')):.4f}  "
          f"epoch={satir.get('epoch_sayisi', '-')}  {satir['hata']}")

cv = pd.read_csv(CV_CSV)
cv = cv[cv["hata"].isna() | (cv["hata"].astype(str).str.strip() == "")]
cv = cv.drop_duplicates(subset=["kat"], keep="last").sort_values("kat")
assert len(cv) == CV_KAT, f"{CV_KAT} katin hepsi tamamlanmadi ({len(cv)}); betigi yeniden calistirin (kaldigi kattan surer)."
OLCUTLER = ["accuracy", "balanced_accuracy", "mcc", "cross_entropy", "roc_auc"] + \
           [f"{m}_{o}" for o in ("macro", "micro", "weighted") for m in ("precision", "recall", "f1")]
cv_ozet = {m: {"ort": float(cv[m].mean()), "std": float(cv[m].std(ddof=1))} for m in OLCUTLER}
print("\nCV ortalama ± std:")
for m in OLCUTLER:
    print(f"  {m:22s} {cv_ozet[m]['ort']:.4f} ± {cv_ozet[m]['std']:.4f}")

# ---- Son egitim: %70 egitim (+%15 dogrulama erken durdurma), %15 testte bir kez ----
print(f"\n===== Son egitim  {time.strftime('%H:%M:%S')} =====")
test_sonuc, test_prob, val_prob, h = egit_ve_degerlendir(train_idx, val_idx, test_idx, RANDOM_SEED, "son")
ekle_csv(h, GECMIS_CSV)
pd.concat([tahmin_tablosu(test_idx, test_prob, "test"), tahmin_tablosu(val_idx, val_prob, "dogrulama")]) \
    .to_csv(SONUC_DIR / "tahminler.csv", index=False, encoding="utf-8-sig")
y_true, y_pred = labels[test_idx], test_prob.argmax(axis=1)
print(classification_report(y_true, y_pred, target_names=SINIF_ADLARI, zero_division=0, digits=4))

cm = confusion_matrix(y_true, y_pred, labels=list(range(N_SINIF)))
pd.DataFrame(cm, index=SINIF_ADLARI, columns=SINIF_ADLARI).to_csv(SONUC_DIR / "confusion_matrix.csv")
fig, ax = plt.subplots(figsize=(4 + N_SINIF, 3 + N_SINIF))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=SINIF_ADLARI, yticklabels=SINIF_ADLARI, ax=ax)
ax.set_xlabel("Tahmin")
ax.set_ylabel("Gercek")
ax.set_title(f"{NAME}\n{MODEL_ADI} - Confusion Matrix (held-out test)")
plt.tight_layout()
plt.savefig(SONUC_DIR / "confusion_matrix.png", dpi=150)
plt.close(fig)

fig, eksen = plt.subplots(1, 3, figsize=(15, 4))
for ax, (a, b, baslik) in zip(eksen, (("ce", "val_ce", "Cross-entropy (saf)"), ("loss", "val_loss", "Loss (CE + L2)"),
                                      ("accuracy", "val_accuracy", "Accuracy"))):
    ax.plot(h["epoch"], h[a], label="egitim")
    ax.plot(h["epoch"], h[b], label="dogrulama")
    ax.set_title(baslik)
    ax.set_xlabel("epoch")
    ax.legend()
plt.suptitle(f"{NAME} - son egitim")
plt.tight_layout()
plt.savefig(SONUC_DIR / "egitim_egrisi.png", dpi=120)
plt.close(fig)

GA_TEKRAR, GA_SEED = 1000, 42


def bootstrap_ga(y_true, prob):
    """Test kumesinde %95 bootstrap guven araligi: test ornekleri yerine koyarak GA_TEKRAR kez yeniden secilir,
    her seferinde metrik hesaplanir; %2.5 ve %97.5 yuzdelikleri alinir. Egitim yok, kayitli tahminlerden."""
    import warnings
    y_true = np.asarray(y_true)
    y_pred = np.asarray(prob).argmax(axis=1)
    etiket = list(range(N_SINIF))
    rng = np.random.default_rng(GA_SEED)
    kayit = {k: [] for k in ("accuracy", "f1_weighted", "f1_macro", "mcc", "balanced_accuracy")}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for _ in range(GA_TEKRAR):
            i = rng.integers(0, len(y_true), len(y_true))
            t, p = y_true[i], y_pred[i]
            kayit["accuracy"].append(accuracy_score(t, p))
            kayit["f1_weighted"].append(precision_recall_fscore_support(t, p, average="weighted", labels=etiket,
                                                                        zero_division=0)[2])
            kayit["f1_macro"].append(precision_recall_fscore_support(t, p, average="macro", labels=etiket,
                                                                     zero_division=0)[2])
            kayit["mcc"].append(matthews_corrcoef(t, p))
            kayit["balanced_accuracy"].append(balanced_accuracy_score(t, p))
    return {k: {"alt": float(np.percentile(v, 2.5)), "ust": float(np.percentile(v, 97.5))} for k, v in kayit.items()}


def sinif_dagilimi(ix):
    say = {ad: int((labels[ix] == k).sum()) for k, ad in enumerate(SINIF_ADLARI)}
    return {"sayi": say, "oran": {ad: round(v / max(1, len(ix)), 4) for ad, v in say.items()}, "toplam": int(len(ix))}


test_ga = bootstrap_ga(labels[test_idx], test_prob)
kume_dagilim = {"tum": sinif_dagilimi(idx_all), "train": sinif_dagilimi(train_idx), "val": sinif_dagilimi(val_idx),
                "test": sinif_dagilimi(test_idx)}
for ad, d in kume_dagilim.items():
    print(f"Sinif dagilimi {ad:5s}: {d['sayi']}  oran {d['oran']}")

sec = lambda d, on="": {m: d[on + m] for m in OLCUTLER}  # noqa: E731
sinif_bazli = lambda d, on="": {ad: {k: d[f"{on}{k}_{ad}"] for k in ("precision", "recall", "f1", "destek")}  # noqa: E731
                                for ad in SINIF_ADLARI}
result = {
    "kosu": NAME, "ayar_ozeti": AYAR_OZETI, "ayarlar": AYARLAR, "subdataset": SUBDATASET, "llm": LLM,
    "process_id_aciklama": PROCESS, "siniflar": {ad: k for k, ad in enumerate(SINIF_ADLARI)},
    "veri": {**{s: len(sinif_dosyalari[s]) for s in SINIFLAR}, "toplam": n, "haric_tutulan": haric},
    "split": {"train": len(train_idx), "val": len(val_idx), "test": len(test_idx),
              "yontem": ("aile bazli: iki asamali GroupShuffleSplit 70/15/15, CV StratifiedGroupKFold" if GRUP else
                         "stratified rastgele 70/15/15, CV StratifiedKFold") + ", random_state=42"},
    "kume_sinif_dagilimi": kume_dagilim,
    "aile": aile_bilgi,
    "metrik_notu": "micro P = micro R = micro F1 = accuracy (tek etiketli siniflandirmada matematiksel olarak esit). "
                   "cross_entropy = saf siniflandirma kaybi (L2 cezasi yok), olasiliklardan hesaplanir.",
    "cross_validation": {"n_splits": CV_KAT, "ortalama": {m: cv_ozet[m]["ort"] for m in OLCUTLER},
                         "std": {m: cv_ozet[m]["std"] for m in OLCUTLER},
                         "katlar": cv[["kat"] + OLCUTLER + ["epoch_sayisi", "en_iyi_epoch"]].to_dict(orient="records")},
    "validation_metrics": sec(test_sonuc, "val_"), "validation_sinif_bazli": sinif_bazli(test_sonuc, "val_"),
    "held_out_test_metrics": sec(test_sonuc), "test_sinif_bazli": sinif_bazli(test_sonuc),
    "held_out_test_guven_araligi_95": test_ga,
    "guven_araligi_yontemi": f"bootstrap, {GA_TEKRAR} tekrar, yuzdelik %2.5-%97.5, seed {GA_SEED}; test tahminleri "
                             f"yerine koyarak yeniden orneklenir (egitim tekrarlanmaz)",
    "test_epoch_sayisi": test_sonuc["epoch_sayisi"], "test_en_iyi_epoch": test_sonuc["en_iyi_epoch"],
    "son_egitim_deneme": test_sonuc["deneme"], "son_egitim_lr": test_sonuc["kullanilan_lr"],
    "son_egitim_sinif_agirligi": json.loads(test_sonuc["sinif_agirligi"]),
    "cv_tekrarlanan_kat": [int(k) for k in cv.loc[cv["deneme"] == 2, "kat"]],
    "son_egitim_sn": test_sonuc["egitim_sn"], "confusion_matrix": cm.tolist(),
}
with open(SONUC_DIR / "sonuc.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n{NAME}  {MODEL_ADI} ({ACTIVATION}, dropout {DROPOUT_RATE}, lr {LEARNING_RATE:g})")
for baslik, d in (("CV ort", {m: cv_ozet[m]["ort"] for m in OLCUTLER}), ("DOGRULAMA", sec(test_sonuc, "val_")),
                  ("TEST", sec(test_sonuc))):
    print(f"{baslik:10s} acc={d['accuracy']:.4f}  F1 w/m/micro={d['f1_weighted']:.4f}/{d['f1_macro']:.4f}/"
          f"{d['f1_micro']:.4f}  P_w={d['precision_weighted']:.4f}  R_w={d['recall_weighted']:.4f}  "
          f"CE={d['cross_entropy']:.4f}  AUC={d['roc_auc']:.4f}  MCC={d['mcc']:.4f}")
print("TEST %95 GA: " + "  ".join(f"{k}=[{v['alt']:.4f}, {v['ust']:.4f}]" for k, v in test_ga.items()))
print(f"Ciktilar: {SONUC_DIR}\n{time.strftime('%Y-%m-%d %H:%M:%S')} BITTI")
