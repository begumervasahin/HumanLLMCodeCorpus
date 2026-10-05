# -*- coding: utf-8 -*-
"""
Reviewer #4, Concern #1 -- insan / GPT-3.5 / GPT-4o kodlarinin STIL metrikleri (surum 3, sade)

"Please align the paper with its title by reporting actual style metrics for human, GPT-3.5 and GPT-4o code,
 for example lines of code, comment ratio, identifier naming patterns, nesting depth and cyclomatic complexity,
 with significance tests."

v2'den farki: yalniz hakemin saydigi metrikler (+ fonksiyon sayisi) tutuldu, GPT-3.5 - GPT-4o testi ve bootstrap
guven araliklari cikarildi, cikti iki tablo + bir sekle indirildi. Veri, eslestirme ve temizleme v2 ile ayni.

METRIKLER (9)
  Lines of code      : SLOC (bos ve yalniz yorum olan satirlar haric)
  Comment ratio      : yorum iceren satir / bos olmayan satir.  Insan kodlarindan yorumlar veri hazirliginda
                       silindigi icin insan - LLM testi YAPILMAZ, yalniz betimsel verilir.
                       Docstring coverage: docstring'li def/class orani (docstring'ler silinmemis -> test edilir)
  Identifier naming  : ortalama tanimlayici uzunlugu, tek harfli ad orani, snake_case orani
                       (tanimlayici = dosyada tanimlanan fonksiyon, sinif, degisken ve parametre adlari)
  Nesting depth      : en derin if/for/while/try/with ic iceligi (def/class sayilmaz)
  Cyclomatic compl.  : fonksiyon basina ortalama CCN (Lizard); yaninda dosya basina fonksiyon sayisi

YONTEM
  Veri       : Duz KODLAR PY\\gpt3.5 ayrilmis ve GPT4o ayrilmis (Ham + V1..V5).
  Eslestirme : her insan dosyasi kendi V1..V5 surumleriyle eslesir (dosya adindaki <sira>_content_<govde>).
               Ayni anahtar birden fazla dosyada varsa adindaki surum etiketi klasoruyle uyan tek dosya tutulur.
  Ayristirma : Python tokenize (Python 2 kodunu da okur) + Lizard. utf-8-sig, CRLF -> LF, sekme -> 8 sutun,
               'README Content:' satirindan sonrasi atilir. Islenemeyen dosyalar kapsam tablosunda.
  Istatistik : eslestirilmis Wilcoxon signed-rank (iki yonlu) + matched-pairs rank-biserial r (+ = LLM daha yuksek),
               tum testlere birlikte Holm duzeltmesi. Sifirdan farkli cift < 10 ise test yapilmaz.
               |r| < 0.1 ihmal edilebilir, 0.1-0.3 kucuk, 0.3-0.5 orta, >= 0.5 buyuk.

Calistirma: py -3.13 R4_C1_stil_metrikleri_v3.py      (gerekenler: lizard, scipy, pandas, matplotlib, openpyxl)
Cikti     : sonuclar_stil_v3\\
"""
import io
import keyword
import re
import sys
import time
import tokenize
import unicodedata
import warnings
from pathlib import Path

import lizard
import numpy as np
import pandas as pd
from scipy.stats import rankdata, wilcoxon

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VERI = Path(r"C:\Users\Murat Çoban\Desktop\Bitirme çalışması\Kullanılan Veriler\Düz KODLAR PY")
LLMLER = {"GPT-3.5": VERI / "gpt3.5 ayrılmış", "GPT-4o": VERI / "GPT4o ayrılmış"}
GRUPLAR = ["ham", "v1", "v2", "v3", "v4", "v5"]
CIKTI = Path(__file__).resolve().parent / "sonuclar_stil_v3"
HARIC_RE = re.compile(r"^(?:\d+_)?vs[1-5]_")          # ham klasorunde olup adi LLM surumu olan dosyalar
AD_RE = re.compile(r"^(?:(?P<dis>\d+)_)?(?:vs?(?P<surum>[1-5])_?\s*)*(?P<sira>\d+)_content_(?P<govde>.+)$")
ETIKET_RE = re.compile(r"^(?:\d+_)?((?:vs?[1-5]_?\s*)*)\d+_content_")

