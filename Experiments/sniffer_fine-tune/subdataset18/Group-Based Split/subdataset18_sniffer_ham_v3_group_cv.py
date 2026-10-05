#!/usr/bin/env python3
# subdataset18_sniffer_ham_v3_group_cv
# subdataset18 -- GPTSniffer (CodeBERT) FINE-TUNE -- Ham / V3 -- Group-Based Split
# Calistirma:  python subdataset18_sniffer_ham_v3_group_cv.py --vektor <VEKTOR klasoru> --kod <Duz KODLAR PY klasoru>
#              python subdataset18_sniffer_ham_v3_group_cv.py --sadece-ayrim   (egitim yok, yalniz veri ayrimi)
#              python subdataset18_sniffer_ham_v3_group_cv.py --duman          (kisa duman testi; sonuclar_duman/ altina, sonuclari anlamsiz)
# Gerekenler: torch, transformers, scikit-learn, pandas (Colab'da hazir). GPU sart (CPU'da cok yavas).
# Dosya listesi: VEKTOR\Benzerlik+4o Ml için ayrılmıs  (ML kosulariyla ayni liste ve AYNI veri ayrimi)
# Metinler    : Duz KODLAR PY\GPT4o ayrılmış\<ham|vN>\<kaynak_dosya>
#
# Eski fine-tune scriptine gore degisenler: metin modele verilmeden once iki sinifa AYNI bicim temizligi uygulanir
# (insan dosyalarinda bos satir/yorum silinmis, LLM dosyalarinda silinmemis -> model bu farki ogreniyordu, test F1 1.000);
# ayrim ML kosulariyla ayni (aile anahtari + icerik birlestirme, 70/15/15, 5 katli CV); erken durdurma dogrulama
# cross-entropy'sine gore; sinif agirligi balanced; cokme korumasi; metrikler ve %95 GA ML/CNN ile ayni bicimde;
# model agirliklari KAYDEDILMEZ.
import argparse
import hashlib
import json
import pickle
import platform
import random
import re
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, classification_report, confusion_matrix,
                             log_loss, matthews_corrcoef, precision_recall_fscore_support, roc_auc_score)
from sklearn.model_selection import GroupShuffleSplit, StratifiedGroupKFold, StratifiedKFold, train_test_split
from sklearn.utils.class_weight import compute_class_weight

BETIK_SURUMU = "2026-10-03-ft1"

# =================================================================================================================
# BU KOSUNUN AYARLARI
# =================================================================================================================
NAME = 'subdataset18_sniffer_ham_v3_group_cv'
SUBDATASET = 18
MIMARI = 'sniffer'                 # 'sniffer' = GPTSniffer (CodeBERT), 'sensor' = CodeGPTSensor (UniXcoder)
SINIFLAR = ['ham', 'v3']                # etiket = listedeki sira (0 = ham)
AYRIM = 'group'                     # 'group' = Group-Based Split, 'snippet' = Snippet-Level Split
LLM, PROCESS = 'GPT-4o', '9 = (3)  Sadece Benzerlik(dedup)'
VERI_KLASORU = 'Benzerlik+4o Ml için ayrılmıs'   # VEKTOR altindaki klasor (dosya listesi)
KOD_KLASORU = 'GPT4o ayrılmış'   # Duz KODLAR PY altindaki klasor (metinler)
HARIC_RE = r"^(?:\d+_)?vs[1-5]_"   # ham'da olup adi LLM surumu olan ornekler listeye alinmaz
MIN_ESLESME_ORANI, MAKS_AILE_ORANI = 0.50, 0.75
# =================================================================================================================
TEST_ORANI, VAL_ORANI, IC_VAL_ORANI, CV_KAT, RANDOM_SEED = 0.15, 0.15, 0.15, 5, 42
AYNI_ICERIGI_BIRLESTIR = True
ORAN_TOLERANSI = 0.03
LR, MAKS_EPOCH, PATIENCE, BATCH, MAX_LEN = 2e-5, 5, 2, 16, 512
COKME_ESIGI = 0.95          # dogrulama tahminlerinin >= %95'i tek sinifta ise egitim LR/10 ile 1 kez tekrarlanir
TRIPLET_MARJ = 1.0          # yalniz CodeGPTSensor (kontrastif kayip)
MODEL_HF = {"sniffer": "microsoft/codebert-base", "sensor": "microsoft/unixcoder-base-nine"}[MIMARI]
MIMARI_ADI = {"sniffer": "GPTSniffer", "sensor": "CodeGPTSensor"}[MIMARI]

