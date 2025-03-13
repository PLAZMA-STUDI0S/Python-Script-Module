import json
import os

class JsonCreator:
    def __init__(self, project_name):
        self.json_path = f"engine/json/{project_name}.json"

    def create_json(self, scripts):
        """Kullanıcıların girdiği Python kodlarını JSON formatında kaydet."""
        if os.path.exists(self.json_path):
            print(f"❌ {self.json_path} zaten mevcut!")
            return

        try:
            with open(self.json_path, "w", encoding="utf-8") as f:
                json.dump(scripts, f, indent=4)
            print(f"✔️ JSON dosyası başarıyla oluşturuldu: {self.json_path}")

        except Exception as e:
            print(f"❌ JSON dosyası oluşturulamadı: {e}")

# Test
if __name__ == "__main__":
    scripts = {
        "test_script": "print('Merhaba Python!')",
        "second_script": "x = 5; print(x * 2)"
    }
    creator = JsonCreator("my_project")
    creator.create_json(scripts)
