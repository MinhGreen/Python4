print("Xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.")
x=0
def xoataivitri(line):
    n=line[:x]+line[x+1:]
    print(n)
line =input("Nhập chuỗi: ") 
x=int(input("Nhập vị trí xóa:"))
xoataivitri(line)