KONTROL = {"if", "elif", "else", "for", "while", "try", "except", "finally", "with"}
ATAMA = {"=", "+=", "-=", "*=", "/=", "//=", "%=", "**=", ">>=", "<<=", "&=", "^=", "|=", "@="}
ACAN, KAPAYAN = set("([{"), set(")]}")
ANLAMSIZ = {tokenize.NL, tokenize.COMMENT, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT,
            tokenize.ENDMARKER, tokenize.ENCODING}
KW = set(keyword.kwlist) | {"print", "exec"}          # Python 2'de print/exec anahtar kelime
SNAKE = re.compile(r"^_*[a-z][a-z0-9]*(_[a-z0-9]+)*_*$")

# (anahtar, makaledeki ad, insan-LLM testi yapilir mi)
METRIKLER = [
    ("sloc", "Lines of code (SLOC)", True),
    ("comment_ratio", "Comment ratio", False),
    ("docstring_coverage", "Docstring coverage", True),
    ("avg_id_len", "Avg. identifier length", True),
    ("single_letter_ratio", "Single-letter identifier ratio", True),
    ("snake_ratio", "snake_case ratio", True),
    ("max_nesting", "Max. nesting depth", True),
    ("avg_ccn", "Avg. cyclomatic complexity", True),
    ("n_functions", "Functions per file", True),
]
ANAHTAR = [m[0] for m in METRIKLER]
AD = {m[0]: m[1] for m in METRIKLER}
TEST = {m[0]: m[2] for m in METRIKLER}


# --------------------------------------------------------------------------------------------------------------
# Dosya listesi ve eslestirme anahtari
# --------------------------------------------------------------------------------------------------------------
def aile_anahtari(dosya_adi):
    ad = unicodedata.normalize("NFC", dosya_adi).split("__", 1)[-1]
    ad = re.sub(r"\.(txt|py)$", "", ad.strip(), flags=re.IGNORECASE)
    m = AD_RE.match(ad)
    if not m:
        return None
    govde = re.sub(r"(?:\.py\w*)+$", "", m.group("govde"), flags=re.IGNORECASE)
    return re.sub(r"\s+", "", govde).lower()


def dosyalari_listele():
    satirlar = []
    for llm, kok in LLMLER.items():
        for g in GRUPLAR:
            for f in sorted((kok / g).iterdir()):
                if not f.is_file():
                    continue
                ad = unicodedata.normalize("NFC", f.name)
                konu, _, kalan = ad.partition("__")
                satirlar.append({"llm": llm, "grup": g, "konu": konu, "dosya": ad, "yol": f,
                                 "anahtar": aile_anahtari(ad),
                                 "haric": g == "ham" and bool(HARIC_RE.match(kalan))})
    return pd.DataFrame(satirlar)


def surum_etiketleri(dosya):
    """'v1_v2_25_content_...' -> ('1', '2'); insan -> ()."""
    kalan = unicodedata.normalize("NFC", dosya).split("__", 1)[-1]
    m = ETIKET_RE.match(kalan)
    return tuple(re.findall(r"vs?([1-5])", m.group(1))) if m else None


def eslestirme_icin_tekille(df):
    """Her (llm, grup, konu, anahtar) icin TEK dosya: tekrar varsa surum etiketi klasoruyle birebir uyan tek dosya
    tutulur, yoksa o anahtarin tum dosyalari cikarilir."""
    t = df.copy()
    t["_etiket"] = t["dosya"].map(surum_etiketleri)
    t["_beklenen"] = t["grup"].map(lambda g: () if g == "ham" else (g[1],))
    tut, rapor = [], []
    for (llm, grup), alt in t.groupby(["llm", "grup"], sort=False):
        a = alt[alt["anahtar"].notna()]
        sayi = a.groupby(["konu", "anahtar"])["dosya"].transform("size")
        tek, cok = a[sayi == 1], a[sayi > 1]
        uyan = cok[pd.Series([e == b for e, b in zip(cok["_etiket"], cok["_beklenen"])], index=cok.index, dtype=bool)]
        uyan = uyan[uyan.groupby(["konu", "anahtar"])["dosya"].transform("size") == 1]
        tut += [tek, uyan]
        rapor.append({"llm": llm, "group": grup_adi(grup), "files": len(alt),
                      "removed_duplicates_or_no_key": len(alt) - len(tek) - len(uyan),
                      "matching_candidates": len(tek) + len(uyan)})
    return pd.concat(tut).drop(columns=["_etiket", "_beklenen"]), pd.DataFrame(rapor)


def grup_adi(g):
    return "Human" if g == "ham" else g.upper()