_p = argparse.ArgumentParser()
_p.add_argument("--sadece-ayrim", action="store_true", help="egitim yok, yalniz veri ayrimi")
_p.add_argument("--duman", action="store_true", help="kisa duman testi: kucuk alt kume, 1 epoch, ayri cikti klasoru")
_p.add_argument("--vektor", help="VEKTOR klasoru (icinde bu subdataset'in vektor klasoru olan)")
_p.add_argument("--kod", help="Duz KODLAR PY klasoru (icinde bu subdataset'in '... ayrilmis' kod klasoru olan)")
_K = _p.parse_args()

KLASOR = {"snippet": "Snippet-Level Split", "group": "Group-Based Split"}
N_SINIF = len(SINIFLAR)
SINIF_ADLARI = ["Ham"] + [s.upper() for s in SINIFLAR[1:]]
GRUP = AYRIM == "group"
if _K.duman:
    MAKS_EPOCH = 1


def _resolve(win_path: str) -> Path:
    if platform.system() == "Windows":
        return Path(win_path)
    m = re.match(r"^([A-Za-z]):\\(.*)$", win_path)
    if m:
        return Path(f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92), '/')}")
    return Path(win_path)


def _bul(adaylar, ne):
    v = next((a for a in adaylar if a.is_dir()), None)
    if v is None:
        sys.exit(f"{ne} bulunamadi. Denenen yollar:\n  " + "\n  ".join(map(str, adaylar)))
    return v


# vektor klasoru yalniz dosya listesi (metadata) ve "birebir ayni icerik" (CodeBERT vektorunun md5'i) icin okunur
# -> veri ayrimi ML (vektor) kosulariyla birebir ayni olur
VEKTOR_KOK = _bul(([_resolve(_K.vektor) / VERI_KLASORU] if _K.vektor else []) +
                  [Path(__file__).resolve().parents[3] / "VEKTÖR" / VERI_KLASORU] +
                  [_resolve(rf"C:\Users\{k}\Desktop\Bitirme\VEKTÖR\{VERI_KLASORU}") for k in ("Murat Çoban", "murat.coban")],
                  "Vektor klasoru")
KOD_KOK = _bul(([_resolve(_K.kod) / KOD_KLASORU] if _K.kod else []) +
               [_resolve(rf"C:\Users\{k}\Desktop\Bitirme çalışması\Kullanılan Veriler\Düz KODLAR PY\{KOD_KLASORU}")
                for k in ("Murat Çoban", "murat.coban")],
               "Kod klasoru")
SONUC_DIR = Path(__file__).resolve().parent / ("sonuclar_duman" if _K.duman else "sonuclar") / NAME
SONUC_DIR.mkdir(parents=True, exist_ok=True)

AYARLAR = {
    "betik_surumu": BETIK_SURUMU, "subdataset": SUBDATASET, "siniflar": SINIFLAR, "ayrim": AYRIM,
    "veri_klasoru": VERI_KLASORU, "kod_klasoru": KOD_KLASORU, "mimari": MIMARI_ADI, "model": MODEL_HF,
    "fine_tuning": "tum ag (encoder + siniflandirma basi)", "lr": LR, "maks_epoch": MAKS_EPOCH, "patience": PATIENCE,
    "batch": BATCH, "max_len": MAX_LEN, "erken_durdurma": "dogrulama cross-entropy, en iyi agirliklar geri yuklenir",
    "kayip": ("cross-entropy (sinif agirlikli)" if MIMARI == "sniffer" else
              f"cross-entropy (sinif agirlikli) + triplet (kosinus uzakligi, marj {TRIPLET_MARJ})"),
    "sinif_agirligi": "balanced", "normallestirme": "iki sinifa ayni: CRLF->LF, tab->4 bosluk, satir sonu bosluklari, "
                                                   "bos satirlar ve yalniz yorumdan olusan satirlar silinir, tek satir sonu",
    "cokme_korumasi": f">= %{int(100 * COKME_ESIGI)} tek sinif -> LR/10 ile 1 kez tekrar",
    "test_orani": TEST_ORANI, "val_orani": VAL_ORANI, "ic_val_orani": IC_VAL_ORANI, "cv_kat": CV_KAT,
    "seed": RANDOM_SEED, "haric_re": HARIC_RE,
    "min_eslesme": MIN_ESLESME_ORANI if GRUP else None, "maks_aile": MAKS_AILE_ORANI if GRUP else None,
    "duman_testi": bool(_K.duman),
}
AYAR_OZETI = hashlib.md5(json.dumps(AYARLAR, sort_keys=True).encode()).hexdigest()[:12]


class _Tee:
    def __init__(self, akim, dosya):
        self.akim, self.dosya = akim, dosya

    def write(self, s):
        self.akim.write(s)
        self.dosya.write(s)
        self.dosya.flush()

    def flush(self):
        self.akim.flush()
        self.dosya.flush()

    def isatty(self):          # ilerleme cubuklari (tqdm / transformers) bunu sorar
        return False

    def __getattr__(self, ad):  # diger her ozellik (fileno, encoding ...) asil akistan
        return getattr(self.akim, ad)


