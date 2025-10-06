st1 = "!()-[]{};:"",<>./?@#$%^&*_~"
st2 = " "

st = input("Nhap chuoi: ")
for i in st:
    if i not in st1:
        st2 = st2 + i
print("chuoi vua nhap la: ", st)
print("Chuoi sau khi loại bỏ kí tự đặc biệt" ,st2)