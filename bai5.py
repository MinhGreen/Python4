print("Tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.")
def minmaxchuoi(line):
    max=min=line[0]
    for i in line:
        if min>i:
            min=i
        if max<i:
            max=i
    print("Kí tự lớn nhất là: ",max)
    print("Kí tự nhỏ nhất là: ",min)
line=input("Nhập chuỗi: ")
minmaxchuoi(line)