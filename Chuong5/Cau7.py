def ToiUuChuoiDanhTu(s):
    words = s.strip().split()
    words = [word.capitalize() for word in words]
    return " ".join(words)

chuoi = "  TRần    duY   thAnH   "
print("Chuỗi gốc:", repr(chuoi))
print("Chuỗi tối ưu:", ToiUuChuoiDanhTu(chuoi))
