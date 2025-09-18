import math

xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))
xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))
dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print(f"Độ dài đoạn thẳng AB là: {dAB:.2f}")
