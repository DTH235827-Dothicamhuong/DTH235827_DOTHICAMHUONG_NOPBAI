import os
def get_filename(path):
    return os.path.basename(path)

def get_filename_without_ext(path):
    return os.path.splitext(os.path.basename(path))[0]

path = r"d:\music\muabui.mp3"

print("Đường dẫn:", path)
print("Tên file (có đuôi):", get_filename(path))
print("Tên file (không đuôi):", get_filename_without_ext(path))
