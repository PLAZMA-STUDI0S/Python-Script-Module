import json
import os

class ScriptOpener:
    def __init__(self, project_name):
        self.json_path = f"engine/json/{project_name}.json"

    def load_and_run(self):
        """JSON içindeki kodları çalıştır."""
        if not os.path.exists(self.json_path):
            print("❌ JSON dosyası bulunamadı!")
            return
        
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                scripts = json.load(f)

            for script_name, code in scripts.items():
                print(f"🚀 Çalıştırılıyor: {script_name}")
                exec(code)  # JSON içindeki kodu çalıştır

        except json.JSONDecodeError:
            print("❌ Hata: JSON dosyası bozuk!")

# Test
if __name__ == "__main__":
    opener = ScriptOpener("my_project")
    opener.load_and_run()
