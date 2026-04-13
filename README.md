Bu proje, video akışlarından nesne tespiti yaparak müşteri hareket modellerini analiz eden ve bu verileri soyutlanmış ısı haritalarına dönüştüren uçtan uca bir veri analitiği çözümüdür.

🚀 Proje Özeti
Proje, ham video verisini yapılandırılmış koordinat verisine dönüştürür ve ardından bu veriyi kullanarak işletmelerin fiziksel alan verimliliğini ölçmesine olanak tanır. YOLO (You Only Look Once) mimarisi kullanılarak yüksek doğrulukla kişi tespiti gerçekleştirilmektedir.

🛠️ Teknik Yetkinlikler
Computer Vision: YOLOv11/v12, OpenCV

Data Science: Pandas, NumPy

Data Visualization: Seaborn, Matplotlib

Architecture: Modüler Python Scriptleri (Inference & Analytics separation)

📁 Dosya Yapısı
tracker.py: Videoyu işleyerek insan koordinatlarını (x, y) ve zaman damgasını (timestamp) CSV formatında dışa aktarır.

analiz.py: CSV verisini alarak video üzerine veya soyutlanmış beyaz bir tuval üzerine ısı haritası ve nokta analizi (scatter plot) çizer.

💡 Mühendislik Yaklaşımı ve Çözümler
Proje geliştirme sürecinde karşılaşılan zorluklar ve uygulanan çözümler:

Perspektif Düzeltme: Kamera açısı nedeniyle oluşan yığılmaları engellemek için koordinat sistemi y_bottom yerine y_center (merkez nokta) olarak güncellenmiş, böylece noktaların nesne üzerine tam oturması sağlanmıştır.

Veri Soyutlama: Arka plan gürültüsünü temizlemek için video karesinden bağımsız, sadece koordinat düzlemi üzerine inşa edilen "Beyaz Tuval Analizi" geliştirilmiştir.

Performans: Gerçek zamanlı analiz gereksinimleri için her kareden veri toplamak yerine kare atlama (frame skipping) optimizasyonu uygulanmıştır.


# Kütüphaneleri yükleyin
pip install ultralytics opencv-python pandas seaborn matplotlib

# Veri toplama aşamasını başlatın
python tracker.py

# Analiz ve görselleştirme aşamasını başlatın
python analiz.py
