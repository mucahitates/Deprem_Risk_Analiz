#  Deprem Risk Analizi ve Bölgesel Güvenlik Skoru Sistemi

Bu proje, Türkiye genelindeki deprem verilerini analiz ederek il bazlı risk skorları oluşturan ve kullanıcıya etkileşimli bir web paneli sunan veri odaklı bir karar destek sistemidir.

Amaç; bireylerin, şehir planlamacılarının ve yerel yönetimlerin daha bilinçli risk değerlendirmesi yapabilmesine katkı sağlamaktır.

---

##  Proje Özellikleri

*  Ham deprem verisinin temizlenmesi ve işlenmesi
*  İl bazlı deprem istatistikleri
*  Özel risk skoru hesaplama algoritması
*  En riskli 10 ilin görselleştirilmesi
*  Etkileşimli Streamlit web paneli
*  İl seçimi ve detaylı analiz ekranı
*  Grafiksel risk görselleştirmesi
*  Harita tabanlı risk gösterimi (HTML)

---

##  Kullanılan Teknolojiler

* Python 3.11
* Pandas
* NumPy
* Matplotlib
* Folium
* Streamlit
* VS Code

---

## Risk Skoru Hesaplama Formülü

Her il için risk skoru aşağıdaki formüle göre hesaplanır:

```
Risk Skoru =
(Deprem Sayısı / Maksimum Deprem Sayısı) * 4
+ (Ortalama Büyüklük / Maksimum Ortalama Büyüklük) * 3
+ (Maksimum Büyüklük / Maksimum Maksimum Büyüklük) * 3
```

Risk Seviyeleri:

* 0 - 3   → Düşük
* 3 - 6   → Orta
* 6+      → Yüksek

---

##  Web Panel Özellikleri

Streamlit ile geliştirilen web paneli aşağıdaki işlevleri içerir:

* 🔹 Deprem verisinin tablo halinde gösterimi
* 🔹 İl bazlı risk skorlarının hesaplanması
* 🔹 En riskli 10 ilin grafik sunumu
* 🔹 Açılır menü ile il seçimi
* 🔹 Seçilen il için detaylı analiz

---

##  Proje Klasör Yapısı

```
DepremRiskAI/
│
├── data/
│   └── raw/
│       └── raw_deprem.xlsx
│
├── app.py
├── deprem_risk_analizi.ipynb
├── turkiye_risk_haritasi.html
├── requirements.txt
└── README.md
```

---

## ▶ Kurulum ve Çalıştırma

### 1. Bağımlılıkları yükle

```bash
pip install -r requirements.txt
```

### 2. Web paneli çalıştır

```bash
streamlit run app.py
```

Tarayıcıda otomatik olarak aşağıdaki adreste açılır:

```
http://localhost:8501
```

---

## Örnek Kullanım Senaryosu

Kullanıcı panel üzerinden "Balıkesir" ilini seçtiğinde:

* Deprem sayısını
* Ortalama büyüklüğü
* Maksimum büyüklüğü
* Risk skorunu
* Risk seviyesini

dinamik olarak görebilir.

---

##  Projenin Katkısı

Bu proje sayesinde:

* Deprem riskleri şeffaf şekilde görünür hale gelir
* Veri temelli karar verme desteklenir
* Şehir güvenliği farkındalığı artırılır

---

---

##  Lisans

Bu proje eğitim ve portföy amaçlı olarak geliştirilmiştir.
