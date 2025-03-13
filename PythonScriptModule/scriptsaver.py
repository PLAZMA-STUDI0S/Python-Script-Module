import os

def save_script(script_name, code):
    directory = "saved_scripts"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, f"{script_name}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    
    print(f"Script kaydedildi: {file_path}")

if __name__ == "__main__":
    # Test etmek için:
    example_code = "print('Merhaba, Python Script Module!')"
    save_script("test_script", example_code)
