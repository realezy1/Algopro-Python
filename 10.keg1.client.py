import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print("Mesin penjawab otomatis siap")
while True:
    pesan = input('Pertanyaan:')
    s.send(pesan.encode())
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print("Jawaban :", response.decode())
    else:
        print("Siap")
        s.close()
        break
