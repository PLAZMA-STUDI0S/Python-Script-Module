import socket

class LocalServer:
    def __init__(self, project_name):
        self.project_name = project_name
        self.host = 'localhost'
        self.port = 8080

    def start_server(self):
        print(f"🚀 {self.project_name} için yerel sunucu başlatılıyor...")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Sunucu {self.host}:{self.port} adresinde dinleniyor...")

        client_socket, client_address = server_socket.accept()
        print(f"Bağlantı kabul edildi: {client_address}")
        client_socket.send(b"Sunucuya bağlandınız!")
        client_socket.close()
