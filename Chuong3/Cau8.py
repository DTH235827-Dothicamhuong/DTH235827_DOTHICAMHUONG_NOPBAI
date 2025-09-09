def may_tinh(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Lỗi: chia cho 0!"
    else:
        return "Phép toán không hợp lệ!"

# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")

# Xuất kết quả
print("Kết quả:", may_tinh(a, b, op))
