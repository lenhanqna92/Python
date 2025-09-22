"""mail = "lenhan@gmail.com Sat Jan 5 09:14:16"
Start_position = mail.find("@")               
End_position = mail.find(" ", Start_position) 
host = mail[Start_position +1 : End_position]
print(host) """

mail2 = input("Nhap email: ")
dau = mail2.find("@")
#cuoi = mail2.find()
host = mail2[dau+1:]
print(host)
