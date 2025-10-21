import zipfile

def nen_file(ten_tin_nguon, ten_file_zip):
    # 'w' để tạo mới, ZIP_DEFLATED là phương pháp nén
    with zipfile.ZipFile(ten_file_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(ten_tin_nguon)
    print(f"✅ Đã nén {ten_tin_nguon} thành {ten_file_zip}")
    

# --- Chạy thử ---
source = input("Nhập đường dẫn tệp cần nén: ")
zipname = input("Nhập tên tệp zip muốn tạo (vd: output.zip): ")
nen_file(source, zipname)
