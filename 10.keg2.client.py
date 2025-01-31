import socket

hostname = "localhost"
pesan = "" 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50505))
while pesan.lower() != "q":
    pesan = input("Command:")
    s.send(pesan.encode())
    if pesan.lower() == "keluar":
        s.close()
        break
    elif pesan.lower() != "q":
        response = s.recv(1024).decode()
        print("Response :", response)
s.close()
