def luas(Lalas,Lselimut):
    luas = (2 * Lalas) + Lselimut
    return luas

Lalas = 2
Lselimut = 5
    
print("<!DECOTYPE html>\n")
print("""<html>
<head><title>Akses dengan SimpleHTTPRequestHadler</title></head>
<body><h3>Bangun Geometri</h3>""")

print("""<table><tr><td>Nama Bangunan</td><td>:</td><td>Prisma</td></tr>
                <tr><td>Dimensi</td><td>:</td><td>2D</td></tr>
                <tr><td>Rumus Luas</td><td>:</td><td>(2 * 1/2 * Asegitiga * Talas) + (3 * Stegak)</td></tr>""")
print("""<tr><td>Parameter 1</td><td>:</td><td>{0}</td></tr>""".format(Lalas))
print("""<tr><td>Parameter 2</td><td>:</td><td>{0}</td></tr>""".format(Lselimut))
print(
    """<tr><td>Luas</td><td>:</td><td>{0}</td></tr>""".format(luas(Lalas,Lselimut)))
print("""</body></html>""")
