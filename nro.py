import os
import zipfile
import requests
from tqdm import tqdm
import subprocess

# Link tải trực tiếp
ZIP_FILE_URL = "https://github.com/NGUYENTRIEUPHUC/nro-offline/releases/download/SOURCE/NRO.OFFLINE.zip"  # Link tải file ZIP trực tiếp
SQL_FILE_URL = "https://github.com/NGUYENTRIEUPHUC/nro-offline/releases/download/SOURCE/solomon.1.sql"  # Link tải file SQL trực tiếp

def download_file(url, destination):
    """
    Tải file từ URL bất kỳ.
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Kiểm tra lỗi HTTP
    with open(destination, "wb") as f:
        for chunk in tqdm(response.iter_content(1024), desc="Downloads", unit="KB"):
            f.write(chunk)

def extract_zip(zip_path, extract_to):
    """
    Giải nén file ZIP.
    """
    print("Extracting zip file...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Extraction complete!")

def run_server():
    """
    Chạy lệnh khởi động server.
    """
    jar_path = "dist/Arriety.jar"
    if os.path.exists(jar_path):
        print("Starting server...")
        subprocess.run(["java", "-jar", jar_path])
    else:
        print(f"Error: {jar_path} not found!")

def show_menu():
    """
    Hiển thị menu để người dùng chọn.
    """
    while True:
        print("\n=== Menu ===")
        print("1. Tải xuống và giải nén file ZIP")
        print("2. Tải file SQL")
        print("3. Chạy server")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == "1":
            print("Đang tải file ZIP...")
            destination = "nro.zip"
            download_file(ZIP_FILE_URL, destination)
            if os.path.exists(destination):
                extract_zip(destination, ".")
        elif choice == "2":
            print("Đang tải file SQL...")
            destination = "NROBABY.sql"
            download_file(SQL_FILE_URL, destination)
            print(f"File SQL đã được tải về: {destination}")
        elif choice == "3":
            run_server()
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    show_menu()