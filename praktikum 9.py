# Kegiatan 1
a = open("L200180175","w")
a.write("L200180175\n")
a.write("11-04-2000\n")
a.write("Afrialdy Asyura Buana\n")
a.write("Kartasura")
a.close()

# Kegiatan 2,3,4

import shelve

a = open("L200180175","r")

b = shelve.open("Praktikum 9.data")
b["Data"] = a.read()
b.close

a.close()

b = shelve.open("Praktikum 9.data")
print(b["Data"])
b.close()
