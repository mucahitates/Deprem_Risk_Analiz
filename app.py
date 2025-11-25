import streamlit as st
import pandas as pd
st.set_page_config(page_title="Deprem Risk Analizi", layout="wide")

#st.title("Deprem Risk Analizi Paneli")
#st.write("Uygulama başarıyla çalışıyor ")

st.title("Deprem Risk Analizi Paneli")

# ======================
# VERİYİ OKU
# ======================
df = pd.read_excel("data/raw/raw_deprem.xlsx")

# İl çıkarma fonksiyonu
def il_cek(location):
    if "(" in str(location) and ")" in str(location):
        return location.split("(")[-1].replace(")", "").strip()
    return "-"

df["Il"] = df["Location"].apply(il_cek)

# Temizleme
df = df[
    (df["Il"] != "-") &
    (~df["Il"].str.contains("Denizi", na=False))
]

# Sadece gerekli kolonlar
df["Magnitude"] = pd.to_numeric(df["Magnitude"], errors="coerce")
df["Depth"] = pd.to_numeric(df["Depth"], errors="coerce")
df = df.dropna(subset=["Magnitude", "Depth"])

analiz_df = df[["Il", "Magnitude", "Depth"]]

# ======================
# İL BAZLI İSTATİSTİK
# ======================
il_istatistik = analiz_df.groupby("Il").agg(
    deprem_sayisi=("Magnitude", "count"),
    ortalama_buyukluk=("Magnitude", "mean"),
    max_buyukluk=("Magnitude", "max")
).reset_index()

# ======================
# RİSK SKORU
# ======================
max_deprem = il_istatistik["deprem_sayisi"].max()
max_ortalama = il_istatistik["ortalama_buyukluk"].max()
max_buyukluk = il_istatistik["max_buyukluk"].max()

il_istatistik["risk_skoru"] = (
    (il_istatistik["deprem_sayisi"] / max_deprem) * 4 +
    (il_istatistik["ortalama_buyukluk"] / max_ortalama) * 3 +
    (il_istatistik["max_buyukluk"] / max_buyukluk) * 3
)

def risk_seviyesi(skor):
    if skor < 3:
        return "Düşük"
    elif skor < 6:
        return "Orta"
    else:
        return "Yüksek"

il_istatistik["risk_seviyesi"] = il_istatistik["risk_skoru"].apply(risk_seviyesi)

# ======================
# PANELDE GÖSTER
# ======================

st.subheader("Deprem Verisi - İlk 10 Kayıt")
st.dataframe(df.head(10))

st.subheader("İl Bazlı Deprem Risk Analizi")
st.dataframe(il_istatistik.sort_values(by="risk_skoru", ascending=False))

st.subheader("En Riskli 10 İl")
en_riskli_10 = il_istatistik.sort_values(by="risk_skoru", ascending=False).head(10)
st.dataframe(en_riskli_10)


st.subheader("En Riskli 10 İl - Grafik Gösterim")

grafik_df = en_riskli_10.set_index("Il")

st.bar_chart(grafik_df["risk_skoru"])



st.subheader("İl Bazlı Detaylı Analiz")

secili_il = st.selectbox("Analiz etmek istediğiniz ili seçin:", il_istatistik["Il"])

il_verisi = il_istatistik[il_istatistik["Il"] == secili_il].iloc[0]

st.markdown(f"""
### 📍 {secili_il} için Deprem Analizi

- 🧮 Deprem Sayısı: **{il_verisi['deprem_sayisi']}**
- 📊 Ortalama Büyüklük: **{il_verisi['ortalama_buyukluk']:.2f}**
- ⚡ Maksimum Büyüklük: **{il_verisi['max_buyukluk']:.2f}**
- 🚨 Risk Skoru: **{il_verisi['risk_skoru']:.2f}**
- 🔥 Risk Seviyesi: **{il_verisi['risk_seviyesi']}**
""")
