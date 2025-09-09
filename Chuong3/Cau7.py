import datetime

def ngay_ke_tiep(ngay, thang, nam):
    try:
        d = datetime.date(nam, thang, ngay)         
        d_next = d + datetime.timedelta(days=1)     
        return d_next.day, d_next.month, d_next.year
    except ValueError:
        return None

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ket_qua = ngay_ke_tiep(ngay, thang, nam)
if ket_qua:
    print("Ngày kế tiếp là: {}/{}/{}".format(*ket_qua))
else:
    print("Ngày không hợp lệ!")

