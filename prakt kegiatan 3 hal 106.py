# Kegiatan 3
import shelve

berkas1 =  open("L200220269", "r")
data1 = berkas1.readlines()
berkas1.close()

berkas2 = shelve.open("Muhammad Aksal")
berkas2["Biodata"] = [data1[0],data1[1],data1[2],data1[3]]
berkas2.close()
