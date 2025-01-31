import socket

#persiapan connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
port = 5000
s.connect((hostname,port))
print("Menghitung luas Segitiga")

pesan = ''
AlasSegitiga = ''
TinggiSegitiga = ''
#intmain

while(pesan != 'y'):
    if(AlasSegitiga == ''):
        AlasSegitiga = input("Alas segitiga ? ")
        s.send(AlasSegitiga.encode())
        response = s.recv(1024).decode()
        print("Response : " ,response)
    elif(TinggiSegitiga == ''):
        TinggiSegitiga = input("Tinggi segitiga ? ")
        s.send(TinggiSegitiga.encode())
        response = s.recv(1024).decode()
        print("Response : " ,response)
    else:
        pesan = input('Hitung ? (y/n)')
        s.send(pesan.encode())

pesan = s.recv(1024).decode()
print("Response : ",pesan)
s.close()
