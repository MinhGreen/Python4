print("Thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành '$'")
def thaythe(line):
    x=line[0]
    for i in range(1,len(line)):
        if line[i] == line[0]:
            x+="$"
        else:
            x+=line[i]
    return x
line=input("Nhập chuỗi: ")
print(thaythe(line))