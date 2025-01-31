import socket

#persiapan connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000
s.bind(('',port))
s.listen(2)
print("Server siap")

#message
success = "Data disimpan"

AlasSegitiga = ''
TinggiSegitiga = ''
pesan = ''

while(pesan.lower() != 'y'):
    komm, addr = s.accept()
    while(pesan.lower() != 'y'):
        pesan = komm.recv(1024).decode()
        if(pesan.lower() == 'y'):
            hitungLuas = AlasSegitiga * TinggiSegitiga / 2
            luas = int(hitungLuas)
            print(luas)
            resend = str(luas)
            komm.send(resend.encode())
            s.close()
            break
        elif(AlasSegitiga == ''):
            AlasSegitiga = int(pesan)
            print("Alas Segitiga : " ,AlasSegitiga)
            komm.send(success.encode())
        elif(TinggiSegitiga == ''):
            TinggiSegitiga = int(pesan)
            print("TinggiSegitiga : ",TinggiSegitiga)
            komm.send(success.encode())
            
        

    
