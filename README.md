# DevSecOps-CI-CD-Pipeline 

Bu proje, bir Yazılım Mühendisliği ödevi kapsamında, modern yazılım geliştirme süreçlerinde **CI/CD** (Sürekli Entegrasyon / Sürekli Dağıtım) ve **DevSecOps** pratiklerini somutlaştırmak amacıyla geliştirilmiştir.

## Proje Amacı
Yazılım Yaşam Döngüsü (SDLC) üzerinde otomasyon sağlayarak, kodun her gönderiminde (push) otomatik olarak test edilmesi ve güvenlik taramasından geçirilmesi hedeflenmiştir. Bu süreç, **"Shift Left"** prensibi uyarınca güvenliği geliştirme sürecinin en başına çekmeyi amaçlar.

## Kullanılan Teknolojiler
* **Dil:** Python 3.9+
* **Otomasyon:** GitHub Actions
* **Test:** Pytest (Birim Testleri)
* **Güvenlik (SAST):** Bandit (Statik Uygulama Güvenlik Testi)

## Proje Yapısı
* `app.py`: Şifre gücü kontrolü yapan temel uygulama mantığı.
* `test_app.py`: Uygulamanın doğruluğunu denetleyen otomatik test senaryoları.
* `.github/workflows/devsecops.yml`: Tüm iş hattını (pipeline) yöneten otomasyon dosyası.

## Pipeline Aşamaları
1. **Build & Setup:** Bulut üzerinde sanal bir çalışma ortamı kurulur ve bağımlılıklar yüklenir.
2. **CI (Continuous Integration):** Yazılan birim testleri koşturulur. Hata varsa süreç durdurulur.
3. **DevSecOps (Security Scan):** Bandit aracı ile kodun "röntgeni" çekilir ve olası güvenlik zafiyetleri (sızıntılar, riskli komutlar) taranır.

## Nasıl Çalışır?
Herhangi bir kod değişikliği yapıp depoya `push` yaptığınızda, GitHub üzerindeki **Actions** sekmesinden tüm bu sürecin otomatik olarak başladığını ve "yeşil" yanarak başarıyla tamamlandığını takip edebilirsiniz.

---
*Bu çalışma Sakarya Üniversitesi Yazılım Mühendisliği dersi sunum ödevi için hazırlanmıştır.*