# --------------------------------------------------------------------------------------------------------------
# Metrikler
# --------------------------------------------------------------------------------------------------------------
def mantiksal_satirlar(toks):
    """(satir_tokenlari, parantez_derinlikleri) -- NEWLINE'a kadar anlamli tokenlar."""
    satir, derin, d = [], [], 0
    for t in toks:
        if t.type == tokenize.NEWLINE:
            if satir:
                yield satir, derin
            satir, derin, d = [], [], 0
            continue
        if t.type in ANLAMSIZ:
            continue
        if t.type == tokenize.OP and t.string in KAPAYAN:
            d = max(0, d - 1)
        satir.append(t)
        derin.append(d)
        if t.type == tokenize.OP and t.string in ACAN:
            d += 1
    if satir:
        yield satir, derin


def token_metrikleri(kod, uzunluk_metni):
    toks = list(tokenize.generate_tokens(io.StringIO(kod).readline))

    # --- SLOC ve yorum orani ---
    yorumlar = {}
    for t in toks:
        if t.type == tokenize.COMMENT:
            yorumlar.setdefault(t.start[0], t.string.rstrip())
    sloc = dolu = 0
    for no, s in enumerate(uzunluk_metni.split("\n"), start=1):
        s = s.rstrip()
        if not s.strip():
            continue
        dolu += 1
        yorum = yorumlar.get(no)
        if yorum and s.endswith(yorum):
            s = s[:len(s) - len(yorum)]
        sloc += bool(s.strip())
    if sloc == 0:
        return None

    # --- kontrol akisi ic iceligi (INDENT/DEDENT ile; yalniz if/for/while/try/with bloklari sayilir) ---
    yigin, en_derin, bekleyen = [], 0, None
    ilk, son_anlamli = None, None
    for t in toks:
        if t.type == tokenize.INDENT:
            yigin.append(bekleyen in KONTROL)
            en_derin = max(en_derin, sum(yigin))
            bekleyen = None
        elif t.type == tokenize.DEDENT:
            if yigin:
                yigin.pop()
        elif t.type == tokenize.NEWLINE:
            bekleyen = ilk if (son_anlamli is not None and son_anlamli.string == ":") else None
            ilk, son_anlamli = None, None
        elif t.type not in ANLAMSIZ:
            if ilk is None:
                ilk = t.string
            son_anlamli = t

    # --- tanimlanan adlar ve docstring ---
    fonks, siniflar, degiskenler, parametreler = set(), set(), set(), set()
    n_def = n_class = n_doclu = 0
    doc_bekle = False
    for L, D in mantiksal_satirlar(toks):
        bas = L[0].string
        if doc_bekle:
            n_doclu += int(L[0].type == tokenize.STRING)
            doc_bekle = False
        j = 1 if (bas == "async" and len(L) > 1) else 0
        if L[j].string in ("def", "class") and len(L) > j + 1 and L[j + 1].type == tokenize.NAME:
            ad = L[j + 1].string
            if L[j].string == "class":
                n_class += 1
                siniflar.add(ad)
            else:
                n_def += 1
                fonks.add(ad)
                for k in range(j + 2, len(L)):
                    t, d = L[k], D[k]
                    if d == 1 and t.type == tokenize.NAME and t.string not in KW and \
                            L[k - 1].string in ("(", ",", "*", "**") and t.string not in ("self", "cls"):
                        parametreler.add(t.string)
            doc_bekle = L[-1].string == ":"
            continue
        if bas in ("import", "from", "global", "nonlocal"):
            continue
        # atama hedefleri (derinlik 0'daki ilk atama operatorunden onceki adlar; self.x gibi nitelikler haric)
        esit = next((k for k, (t, d) in enumerate(zip(L, D)) if t.type == tokenize.OP and t.string in ATAMA and d == 0), None)
        if esit is not None and bas not in KW:
            for k in range(esit):
                t = L[k]
                if t.type == tokenize.NAME and t.string not in KW and D[k] == 0 and \
                        (k == 0 or L[k - 1].string != ".") and L[k + 1].string not in ("(", "[", "."):
                    degiskenler.add(t.string)
        if bas == "for":
            for k in range(1, len(L)):
                if L[k].string == "in" and D[k] == 0:
                    break
                if L[k].type == tokenize.NAME and L[k].string not in KW:
                    degiskenler.add(L[k].string)
        for k in range(1, len(L) - 1):                       # with ... as x / except E as x
            if L[k].string == "as" and L[k + 1].type == tokenize.NAME:
                degiskenler.add(L[k + 1].string)

    hepsi = fonks | siniflar | degiskenler | parametreler
    snake_kume = fonks | degiskenler | parametreler          # PEP 8'e gore snake_case olmasi beklenen adlar
    m = {"sloc": sloc, "comment_ratio": len(yorumlar) / dolu, "max_nesting": en_derin, "n_functions": n_def}
    if hepsi:
        m["avg_id_len"] = float(np.mean([len(x) for x in hepsi]))
        m["single_letter_ratio"] = sum(1 for x in hepsi if len(x.strip("_")) == 1) / len(hepsi)
    if snake_kume:
        m["snake_ratio"] = sum(1 for x in snake_kume if SNAKE.match(x)) / len(snake_kume)
    if n_def + n_class:
        m["docstring_coverage"] = n_doclu / (n_def + n_class)
    return m


