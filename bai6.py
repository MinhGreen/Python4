print("Đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.")
def hoathuong(line):
    x = ""
    for i in line:
        if i.islower():
            x+=i.upper()
        else:
            x+=i.lower()
    print(x)
line=input("Nhập chuỗi: ")
hoathuong(line)