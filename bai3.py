print("Xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.")
def xoakitule(line):
    return line[::2]
line=input("Nhập chuỗi: ")
print(xoakitule(line)) 