def dosya_analizi(yol):
    kod = Path(yol).read_bytes().decode("utf-8-sig", errors="ignore").replace("\r\n", "\n").replace("\r", "\n")
    i = kod.find("README Content:")                          # toplama sirasinda eklenmis README metni
    if i >= 0:
        kod = kod[:kod.rfind("\n", 0, i) + 1]
    uzunluk_metni = kod
    kod = "\n".join(s.expandtabs(8) for s in kod.split("\n"))   # Python 2 sekme kurali
    sonuc = {"parsed": False}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            tm = token_metrikleri(kod, uzunluk_metni)
        except (tokenize.TokenError, SyntaxError, IndentationError):
            tm = None
    if tm:
        sonuc["parsed"] = True
        sonuc.update(tm)
        fl = lizard.analyze_file.analyze_source_code("dosya.py", kod).function_list
        if fl:
            sonuc["avg_ccn"] = float(np.mean([f.cyclomatic_complexity for f in fl]))
    return sonuc


def temizlik_kaniti(yol):
    """Ham metinde (hicbir duzeltme yok) bos satir ve yorum var mi -- insan kodlarinin farkli temizlendiginin kaniti."""
    kod = Path(yol).read_bytes().decode("utf-8-sig", errors="ignore").replace("\r\n", "\n").replace("\r", "\n")
    satirlar = kod.split("\n")
    return {"has_blank_line": any(not s.strip() for s in satirlar[:-1]),
            "has_comment": any(s.lstrip().startswith("#") for s in satirlar) or bool(re.search(r"\S\s+#\s", kod))}


# --------------------------------------------------------------------------------------------------------------
# Istatistik
# --------------------------------------------------------------------------------------------------------------
def rank_biserial(fark):
    f = fark[fark != 0]
    r = rankdata(np.abs(f))
    tp, tm = r[f > 0].sum(), r[f < 0].sum()
    return float((tp - tm) / (tp + tm))


def wilcoxon_test(x, y):
    """x = insan, y = LLM; fark = y - x."""
    fark = y - x
    n0 = int((fark != 0).sum())
    sonuc = {"n_pairs": len(fark), "median_human": float(np.median(x)), "median_llm": float(np.median(y))}
    if n0 < 10:
        return {**sonuc, "r": np.nan, "p": np.nan, "status": "not tested (< 10 non-zero pairs)"}
    p = float(wilcoxon(fark, zero_method="wilcox", alternative="two-sided").pvalue)
    return {**sonuc, "r": rank_biserial(fark), "p": p, "status": "tested"}


def holm(p):
    p = np.asarray(p, dtype=float)
    sonuc = np.full(len(p), np.nan)
    gecerli = np.where(~np.isnan(p))[0]
    sira = gecerli[np.argsort(p[gecerli])]
    m, onceki = len(sira), 0.0
    for i, idx in enumerate(sira):
        onceki = max(onceki, min(1.0, (m - i) * p[idx]))
        sonuc[idx] = onceki
    return sonuc


def etki_etiketi(r):
    if np.isnan(r):
        return ""
    a = abs(r)
    return "negligible" if a < 0.1 else "small" if a < 0.3 else "medium" if a < 0.5 else "large"


def medyan_iqr(s):
    s = s.dropna()
    if s.empty:
        return "–"
    q1, q2, q3 = np.percentile(s, [25, 50, 75])
    return f"{q2:.3g} [{q1:.3g}–{q3:.3g}]"


