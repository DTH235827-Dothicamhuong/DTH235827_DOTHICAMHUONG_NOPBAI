
s = input("Nhập chuỗi: ")

so_in_hoa = 0
so_in_thuong = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
so_khoang_trang = 0
so_nguyen_am = 0
so_phu_am = 0

nguyen_am = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        so_in_hoa += 1
    elif ch.islower():
        so_in_thuong += 1

    if ch.isdigit():
        so_chu_so += 1
    elif not ch.isalnum() and not ch.isspace():  
        so_ky_tu_dac_biet += 1

    if ch.isspace():
        so_khoang_trang += 1
    
    if ch.isalpha(): 
        if ch in nguyen_am:
            so_nguyen_am += 1
        else:
            so_phu_am += 1

print("Số chữ IN HOA:", so_in_hoa)
print("Số chữ in thường:", so_in_thuong)
print("Số chữ là chữ số:", so_chu_so)
print("Số ký tự đặc biệt:", so_ky_tu_dac_biet)
print("Số khoảng trắng:", so_khoang_trang)
print("Số chữ là Nguyên Âm:", so_nguyen_am)
print("Số chữ là Phụ Âm:", so_phu_am)
