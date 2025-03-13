import sys
import os
from engine.inputs import InputHandler
from engine.output import OutputHandler
from engine.data import DataProcessor
from engine.localserver import LocalServer
from engine.errorfinder import ErrorFinder

class MainEngine:
    def __init__(self, project_name):
        self.project_name = project_name
        self.input_handler = InputHandler(self.project_name)
        self.output_handler = OutputHandler(self.project_name)
        self.data_processor = DataProcessor(self.project_name)
        self.local_server = LocalServer(self.project_name)
        self.error_finder = ErrorFinder()

    def run(self):
        print("🔧 Proje başlatılıyor...")

        try:
            # Giriş işlemleri
            self.input_handler.process_inputs()

            # Veri işleme
            self.data_processor.process_data()

            # Lokal sunucu başlatma
            self.local_server.start_server()

            # Çıktı yönetimi
            self.output_handler.handle_output()

        except Exception as e:
            # Hataları raporlama
            self.error_finder.report_error(e)

if __name__ == "__main__":
    project_name = "my_project"
    engine = MainEngine(project_name)
    engine.run()