# --------------------------------------------------------------------------------------------------------------
# Sekil
# --------------------------------------------------------------------------------------------------------------
def isi_haritasi(testler):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap

    plt.rcParams.update({"font.size": 8, "axes.edgecolor": "#52514e", "axes.labelcolor": "#0b0b0b",
                         "xtick.color": "#52514e", "ytick.color": "#52514e", "figure.facecolor": "#ffffff"})
    cmap = LinearSegmentedColormap.from_list("ayrisan", ["#184f95", "#6da7ec", "#f0efec", "#ec8a89", "#b3302f"])
    metrikler = [m for m in ANAHTAR if TEST[m]]
    fig, eksenler = plt.subplots(1, 2, figsize=(7.2, 3.6), sharey=True)
    for ax, llm in zip(eksenler, LLMLER):
        alt = testler[testler["llm"] == llm]
        M = np.full((len(metrikler), 5), np.nan)
        P = np.full((len(metrikler), 5), np.nan)
        for i, mt in enumerate(metrikler):
            for j, g in enumerate(GRUPLAR[1:]):
                s = alt[(alt["metric_key"] == mt) & (alt["version"] == grup_adi(g))]
                if len(s):
                    M[i, j], P[i, j] = s["r"].iloc[0], s["p_holm"].iloc[0]
        im = ax.imshow(M, cmap=cmap, vmin=-1, vmax=1, aspect="auto")
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if np.isnan(M[i, j]):
                    continue
                anlamli = P[i, j] < 0.05
                ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=7,
                        color=("#ffffff" if abs(M[i, j]) > 0.6 else "#0b0b0b") if anlamli else "#8a8985",
                        fontstyle="normal" if anlamli else "italic")
        ax.set_xticks(range(5), ["V1", "V2", "V3", "V4", "V5"])
        ax.set_title(f"Human vs {llm}", fontsize=9)
        ax.set_yticks(range(len(metrikler)), [AD[m] for m in metrikler])
        for s in ax.spines.values():
            s.set_visible(False)
    cb = fig.colorbar(im, ax=eksenler, shrink=0.8, pad=0.02)
    cb.set_label("Effect size r  (+ : higher in LLM code)")
    fig.text(0.01, -0.02, "Grey italic: not significant after Holm correction (p ≥ 0.05).", fontsize=7, color="#52514e")
    for uz in ("png", "pdf"):
        fig.savefig(CIKTI / f"Figure_style_effect_sizes.{uz}", dpi=300, bbox_inches="tight")
    plt.close(fig)


