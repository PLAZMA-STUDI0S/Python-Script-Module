import os
import subprocess

def run_script(script_name):
    file_path = os.path.join("saved_scripts", f"{script_name}.py")
    
    if os.path.exists(file_path):
        print(f"Çalıştırılıyor: {file_path}")
        subprocess.run(["python", file_path])
    else:
        print("Hata: Belirtilen script bulunamadı!")

if __name__ == "__main__":
    # Örnek kullanım:
    run_script("test_script")
