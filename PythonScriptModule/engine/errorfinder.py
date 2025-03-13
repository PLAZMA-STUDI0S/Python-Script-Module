class ErrorFinder:
    def __init__(self):
        pass

    def report_error(self, error):
        print(f"❌ Hata oluştu: {str(error)}")
        # Hataları kaydedip ayrıntılı rapor alabilirsiniz.
        # Örneğin:
        with open("error_log.txt", "a") as f:
            f.write(f"Hata: {str(error)}\n")
