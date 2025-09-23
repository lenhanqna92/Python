st = input("Nhap chuoi: ")
print("Chuoi cua ban la: ", st)
st2 = input("Nhap chuoi can tim: ")
index = st.find(st2)
if st2 in st:
    print("Chuoi da duoc tim thay !, vi tri cua chuoi la: ",index)
else:
    print('khong tim thay')