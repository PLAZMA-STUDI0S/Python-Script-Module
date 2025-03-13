import subprocess
import sys

# Gerekli modüller listesi
modules = ["flask", "requests", "tkinter"]  # Gerekirse ekleme yapılabilir

def install_modules():
    for module in modules:
        try:
            __import__(module)
            print(f"{module} zaten yüklü.")
        except ImportError:
            print(f"{module} bulunamadı, yükleniyor...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

if __name__ == "__main__":
    install_modules()
