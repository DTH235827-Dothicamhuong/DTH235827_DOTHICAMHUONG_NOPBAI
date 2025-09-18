import random


print("Các giá trị ngẫu nhiên từ randrange(0, 100):")
for _ in range(10):
    print(random.randrange(0, 100), end=" ")
print("\n")
test_values = [4.5, 34, -1, 100, 0, 99]
print("Kiểm tra các giá trị trong đề:")
for v in test_values:
    if isinstance(v, int) and 0 <= v < 100:
        print(f"{v} ✅ Có thể xuất hiện")
    else:
        print(f"{v} ❌ Không thể xuất hiện")
