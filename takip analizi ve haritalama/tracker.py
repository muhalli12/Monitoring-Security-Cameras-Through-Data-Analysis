import cv2
from ultralytics import YOLO
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

# --- ADIM 1: DOSYA SEÇME PENCERESİ ---
def select_video_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Pencereyi öne getir
    file_path = filedialog.askopenfilename(
        title="Analiz Edilecek Videoyu Seçiniz",
        filetypes=[("Video Dosyaları", "*.mp4 *.avi *.mov *.mkv")]
    )
    return file_path

video_path = select_video_file()

if not video_path:
    print("Dosya seçilmedi, program kapatılıyor.")
else:
    print(f"Seçilen dosya analize alınıyor: {video_path}")
    
    # Model yükleme (v8, v11 veya v12 kullanabilirsin)
    model = YOLO('yolo11n.pt') # Güncel sürüm
    cap = cv2.VideoCapture(video_path)
    data = []
    
    frame_count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        frame_count += 1
        # HIZLANDIRMA: Her 2 karede bir işlem yap (Opsiyonel: 1 yaparsan her kareyi işler)
        if frame_count % 2 != 0:
            continue

        # Tahmin (Sadece insan sınıfı: class 0)
        results = model(frame, classes=[0], verbose=False)

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy() 
            for box in boxes:
                # KRİTİK GÜNCELLEME: y_center (Merkez Nokta)
                # İnsanların üzerine tam oturması için orta noktayı alıyoruz
                x_center = (box[0] + box[2]) / 2
                y_center = (box[1] + box[3]) / 2 
                
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
                data.append([timestamp, x_center, y_center])

        # İşlemi görsel olarak takip etmek istersen (isteğe bağlı):
        # cv2.imshow("Analiz Yapiliyor...", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

    # --- ADIM 3: VERİYİ SAKLA ---
    df = pd.DataFrame(data, columns=['Time', 'X', 'Y'])
    output_name = "analiz edilen video sonucu.csv"
    df.to_csv(output_name, index=False)
    
    print("-" * 30)
    print(f"İŞLEM BAŞARIYLA TAMAMLANDI!")
    print(f"Toplam {len(df)} adet veri noktası toplandı.")
    print(f"Yeni dosya: '{output_name}'")
    print("-" * 30)