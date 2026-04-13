import pandas as pd
import matplotlib.pyplot as plt
import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

# --- ADIM 1: CSV DOSYASINI SEÇ (Video seçmeye gerek yok) ---
def get_csv_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    csv_file = filedialog.askopenfilename(title="CSV Veri Dosyasını Seç", filetypes=[("CSV Files", "*.csv")])
    return csv_file

csv_path = get_csv_file()

if not csv_path:
    print("Dosya seçilmedi, program kapatılıyor.")
    exit()

# --- ADIM 2: VERİYİ VE ÇÖZÜNÜRLÜĞÜ HAZIRLA ---
df = pd.read_csv(csv_path)

# Not: Beyaz tuval için videonun çözünürlüğünü bilmemiz lazım.
# Eğer bilmiyorsak, CSV'deki maksimum X ve Y değerlerini baz alabiliriz.
max_x = int(df['X'].max()) + 50 # Biraz marj ekleyelim
max_y = int(df['Y'].max()) + 50

# --- ADIM 3: BEYAZ KANVAS ÜZERİNDE GÖRSELLEŞTİRME ---
plt.figure(figsize=(12, 10))

# Arka planı tamamen beyaz bir resim (tuval) ile doldur
white_canvas = np.ones((max_y, max_x, 3), dtype=np.uint8) * 255
# exten=[sol, sağ, alt, üst] koordinatları tuvale oturt
plt.imshow(white_canvas, extent=[0, max_x, max_y, 0]) 

# Isı Haritası (KDE Plot) - Beyaz zeminde en iyi sonucu bu verir
import seaborn as sns
sns.kdeplot(
    data=df, x='X', y='Y', 
    fill=True, 
    thresh=0.05,       # Düşük yoğunluklu gürültüyü temizler
    levels=100, 
    cmap="YlOrRd",    # Sarıdan kırmızıya (sıcaklık haritası)
    alpha=0.8,
    bw_adjust=0.5     # Haritanın odaklılığını ayarlar
)

# Nokta Analizi de ekleyelim (Opsiyonel, veri yoğunsa kapatabilirsin)
# plt.scatter(df['X'], df['Y'], c='black', s=1, alpha=0.1)

# Grafik Ayarları
plt.title(f"Yoğunluk Analizi Sonucu: {len(df)}", fontsize=15)
plt.xlim(0, max_x)
plt.ylim(max_y, 0) # Y eksenini OpenCV uyumu için ters çevir
plt.axis('on') # Eksenleri açalım ki koordinatları görebilelim
plt.grid(True, linestyle='--', alpha=0.5) # Koordinat çizgileri ekle
plt.xlabel("X Koordinatı (Piksel)")
plt.ylabel("Y Koordinatı (Piksel)")

plt.show()