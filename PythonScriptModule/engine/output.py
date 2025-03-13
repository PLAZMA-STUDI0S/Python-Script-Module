class OutputHandler:
    def __init__(self, project_name):
        self.project_name = project_name

    def handle_output(self):
        print(f"📊 {self.project_name} için çıktı işleniyor...")
        # Çıktıyı burada işleyebilir ve görüntüleyebilirsiniz.
        print(f"Çıktı: {self.project_name} başarıyla işlendi!")
