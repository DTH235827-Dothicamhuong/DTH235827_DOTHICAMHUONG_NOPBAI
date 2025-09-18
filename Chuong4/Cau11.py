
def sum1(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s


def sum2():
    global val
    s = 0
    while val > 0:
        s = s + val
        val = val - 1
    return s


def sum3():
    s = 0
    for i in range(val, 0, -1):
        s = s + i
    return s

def main1():
    global val
    val = 5
    print(sum1(5))  


def main2():
    global val
    val = 5
    print(sum1(val))
    print(sum2())
    print(sum3())


def main3():
    global val
    val = 5
    print(sum2())
    print(sum3())
    print(sum1(val))

print("Kết quả Trường hợp 1:")
main1()
print("\nKết quả Trường hợp 2:")
main2()
print("\nKết quả Trường hợp 3:")
main3()
