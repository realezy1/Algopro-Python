Nama = "Muhammad Aksal Pratama"
NIM = 269
Tinggi = 1.80
Berat = 55
TahunLahir = 2004
Aku = (TahunLahir,Berat,Tinggi,NIM,Nama)
Data = [TahunLahir,Berat,Tinggi,NIM,Nama]

print(type(Aku))
# Aku memiliki type Tuple
print(Aku[0])
# menghasilkan output 2004
a = Nim%4;Aku[a]
print(Aku[a])
# menghasilkan output 55
print(type(Aku[a]))
# Aku[a] memiliki type Integer
print(Aku[a:4])
# meghasilkan output (55, 1.80, 269)
print(type(Aku[4]))
# Aku[4] memiliki type String
print(Aku[0]=='ok')
# menghasilkan output False

print(type(Data))
# Data memiliki type List
print(type(Data[4]))
# Data[4] memiliki type String
print(Data[4][5])
# Tidak ada output yang dihasilkan
print(Data[4][a:6])
# menghasilkan output uhamm
Data[0] = 'oke';Data
print(Data)
# menghasilkan output ['oke', 64, 1.67, 151, 'Muhammad Aksal Pratama']
print(Data[-a])
# menghasilkan output Muhammad Aksal Pratama
print(range(a))
# menghasilkan output range(0,1)
