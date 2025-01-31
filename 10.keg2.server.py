import socket
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50505))
s.listen(5)
print("Program komunikasi tentang server")
data = ""

while data.lower() != "q":
    komm, addr = s.accept()
    while data.lower() != "q":
        data = komm.recv(1024).decode()
        print("Command:", data)
        if data.lower() == "machine":
            respon = platform.machine()
            komm.send(respon.encode())
        if data.lower() == "release":
            respon = platform.release()
            komm.send(respon.encode())
        if data.lower() == "system":
            respon = platform.system()
            komm.send(respon.encode())
        if data.lower() == "version":
            respon = platform.version()
            komm.send(respon.encode())
        if data.lower() == "node":
            respon = platform.node()
            komm.send(respon.encode())
        else :
            komm.send("unknown command".encode())