# --------------------------------------------------------------------------------------------------------------
def main():
    t0 = time.time()
    CIKTI.mkdir(exist_ok=True)
    liste = dosyalari_listele()
    liste = liste[~liste["haric"]].reset_index(drop=True)
    print(f"Dosya: {len(liste)}", flush=True)
    kayitlar = []
    for i, satir in enumerate(liste.itertuples(index=False), start=1):
        kayitlar.append({**satir._asdict(), **temizlik_kaniti(satir.yol), **dosya_analizi(satir.yol)})
        if i % 5000 == 0:
            print(f"  {i}/{len(liste)}  ({time.time() - t0:.0f} sn)", flush=True)
    df = pd.DataFrame(kayitlar).drop(columns=["yol", "haric"])
    df["group"] = df["grup"].map(grup_adi)

    # ---------- Ek: kapsam ve temizlik kaniti ----------
    kapsam = df.groupby(["llm", "group"], sort=False).agg(
        files=("dosya", "size"), parsed=("parsed", "sum"),
        files_with_functions=("avg_ccn", lambda s: int(s.notna().sum())),
        pct_files_with_blank_lines=("has_blank_line", lambda s: round(100 * s.mean(), 1)),
        pct_files_with_comments=("has_comment", lambda s: round(100 * s.mean(), 1))).reset_index()
    kapsam.insert(4, "parsed_pct", (100 * kapsam["parsed"] / kapsam["files"]).round(1))

    # ---------- Tablo A: betimsel (islenebilen tum dosyalar) ----------
    tablo_a = []
    for mt in ANAHTAR:
        satir = {"Metric": AD[mt]}
        for llm in LLMLER:
            for g in GRUPLAR:
                satir[f"{llm} {grup_adi(g)}"] = medyan_iqr(df[(df.llm == llm) & (df.grup == g)][mt])
        tablo_a.append(satir)
    satir = {"Metric": "Files analysed (n)"}
    for llm in LLMLER:
        for g in GRUPLAR:
            satir[f"{llm} {grup_adi(g)}"] = str(int(df[(df.llm == llm) & (df.grup == g)]["parsed"].sum()))
    tablo_a.append(satir)
    tablo_a = pd.DataFrame(tablo_a)

    # ---------- Testler: insan - Vk, eslesmis ciftler ----------
    tekil, tekil_rapor = eslestirme_icin_tekille(df)
    sonuclar = []
    for llm in LLMLER:
        ham = tekil[(tekil.llm == llm) & (tekil.grup == "ham")].set_index(["konu", "anahtar"])
        for g in GRUPLAR[1:]:
            v = tekil[(tekil.llm == llm) & (tekil.grup == g)].set_index(["konu", "anahtar"])
            ortak = ham.index.intersection(v.index)
            for mt in ANAHTAR:
                if not TEST[mt]:
                    continue
                x, y = ham.loc[ortak, mt].astype(float), v.loc[ortak, mt].astype(float)
                ok = x.notna() & y.notna()
                sonuclar.append({"llm": llm, "version": grup_adi(g), "metric_key": mt, "metric": AD[mt],
                                 **wilcoxon_test(x[ok].values, y[ok].values)})
    testler = pd.DataFrame(sonuclar)
    testler["p_holm"] = holm(testler["p"].values)
    testler["significant"] = testler["p_holm"] < 0.05
    testler["effect_size"] = testler["r"].apply(etki_etiketi)

    # ---------- Tablo B: etki buyuklugu r + yildiz ----------
    def hucre(s):
        if s.empty:
            return "n/a†"
        r, p = s["r"].iloc[0], s["p_holm"].iloc[0]
        if np.isnan(r):
            return "–"
        return f"{r:+.2f}" + ("***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "")
    tablo_b = []
    for mt in ANAHTAR:
        satir = {"Metric": AD[mt]}
        for llm in LLMLER:
            for g in GRUPLAR[1:]:
                satir[f"Human vs {llm} {grup_adi(g)}"] = hucre(
                    testler[(testler.llm == llm) & (testler.version == grup_adi(g)) & (testler.metric_key == mt)])
        tablo_b.append(satir)
    tablo_b = pd.DataFrame(tablo_b)
    notlar = pd.DataFrame({"Note": [
        "Table A: median [interquartile range] over all parsed files.",
        "Table B: matched-pairs rank-biserial r from Wilcoxon signed-rank tests on human/LLM pairs of the same "
        "source program; + = higher in LLM code. Holm-corrected: * p<0.05, ** p<0.01, *** p<0.001.",
        "|r| < 0.1 negligible, 0.1-0.3 small, 0.3-0.5 medium, >= 0.5 large.",
        "† Comment ratio is reported descriptively only: comments (and blank lines) were removed from the "
        "human-written files during dataset preparation, so a human-vs-LLM test would measure preprocessing, "
        "not style (see S1_coverage, pct_files_with_comments).",
        "– : not tested (fewer than 10 non-zero pairs).",
        "Cyclomatic complexity is averaged over functions (module-level code is not counted)."]})

    # ---------- Kaydet ----------
    tablo_a.to_csv(CIKTI / "Table_A_style_metrics.csv", index=False, encoding="utf-8-sig")
    tablo_b.to_csv(CIKTI / "Table_B_significance_tests.csv", index=False, encoding="utf-8-sig")
    testler.to_csv(CIKTI / "all_tests.csv", index=False, encoding="utf-8-sig")
    df.drop(columns=["grup"]).to_csv(CIKTI / "file_metrics.csv", index=False, encoding="utf-8-sig")
    with pd.ExcelWriter(CIKTI / "R4_C1_style_metrics_v3.xlsx", engine="openpyxl") as w:
        tablo_a.to_excel(w, sheet_name="Table_A_style_metrics", index=False)
        tablo_b.to_excel(w, sheet_name="Table_B_significance", index=False)
        notlar.to_excel(w, sheet_name="Notes", index=False)
        testler.to_excel(w, sheet_name="All_tests", index=False)
        kapsam.to_excel(w, sheet_name="S1_coverage", index=False)
        tekil_rapor.to_excel(w, sheet_name="S2_matching", index=False)
    isi_haritasi(testler)

    print(f"\nTest: {len(testler)}, yapilamayan: {int(testler['r'].isna().sum())}, "
          f"Holm sonrasi anlamli: {int(testler['significant'].sum())}")
    print(f"Bitti: {time.time() - t0:.0f} sn. Ciktilar: {CIKTI}")


if __name__ == "__main__":
    main()
