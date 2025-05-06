# Fotoğraf Filigran Oluşturucu

**Fotoğraf Filigran Oluşturucu**, seçtiğiniz klasördeki tüm fotoğraflara şeffaf bir logo filigranı uygulayan bir Python/Tkinter uygulamasıdır. İşlemler tamamlandıktan sonra filigranlı fotoğrafları içeren klasörü otomatik olarak açar.

---

## 🚀 Özellikler

- **Varsayılan Logo**  
  - `logo.png` dosyasını kullanarak hızlıca filigran ekleyebilirsiniz.  
  - Checkbox ile varsayılan logoyu aktif/pasif hale getirebilirsiniz.

- **Özel Logo Seçimi**  
  - Kendi logonuzu `.png`, `.jpg`, `.jpeg` uzantılı dosya ile seçebilirsiniz.  
  - Seçilen logo, checkbox otomatik olarak pasif konuma geçer.

- **Klasör Seçimi**  
  - Filigran eklemek istediğiniz fotoğraf klasörünü seçin.

- **Filigran Uygulama**  
  - Logo, 3x3 cm (354×354 px) boyutuna ölçeklenir, %35 opaklık uygulanır.  
  - Fotoğraf üzerine 75px aralıklarla tekrarlanarak filigran eklenir.  
  - Filigranlı tüm fotoğraflar `Filigranlı Fotoğraflar` adlı yeni bir klasöre JPEG olarak kaydedilir.

- **Otomatik Klasör Açma**  
  - İşlem tamamlandıktan sonra, oluşturulan çıktı klasörü otomatik olarak açılır.
  - Windows, macOS ve Linux uyumludur.

---

## 🛠️ Kurulum

1. Python 3.8+ yüklü olduğundan emin olun.
2. Gerekli paketleri yükleyin:
   ```bash
   pip install pillow
   ```
3. Bu dosyaları aynı klasöre yerleştirin:
   - `FiligranOlusturucu.py`
   - `logo.png` (varsayılan logo)

---

## 📦 Kullanım

1. Uygulamayı çalıştırın:
   ```bash
   dist/FiligranOlusturucu.exe
   ```
2. **Varsayılan Logo** checkbox işaretliyse, `logo.png` kullanılır.
3. Checkbox işaretini kaldırıp `Filigran Olarak Eklenecek Logoyu Seç` ile özel logo seçin.
4. `Filigran Eklenecek Klasörü Seç` ile fotoğraflarınızın bulunduğu klasörü seçin.
5. `Fotoğraflara Filigran Ekle` butonuna tıklayın.
6. İşlem tamamlandığında, yeni klasör otomatik olarak açılacaktır.

---

## 📂 Proje Dosya Yapısı

```plaintext
📂 dist/
    ├── FiligranOlusturucu.exe
├── FiligranOlusturucu.py
├── logo.png
├── arka_plan_dikey.png
├── arka_plan_yatay.png
├── dikey_bos.png
├── yatay_bos.png
```

---

## 🤝 **Yazılım Geliştirici**

[Hakan Akınsu - Computer Engineer](https://github.com/hakanakinsu0)

