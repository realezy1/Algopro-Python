import shelve
berkas = shelve.open("Muhammad Aksal")
data = berkas["Biodata"]
for i in data :
    print(i)
berkas.close()
