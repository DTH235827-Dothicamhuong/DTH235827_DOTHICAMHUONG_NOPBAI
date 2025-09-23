import re

def NegativeNumberInStrings(s):
    
    ket_qua = re.findall(r'-\d+', s)
    return [int(x) for x in ket_qua]  
chuoi = "abc-5xyz-12k9l--p"
print("Chuỗi:", chuoi)
print("Các số nguyên âm trong chuỗi:", NegativeNumberInStrings(chuoi))
