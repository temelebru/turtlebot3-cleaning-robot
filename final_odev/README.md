# 🤖 TurtleBot3 Otonom Navigasyon ve QR Görev Sistemi

Bu proje, ROS Noetic ve Gazebo simülasyon ortamı kullanılarak geliştirilmiş **otonom bir mobil robot görev sistemidir**. TurtleBot3 robotu, önceden oluşturulmuş bir harita üzerinde lokalizasyon yaparak belirlenen odalara sırayla gitmekte ve her odada QR kod doğrulama görevi yürütmektedir.

---

## 📌 Proje Özeti

Projenin temel amacı;

* TurtleBot3 robotunun bir ev ortamında **otonom olarak gezinmesi**
* Harita tabanlı lokalizasyon (AMCL)
* Belirli hedef odalara gitmesi
* Her odada QR kod okuma ile doğrulama yapması
* Görev sırasını bir `mission.yaml` dosyasından yönetmesidir.

---

## 🛠 Kullanılan Teknolojiler

* **ROS Noetic**
* **Gazebo Simulator**
* **TurtleBot3 (Burger)**
* **SLAM & Map Server**
* **AMCL Localization**
* **move_base (DWA Planner)**
* **Python (ROS Node)**
* **YAML Konfigürasyon Dosyaları**

---

## 🗺 Haritalama (SLAM)

* Robot, Gazebo ortamında manuel olarak gezdirilerek ortamın haritası çıkarılmıştır.
* Oluşturulan harita `map.pgm` ve `map.yaml` dosyaları olarak kaydedilmiştir.

---

## 📍 Navigasyon ve Lokalizasyon

* **AMCL** algoritması kullanılarak robotun harita üzerindeki konumu belirlenmiştir.
* `move_base` düğümü ile global ve local costmap’ler yapılandırılmıştır.
* Robot, belirlenen hedef koordinatlara otonom olarak ulaşabilmektedir.

---

## 🧭 Görev Yönetimi (Mission System)

Görevler `mission.yaml` dosyası üzerinden tanımlanmıştır.

### Görev Akışı:

1. Robot belirlenen odaya gider
2. Odaya ulaştıktan sonra QR kod okuma beklenir
3. QR doğrulama başarılıysa bir sonraki odaya geçilir
4. Tüm odalar tamamlandığında görev sona erer

### Tanımlı Odalar:

* LIVINGROOM
* CORRIDOR
* BEDROOM
* KITCHEN

Her oda için:

* Giriş hedefi (x, y, yaw)
* Beklenen QR içeriği tanımlanmıştır

---

## 🔲 QR Kod Sistemi

* Gazebo ortamına her oda için ayrı QR kod modelleri eklenmiştir.
* QR’lar odaların giriş noktalarına yerleştirilmiştir.
* Robot, odaya ulaştıktan sonra kamera üzerinden QR kod okumayı denemektedir.

⚠️ **Not:** QR okuma modülü ve görev mantığı çalışmaktadır.Ancak Gazebo simülasyonunda kamera–QR fiziksel hizalama ve görüş açısı nedeniyle QR kodlar kararlı şekilde decode edilememiştir. Buna rağmen QR sistemi entegre edilmiş ve görev akışına dahil edilmiştir.

---

## 🧹 Mini Temizlik Görevi

Proje kapsamında her oda için mini temizlik rotası planlanmıştır.


⚠️ **Not:** QR okuma modülü çalışmadığı için temzilik aşaması da çalışmamıştır.


---

## ▶️ Çalıştırma Adımları

```bash
# Gazebo ortamını başlat
roslaunch final_odev gazebo.launch

roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/ebru/catkin_ws/src/final_odev/maps/map.yaml


# Görev yöneticisini çalıştır
rosrun final_odev mission_runner.py _mission_file:=/home/ebru/catkin_ws/src/final_odev/config/mission.yaml



---

## 🎯 Sonuç

Bu proje kapsamında;

* TurtleBot3 ile tam otonom navigasyon
* Harita tabanlı lokalizasyon
* Görev sıralı oda gezme

başarıyla gerçekleştirilmiştir.

QR okuma kısmı simülasyon kısıtları nedeniyle kararsız çalışsa da sistem mimarisi, görev yönetimi ve navigasyon modülleri eksiksiz şekilde çalışmaktadır.


---

## 👩‍💻 Geliştiren

**Ebru Temel**
ROS & Robotik Sistemler Dersi – Final Ödevi

