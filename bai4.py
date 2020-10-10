print("Sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.")
def noichuoidaucuoi(Line):
    if len(Line)<2:
        return ""
    else:
        return Line[0:2]+Line[-2:]
Line= input("Nhập chuỗi:")
print(noichuoidaucuoi(Line))