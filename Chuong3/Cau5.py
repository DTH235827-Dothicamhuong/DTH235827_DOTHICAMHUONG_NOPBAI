# Hàm thực hiện theo thuật toán đề bài
def test_case(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, ", j =", j, ", k =", k)

# Các test case
print("Case (a): i=3, j=5, k=7")
test_case(3, 5, 7)

print("Case (b): i=3, j=7, k=5")
test_case(3, 7, 5)

print("Case (c): i=5, j=3, k=7")
test_case(5, 3, 7)

print("Case (d): i=5, j=7, k=3")
test_case(5, 7, 3)

print("Case (e): i=7, j=3, k=5")
test_case(7, 3, 5)

print("Case (f): i=7, j=5, k=3")
test_case(7, 5, 3)