_log = open(SONUC_DIR / "calisma.log", "a", encoding="utf-8")
sys.stdout = _Tee(sys.stdout, _log)
sys.stderr = _Tee(sys.stderr, _log)
print(f"\n{'=' * 100}\n{time.strftime('%Y-%m-%d %H:%M:%S')}  {NAME}  (ayar ozeti {AYAR_OZETI})")

if (SONUC_DIR / "sonuc.json").exists() and not _K.sadece_ayrim:
    print("sonuc.json zaten var -> bu kosu tamamlanmis, atlaniyor. Yeniden kosmak icin klasoru silin:", SONUC_DIR)
    sys.exit(0)
AYAR_DOSYA = SONUC_DIR / "ayarlar.json"
if AYAR_DOSYA.exists():
    eski = json.loads(AYAR_DOSYA.read_text(encoding="utf-8"))
    if eski.get("ayar_ozeti") != AYAR_OZETI:
        sys.exit(f"DURDU: bu klasordeki onceki kosu FARKLI ayarlarla yapilmis ({eski.get('ayar_ozeti')} != {AYAR_OZETI}). "
                 f"Klasoru silin ya da tasiyin: {SONUC_DIR}")
AYAR_DOSYA.write_text(json.dumps({**AYARLAR, "ayar_ozeti": AYAR_OZETI}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Liste : {VEKTOR_KOK}")
print(f"Kod   : {KOD_KOK}")
print(f"Model : {MIMARI_ADI} ({MODEL_HF})  lr {LR}  epoch <= {MAKS_EPOCH}  patience {PATIENCE}  batch {BATCH}")
print(f"Cikti : {SONUC_DIR}")


# ---------------------------------------------------------------------------------------------------------------
# Dosya listesi (VEKTOR metadata'si = ML kosularinin kullandigi liste) + kod metinleri + normallestirme
# ---------------------------------------------------------------------------------------------------------------
def pkl_oku(yol):
    with open(yol, "rb") as f:
        return pickle.load(f)


def normallestir(kod):
    """Iki sinifa AYNI bicim temizligi. Insan dosyalarinda veri hazirlanirken bos satirlar/yorumlar silinmis ve
    sona satir sonu eklenmis, LLM dosyalarinda degil; bu temizlik o farki modelin goremeyecegi hale getirir."""
    kod = kod.replace("\r\n", "\n").replace("\r", "\n")
    satirlar = []
    for s in kod.split("\n"):
        s = s.replace("\t", "    ").rstrip()
        if not s.strip() or s.lstrip().startswith("#"):
            continue
        satirlar.append(s)
    return "\n".join(satirlar) + "\n"


ad_parca, et_parca, ic_parca, yol_parca = [], [], [], []
for k, s in enumerate(SINIFLAR):
    d = VEKTOR_KOK / f"{s}vektor"
    meta, icv = d / f"metadata_{s}.csv", d / "codebert" / f"{s}_vectors.pkl"
    for yol in (meta, icv):
        assert yol.is_file(), f"Dosya bulunamadi: {yol}"
    m, iv = pd.read_csv(meta), pkl_oku(icv)
    assert "kaynak_dosya" in m.columns, f"{meta}: 'kaynak_dosya' sutunu yok (eski VEKTOR klasoru mu yuklendi?)"
    assert len(m) == len(iv), f"{s}: vektor/metadata satir sayisi farkli"
    ad_parca += list(m["filename"])
    yol_parca += [KOD_KOK / s / str(kd) for kd in m["kaynak_dosya"]]
    et_parca.append(np.full(len(m), k))
    ic_parca.append(iv)
dosya_adlari = [str(a) for a in ad_parca]
labels = np.concatenate(et_parca).astype(int)
# "birebir ayni icerik" = CodeBERT vektorunun md5'i (ML kosulariyla ayni olcut -> ayni aileler, ayni ayrim)
icerikler = np.array([hashlib.md5(np.ascontiguousarray(r).tobytes()).hexdigest() for r in np.vstack(ic_parca)])
eksik = [str(p) for p in yol_parca if not p.is_file()]
assert not eksik, f"{len(eksik)} kod dosyasi bulunamadi, ornek: {eksik[:3]}"

haric = []
if HARIC_RE:
    tut = np.array([not (lab == 0 and re.match(HARIC_RE, ad)) for ad, lab in zip(dosya_adlari, labels)])
    haric = [ad for ad, t in zip(dosya_adlari, tut) if not t]
    labels, icerikler = labels[tut], icerikler[tut]
    dosya_adlari = [ad for ad, t in zip(dosya_adlari, tut) if t]
    yol_parca = [p for p, t in zip(yol_parca, tut) if t]
    print(f"Ham'da olup adi LLM surumu olan {len(haric)} ornek ALINMADI (veri degismez): {haric}")
n = len(labels)
for k, ad in enumerate(SINIF_ADLARI):
    print(f"{ad:3s} (etiket {k}): {int((labels == k).sum())} ornek")
print(f"Toplam {n} ornek")


def dagilim(ix):
    return " ".join(f"{ad}={int((labels[ix] == k).sum())}" for k, ad in enumerate(SINIF_ADLARI))


# ---------------------------------------------------------------------------------------------------------------
# Veri ayrimi (ML ve goruntu kodlariyla ayni kural)
# ---------------------------------------------------------------------------------------------------------------
idx_all = np.arange(n)
aile_bilgi = {}
families = anahtarlar = None
if GRUP:
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
    supheli = [ad for ad, e, s in zip(dosya_adlari, labels, ad_surumleri)
               if (e == 0 and s is not None) or (e != 0 and s != SINIFLAR[e].lstrip("v"))]
    aile_bilgi["klasor_ad_surumu_uyusmayan_dosya"] = len(supheli)
    print(f"Klasoru ile adindaki surum etiketi uyusmayan ornek (veri degistirilmez): {len(supheli)}")

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
else:
    dev_idx, test_idx = train_test_split(idx_all, test_size=TEST_ORANI, random_state=RANDOM_SEED, stratify=labels)
    train_idx, val_idx = train_test_split(dev_idx, test_size=VAL_ORANI / (1.0 - TEST_ORANI),
                                          random_state=RANDOM_SEED, stratify=labels[dev_idx])
    skf = StratifiedKFold(n_splits=CV_KAT, shuffle=True, random_state=RANDOM_SEED)
    cv_katlari = [(dev_idx[tr], dev_idx[va]) for tr, va in skf.split(dev_idx, labels[dev_idx])]
    for a, b in ((train_idx, val_idx), (train_idx, test_idx), (val_idx, test_idx)):
        assert not set(a.tolist()) & set(b.tolist()), "kumeler ayni ornegi iceriyor"

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


def ic_dogrulama_ayir(egitim_idx, kat):
    """Erken durdurma icin egitim kumesinden %15 ic dogrulama (aile bazli ayrimda aile bazli)."""
    if GRUP:
        gss = GroupShuffleSplit(n_splits=1, test_size=IC_VAL_ORANI, random_state=RANDOM_SEED + kat)
        a, b = next(gss.split(egitim_idx, labels[egitim_idx], groups=families[egitim_idx]))
        return egitim_idx[a], egitim_idx[b]
    a, b = train_test_split(egitim_idx, test_size=IC_VAL_ORANI, random_state=RANDOM_SEED + kat,
                            stratify=labels[egitim_idx])
    return a, b


if _K.duman:   # yalniz kod yolunu denemek icin: her kumeden kucuk, iki sinifli alt kume
    _rng = np.random.default_rng(0)

    def _kucult(ix, adet):
        return np.concatenate([_rng.permutation(ix[labels[ix] == k])[:adet // N_SINIF] for k in range(N_SINIF)])

    cv_katlari = [(_kucult(tr, 48), _kucult(va, 16)) for tr, va in cv_katlari[:2]]
    train_idx, val_idx, test_idx = _kucult(train_idx, 48), _kucult(val_idx, 16), _kucult(test_idx, 16)
    CV_KAT = 2
    print("DUMAN TESTI: 2 kat, kucuk alt kumeler, 1 epoch (sonuclar anlamsizdir)")

# ---------------------------------------------------------------------------------------------------------------
# Metinler: oku -> normallestir -> bir kez tokenize et
# ---------------------------------------------------------------------------------------------------------------
import torch                                    # noqa: E402  (veri ayrimi torch'suz da calissin)
import torch.nn.functional as F                 # noqa: E402
from transformers import AutoModel, AutoModelForSequenceClassification, AutoTokenizer  # noqa: E402
from transformers import get_linear_schedule_with_warmup  # noqa: E402
from transformers.utils import logging as _hf_log  # noqa: E402

_hf_log.set_verbosity_error()
CIHAZ = "cuda" if torch.cuda.is_available() else "cpu"
if CIHAZ == "cuda":
    print(f"GPU: {torch.cuda.get_device_name(0)}  torch {torch.__version__}")
    AMP_TIP = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
else:
    print(f"UYARI: GPU yok, CPU'da cok yavas olur  torch {torch.__version__}")
    AMP_TIP = None

kullanilan = np.unique(np.concatenate([train_idx, val_idx, test_idx] + [np.concatenate(k) for k in cv_katlari]))
ham_metin = {int(i): yol_parca[i].read_bytes().decode("utf-8", errors="ignore") for i in kullanilan}
metin = {i: normallestir(t) for i, t in ham_metin.items()}
norm_bilgi = {
    "degisen_dosya": int(sum(metin[i] != t for i, t in ham_metin.items())),
    "bos_dosya": int(sum(not t.strip() for t in ham_metin.values())),
    "ortalama_satir_once": float(np.mean([t.count("\n") + 1 for t in ham_metin.values()])),
    "ortalama_satir_sonra": float(np.mean([t.count("\n") for t in metin.values()])),
}
print(f"Normallestirme: {norm_bilgi}")
del ham_metin
tok = AutoTokenizer.from_pretrained(MODEL_HF)
_sira = sorted(metin)
_enc = tok([metin[i] for i in _sira], truncation=True, max_length=MAX_LEN)
TOKEN = {i: ids for i, ids in zip(_sira, _enc["input_ids"])}
norm_bilgi["max_len_ile_kesilen"] = int(sum(len(v) >= MAX_LEN for v in TOKEN.values()))
PAD = tok.pad_token_id
del metin, _enc


def yigin(ix):
    """Dinamik dolgu (batch icindeki en uzun ornege kadar); maske dolguyu modelden gizler."""
    uz = max(len(TOKEN[int(i)]) for i in ix)
    ids = torch.full((len(ix), uz), PAD, dtype=torch.long)
    maske = torch.zeros((len(ix), uz), dtype=torch.long)
    for r, i in enumerate(ix):
        t = TOKEN[int(i)]
        ids[r, :len(t)] = torch.tensor(t)
        maske[r, :len(t)] = 1
    return ids.to(CIHAZ), maske.to(CIHAZ), torch.as_tensor(labels[np.asarray(ix)], device=CIHAZ)


class CodeGPTSensor(torch.nn.Module):
    """UniXcoder encoder + attention-mask'li ortalama pooling + dogrusal siniflandirma katmani."""

    def __init__(self, ad):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(ad)
        self.classifier = torch.nn.Linear(self.encoder.config.hidden_size, N_SINIF)

    def forward(self, input_ids, attention_mask):
        h = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        m = attention_mask.unsqueeze(-1).to(h.dtype)
        emb = (h * m).sum(1) / m.sum(1).clamp(min=1e-9)
        return emb, self.classifier(emb)


def model_kur():
    torch.manual_seed(RANDOM_SEED)
    if MIMARI == "sniffer":
        return AutoModelForSequenceClassification.from_pretrained(MODEL_HF, num_labels=N_SINIF).to(CIHAZ)
    return CodeGPTSensor(MODEL_HF).to(CIHAZ)


def ileri(model, ids, maske):
    """(gomme ya da None, logits)"""
    with torch.autocast("cuda", dtype=AMP_TIP, enabled=AMP_TIP is not None):
        if MIMARI == "sniffer":
            return None, model(input_ids=ids, attention_mask=maske).logits
        return model(ids, maske)


@torch.no_grad()
def olasilik(model, ix):
    model.eval()
    sira = np.argsort([len(TOKEN[int(i)]) for i in ix])        # benzer uzunluklar ayni batch'te -> hizli
    cikti = np.zeros((len(ix), N_SINIF), dtype="float64")
    for b in range(0, len(ix), BATCH * 2):
        parca = sira[b:b + BATCH * 2]
        ids, maske, _ = yigin(np.asarray(ix)[parca])
        _, logits = ileri(model, ids, maske)
        cikti[parca] = torch.softmax(logits.float(), dim=1).cpu().numpy()
    return cikti


def egit(egitim_idx, kat, gecmis_etiketi):
    """Tum agi fine-tune eder; ic dogrulama cross-entropy'sine gore erken durdurma, en iyi agirliklar geri yuklenir.
    Donen: (model, bilgi)"""
    tr_idx, ic_val_idx = ic_dogrulama_ayir(egitim_idx, kat)
    agirlik = torch.tensor(compute_class_weight("balanced", classes=np.arange(N_SINIF), y=labels[tr_idx]),
                           dtype=torch.float32, device=CIHAZ)
    bilgi = {"n_egitim": len(tr_idx), "n_ic_dogrulama": len(ic_val_idx)}
    for deneme, lr in enumerate((LR, LR / 10), start=1):
        model = model_kur()
        opt = torch.optim.AdamW(model.parameters(), lr=lr)
        adim = MAKS_EPOCH * int(np.ceil(len(tr_idx) / BATCH))
        sched = get_linear_schedule_with_warmup(opt, num_warmup_steps=0, num_training_steps=adim)
        scaler = torch.amp.GradScaler("cuda", enabled=AMP_TIP == torch.float16)
        rng = np.random.default_rng(RANDOM_SEED + 100 * kat + deneme)
        en_iyi, en_iyi_epoch, en_iyi_durum, kotu = np.inf, 0, None, 0
        for epoch in range(1, MAKS_EPOCH + 1):
            t0 = time.time()
            model.train()
            toplam, say = 0.0, 0
            karisik = rng.permutation(tr_idx)
            for b in range(0, len(karisik), BATCH):
                ids, maske, y = yigin(karisik[b:b + BATCH])
                emb, logits = ileri(model, ids, maske)
                kayip = F.cross_entropy(logits.float(), y, weight=agirlik)
                if MIMARI == "sensor":
                    # kontrastif terim: ayni ornegin ikinci (farkli dropout) gecisi pozitif, batch'teki farkli sinif negatif
                    emb2, _ = ileri(model, ids, maske)
                    y_np = y.cpu().numpy()
                    neg = np.array([rng.choice(np.where(y_np != c)[0]) if (y_np != c).any() else -1 for c in y_np])
                    gecerli = neg >= 0
                    if gecerli.any():
                        g = torch.as_tensor(gecerli, device=CIHAZ)
                        kayip = kayip + F.triplet_margin_with_distance_loss(
                            emb[g].float(), emb2[g].float(), emb[torch.as_tensor(neg[gecerli], device=CIHAZ)].float(),
                            distance_function=lambda a, b: 1.0 - F.cosine_similarity(a, b, dim=-1), margin=TRIPLET_MARJ)
                opt.zero_grad(set_to_none=True)
                scaler.scale(kayip).backward()
                scaler.unscale_(opt)
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                scaler.step(opt)
                scaler.update()
                sched.step()
                toplam += float(kayip.detach()) * len(y)
                say += len(y)
            p = olasilik(model, ic_val_idx)
            y_val = labels[ic_val_idx]
            val_ce = float(log_loss(y_val, p, labels=list(range(N_SINIF))))
            tah = p.argmax(1)
            satir = {"egitim": gecmis_etiketi, "deneme": deneme, "lr": lr, "epoch": epoch, "train_loss": toplam / say,
                     "val_ce": val_ce, "val_accuracy": float(accuracy_score(y_val, tah)),
                     "val_f1_weighted": float(precision_recall_fscore_support(y_val, tah, average="weighted",
                                                                              zero_division=0)[2]),
                     "sure_sn": round(time.time() - t0, 1)}
            ekle_csv(pd.DataFrame([satir]), SONUC_DIR / "egitim_gecmisi.csv")
            print(f"  [{gecmis_etiketi} d{deneme}] epoch {epoch}: train_loss={satir['train_loss']:.4f}  val_ce={val_ce:.4f}  "
                  f"val_acc={satir['val_accuracy']:.4f}  val_F1w={satir['val_f1_weighted']:.4f}  {satir['sure_sn']} sn",
                  flush=True)
            if val_ce < en_iyi:
                en_iyi, en_iyi_epoch, kotu = val_ce, epoch, 0
                en_iyi_durum = {k: v.detach().to("cpu", copy=True) for k, v in model.state_dict().items()}
            else:
                kotu += 1
                if kotu >= PATIENCE:
                    print(f"  erken durdurma (val_ce {PATIENCE} epoch iyilesmedi)", flush=True)
                    break
        model.load_state_dict(en_iyi_durum)
        tek_sinif_orani = float(np.bincount(olasilik(model, ic_val_idx).argmax(1), minlength=N_SINIF).max()
                                / len(ic_val_idx))
        bilgi.update({"deneme": deneme, "lr": lr, "en_iyi_epoch": en_iyi_epoch, "en_iyi_val_ce": en_iyi,
                      "tek_sinif_orani": tek_sinif_orani})
        if tek_sinif_orani < COKME_ESIGI or deneme == 2:
            break
        print(f"  COKME: ic dogrulama tahminlerinin %{100 * tek_sinif_orani:.0f}'i tek sinifta -> LR/10 ile tekrar",
              flush=True)
        del model, opt
        torch.cuda.empty_cache()
    return model, bilgi


def metrikler(y_true, y_pred, prob):
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
        m["roc_auc"] = float(roc_auc_score(y_true, prob[:, 1]))
    except ValueError:
        m["roc_auc"] = float("nan")
    return m


def tahmin(model, ix):
    prob = olasilik(model, ix)
    return prob.argmax(1).astype(int), prob


def tahmin_tablosu(ix, y_pred, prob, egitim):
    t = pd.DataFrame({"egitim": egitim, "dosya": [dosya_adlari[i] for i in ix], "gercek": labels[ix], "tahmin": y_pred})
    for k, ad in enumerate(SINIF_ADLARI):
        t[f"olasilik_{ad}"] = prob[:, k]
    return t


def ekle_csv(df, yol, sutunlar=None):
    if sutunlar is not None:
        df = df.reindex(columns=sutunlar)
    df.to_csv(yol, mode="a", header=not yol.exists(), index=False)


_ornek = metrikler(np.arange(N_SINIF), np.arange(N_SINIF), np.eye(N_SINIF))
BILGI_SUTUN = ["n_egitim", "n_ic_dogrulama", "deneme", "lr", "en_iyi_epoch", "en_iyi_val_ce", "tek_sinif_orani"]
CV_SUTUNLAR = ["kat", "n_degerlendirme"] + list(_ornek) + BILGI_SUTUN + ["sure_sn", "hata"]

# ---- 5 katli CV (tamamlanan katlar atlanir) ----
CV_CSV = SONUC_DIR / "cv_kat_sonuclari.csv"
tamamlanan = set()
if CV_CSV.exists():
    onceki = pd.read_csv(CV_CSV)
    onceki = onceki[onceki["hata"].isna() | (onceki["hata"].astype(str).str.strip() == "")]
    tamamlanan = set(int(k) for k in onceki["kat"])
    print(f"Onceden tamamlanmis katlar: {sorted(tamamlanan)} (atlanacak)")
for kat, (kat_egitim_idx, kat_deger_idx) in enumerate(cv_katlari, start=1):
    if kat in tamamlanan:
        continue
    print(f"\n===== Kat {kat}/{CV_KAT}  {time.strftime('%H:%M:%S')} =====", flush=True)
    satir = {"kat": kat, "n_degerlendirme": len(kat_deger_idx)}
    t0 = time.time()
    try:
        model, bilgi = egit(kat_egitim_idx, kat, f"kat{kat}")
        y_pred, prob = tahmin(model, kat_deger_idx)
        satir.update(metrikler(labels[kat_deger_idx], y_pred, prob))
        satir.update({**bilgi, "hata": ""})
        ekle_csv(tahmin_tablosu(kat_deger_idx, y_pred, prob, f"kat{kat}"), SONUC_DIR / "tahminler_cv.csv")
        del model
    except Exception as e:
        import traceback
        traceback.print_exc()          # hatanin tam yeri loga yazilsin
        hata = f"{type(e).__name__}: {e}"
        satir["hata"] = hata if len(hata) <= 600 else hata[:300] + " ... " + hata[-300:]
    if CIHAZ == "cuda":
        torch.cuda.empty_cache()
    satir["sure_sn"] = round(time.time() - t0, 1)
    ekle_csv(pd.DataFrame([satir]), CV_CSV, CV_SUTUNLAR)
    print(f"Kat {kat}: accuracy={satir.get('accuracy', float('nan')):.4f}  "
          f"F1(w/m)={satir.get('f1_weighted', float('nan')):.4f}/{satir.get('f1_macro', float('nan')):.4f}  "
          f"{satir['sure_sn']} sn  {satir['hata']}", flush=True)

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

# ---- Son egitim: %70 egitim (icinden %15 erken durdurma) -> %15 testte bir kez (ve %15 dogrulamada) ----
print(f"\n===== Son egitim  {time.strftime('%H:%M:%S')} =====", flush=True)
t0 = time.time()
son_model, son_bilgi = egit(train_idx, 0, "son")
test_pred, test_prob = tahmin(son_model, test_idx)
val_pred, val_prob = tahmin(son_model, val_idx)
test_m = metrikler(labels[test_idx], test_pred, test_prob)
val_m = metrikler(labels[val_idx], val_pred, val_prob)
pd.concat([tahmin_tablosu(test_idx, test_pred, test_prob, "test"),
           tahmin_tablosu(val_idx, val_pred, val_prob, "dogrulama")]).to_csv(SONUC_DIR / "tahminler.csv", index=False,
                                                                             encoding="utf-8-sig")
print(f"Son egitim: {son_bilgi}  {time.time() - t0:.0f} sn")
print(classification_report(labels[test_idx], test_pred, target_names=SINIF_ADLARI, zero_division=0, digits=4))
cm = confusion_matrix(labels[test_idx], test_pred, labels=list(range(N_SINIF)))
pd.DataFrame(cm, index=SINIF_ADLARI, columns=SINIF_ADLARI).to_csv(SONUC_DIR / "confusion_matrix.csv")
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(4 + N_SINIF, 3 + N_SINIF))
    ax.imshow(cm, cmap="Blues")
    for i in range(N_SINIF):
        for j in range(N_SINIF):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center")
    ax.set_xticks(range(N_SINIF), SINIF_ADLARI)
    ax.set_yticks(range(N_SINIF), SINIF_ADLARI)
    ax.set_xlabel("Tahmin")
    ax.set_ylabel("Gercek")
    ax.set_title(f"{NAME}\n{MIMARI_ADI} (fine-tune) - Confusion Matrix (held-out test)")
    plt.tight_layout()
    plt.savefig(SONUC_DIR / "confusion_matrix.png", dpi=150)
    plt.close(fig)
except Exception as e:      # grafik zorunlu degil; CSV kaydedildi
    print("confusion_matrix.png cizilemedi:", e)

GA_TEKRAR, GA_SEED = 1000, 42


def bootstrap_ga(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
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


test_ga = bootstrap_ga(labels[test_idx], test_pred)
kume_dagilim = {"tum": sinif_dagilimi(idx_all), "train": sinif_dagilimi(train_idx), "val": sinif_dagilimi(val_idx),
                "test": sinif_dagilimi(test_idx)}
for ad, d in kume_dagilim.items():
    print(f"Sinif dagilimi {ad:5s}: {d['sayi']}  oran {d['oran']}")
sec = lambda d: {m: d[m] for m in OLCUTLER}  # noqa: E731
sinif_bazli = lambda d: {ad: {k: d[f"{k}_{ad}"] for k in ("precision", "recall", "f1", "destek")}  # noqa: E731
                         for ad in SINIF_ADLARI}
import transformers  # noqa: E402
result = {
    "kosu": NAME, "ayar_ozeti": AYAR_OZETI, "ayarlar": AYARLAR,
    "surumler": {"torch": torch.__version__, "transformers": transformers.__version__, "sklearn": sklearn.__version__,
                 "gpu": torch.cuda.get_device_name(0) if CIHAZ == "cuda" else "cpu"},
    "subdataset": SUBDATASET, "llm": LLM, "process_id_aciklama": PROCESS, "mimari": MIMARI_ADI, "model": MODEL_HF,
    "siniflar": {ad: k for k, ad in enumerate(SINIF_ADLARI)},
    "veri": {**{s: int((labels == k).sum()) for k, s in enumerate(SINIFLAR)}, "toplam": n, "haric_tutulan": haric},
    "normallestirme": norm_bilgi,
    "split": {"train": len(train_idx), "val": len(val_idx), "test": len(test_idx),
              "yontem": ("aile bazli: iki asamali GroupShuffleSplit 70/15/15, CV StratifiedGroupKFold" if GRUP else
                         "stratified rastgele 70/15/15, CV StratifiedKFold") + ", random_state=42 (ML kosulariyla ayni)",
              "ic_dogrulama": f"her egitimde egitim kumesinin %{int(100 * IC_VAL_ORANI)}'i erken durdurma icin "
                              f"({'aile bazli' if GRUP else 'stratified'})"},
    "kume_sinif_dagilimi": kume_dagilim, "aile": aile_bilgi,
    "metrik_notu": "micro P = micro R = micro F1 = accuracy (tek etiketli siniflandirmada esit). Tahmin = en yuksek "
                   "softmax olasiligi; cross_entropy ve AUC softmax olasiliklarindan.",
    "cross_validation": {"n_splits": CV_KAT, "ortalama": {m: cv_ozet[m]["ort"] for m in OLCUTLER},
                         "std": {m: cv_ozet[m]["std"] for m in OLCUTLER},
                         "katlar": cv[["kat"] + OLCUTLER + BILGI_SUTUN].to_dict(orient="records")},
    "son_egitim": son_bilgi,
    "validation_metrics": sec(val_m), "validation_sinif_bazli": sinif_bazli(val_m),
    "held_out_test_metrics": sec(test_m), "test_sinif_bazli": sinif_bazli(test_m),
    "held_out_test_guven_araligi_95": test_ga,
    "guven_araligi_yontemi": f"bootstrap, {GA_TEKRAR} tekrar, yuzdelik %2.5-%97.5, seed {GA_SEED}; test tahminleri "
                             f"yerine koyarak yeniden orneklenir",
    "confusion_matrix": cm.tolist(),
}
with open(SONUC_DIR / "sonuc.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"\n{NAME}  {MIMARI_ADI} (fine-tune)")
for baslik, d in (("CV ort", {m: cv_ozet[m]["ort"] for m in OLCUTLER}), ("DOGRULAMA", val_m), ("TEST", test_m)):
    print(f"{baslik:10s} acc={d['accuracy']:.4f}  F1 w/m/micro={d['f1_weighted']:.4f}/{d['f1_macro']:.4f}/"
          f"{d['f1_micro']:.4f}  P_w={d['precision_weighted']:.4f}  R_w={d['recall_weighted']:.4f}  "
          f"CE={d['cross_entropy']:.4f}  AUC={d['roc_auc']:.4f}  MCC={d['mcc']:.4f}")
print("TEST %95 GA: " + "  ".join(f"{k}=[{v['alt']:.4f}, {v['ust']:.4f}]" for k, v in test_ga.items()))
print(f"Ciktilar: {SONUC_DIR}\n{time.strftime('%Y-%m-%d %H:%M:%S')} BITTI")
