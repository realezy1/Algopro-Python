import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print ("Server penjawab otomatis sudah siap")
data = ""
kamus = {"nama":"Muhammad Aksal", "NIM":"L200220269","angkatan":"2022"}

while data.lower() != "q":
    komm, addr = s.accept()
    while data.lower() != "q":
        data = komm.recv(1024)
        if data.lower() == "q":
            s.close()
            break
        print("Pertanyaan", data.decode())
        if data.decode() in kamus:
            komm.send(kamus[data.decode()].encode())
        else :
            komm.send("Maaf,perintah tidak dimengerti".encode())

