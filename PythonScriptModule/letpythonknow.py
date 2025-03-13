import sys

def check_python():
    version = sys.version_info
    if version.major < 3:
        print("Python 3+ gerekiyor! Lütfen güncelleyin.")
        return False
    print(f"Python sürümü uygun: {version.major}.{version.minor}.{version.micro}")
    return True

if __name__ == "__main__":
    check_python()
