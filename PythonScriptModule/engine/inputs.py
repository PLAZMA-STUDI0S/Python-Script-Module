class InputHandler:
    def __init__(self, project_name):
        self.project_name = project_name

    def process_inputs(self):
        print(f"📝 {self.project_name} için giriş verileri işleniyor...")
        # Giriş verilerini burada işleyebilirsiniz.
        # Örnek olarak, bazı parametreler alabilirsiniz:
        user_input = input("Lütfen bir sayı girin: ")
        print(f"Alınan giriş: {user_input}")
