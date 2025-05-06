import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageDraw, ImageTk
import subprocess
import sys

# Mevcut çalıştırma klasörünü belirle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Varsayılan logo yolu
default_logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
logo_path = default_logo_path  # Başlangıçta varsayılan logoyu kullan

def toggle_default_logo():
    """Checkbox durumuna göre logo seçim butonunu aktif/pasif yap."""
    if use_default_logo.get():
        btn_select_logo.config(state=tk.DISABLED)
        global logo_path
        logo_path = default_logo_path  # Varsayılan logo kullan
    else:
        btn_select_logo.config(state=tk.NORMAL)

def select_logo():
    """Kullanıcının yeni bir logo seçmesini sağlar."""
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if logo_path:
        use_default_logo.set(0)  # Checkbox'ı kaldır
        btn_select_logo.config(state=tk.NORMAL)  # Logo seç butonu aktif kalmalı

def select_folder():
    """İşlem yapılacak klasörü seçer."""
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        btn_apply_watermark.config(state=tk.NORMAL)

def apply_watermark():
    """Filigran işlemini gerçekleştirir."""
    if not logo_path or not folder_path:
        messagebox.showerror("Hata", "Lütfen önce logo ve klasör seçin!")
        return
    
    output_folder = os.path.join(folder_path, "Filigranlı Fotoğraflar")
    os.makedirs(output_folder, exist_ok=True)
    
    logo = Image.open(logo_path).convert("RGBA")
    
    # Logoyu 3x3 cm (354x354 px) olarak yeniden boyutlandır
    target_size = (354, 354)  # 3x3 cm @ 300 DPI
    logo = logo.resize(target_size, Image.Resampling.LANCZOS)  # Pillow 10+ için güncellendi
    
    # Şeffaflığı %35 yaparak tüm renkleri koruyalım
    alpha = logo.getchannel("A")
    alpha = alpha.point(lambda p: int(p * 0.35))  # %35 şeffaflık
    logo.putalpha(alpha)
    
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, file_name)
            image = Image.open(image_path).convert("RGBA")

            # Orijinal dosyanın formatını, renk modunu ve bit derinliğini al
            original_format = image.format  
            original_mode = image.mode  

            # Yeni bir şeffaf katman oluştur
            watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
            
            # Logoyu belirli bir desen halinde tekrar eden şekilde ekle
            logo_width, logo_height = logo.size
            for x in range(0, image.width, logo_width + 75):  # 75px boşluk
                for y in range(0, image.height, logo_height + 75):
                    watermark_layer.paste(logo, (x, y), logo)
            
            # Filigranı fotoğrafa uygula
            watermarked_image = Image.alpha_composite(image, watermark_layer)
            
            # JPEG olarak kaydet ve boyutu birebir koru
            output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".jpg")

            # Eğer orijinal dosya JPEG ise EXIF verilerini de taşı (ama optimize veya progressive kullanma)
            if original_format == "JPEG":
                watermarked_image.convert("RGB").save(output_path, "JPEG", quality=100, subsampling=0, optimize=False, progressive=False)
            else:
                watermarked_image.convert("RGB").save(output_path, "JPEG", quality=100, optimize=False, progressive=False)

    messagebox.showinfo("İşlem Tamamlandı", "Tüm fotoğraflara filigran eklendi!")

    # İşlem klasörünü otomatik aç
    try:
        if sys.platform.startswith('win'):
            os.startfile(output_folder)
        elif sys.platform == 'darwin':
            subprocess.call(['open', output_folder])
        else:
            subprocess.call(['xdg-open', output_folder])
    except Exception as e:
        print(f"Klasör açılırken hata oluştu: {e}")

    root.quit()  # Uygulamayı kapat

# Arayüzü oluştur
root = tk.Tk()
root.title("Filigran Ekle v.1.2.4")
root.geometry("600x300")

# Logo yükle ve göster (varsa)
logo_path = os.path.join(BASE_DIR, "logo.png")
if os.path.exists(logo_path):
    pil_logo = Image.open(logo_path).resize((100, 100), Image.LANCZOS)
    logo_img = ImageTk.PhotoImage(pil_logo)
    logo_label = tk.Label(root, image=logo_img)
    logo_label.image = logo_img
    logo_label.pack(pady=10)
else:
    tk.Label(root, text="Test Deneme", font=("Arial Black", 24)).pack(pady=10)

# Varsayılan logo seçeneği için checkbox
use_default_logo = tk.IntVar(value=1)  # Varsayılan olarak seçili
chk_default_logo = tk.Checkbutton(root, text="Varsayılan Filigran Logosunu Kullan (logo.png)", variable=use_default_logo, command=toggle_default_logo)
chk_default_logo.pack()

btn_select_logo = tk.Button(root, text="Filigran Olarak Eklenecek Logoyu Seç", command=select_logo, state=tk.DISABLED)  # Başlangıçta devre dışı
btn_select_logo.pack(pady=5)

btn_select_folder = tk.Button(root, text="Filigran Eklenecek Klasörü Seç", command=select_folder, state=tk.NORMAL)
btn_select_folder.pack(pady=5)

btn_apply_watermark = tk.Button(root, text="Fotoğraflara Filigran Ekle", command=apply_watermark, state=tk.DISABLED)
btn_apply_watermark.pack(pady=10)

root.mainloop()
