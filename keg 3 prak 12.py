def hitung(sisialas,tinggi) :
    sa=sisialas
    t=tinggi
    V=(sa**2*t)/3
    return V
sisialas = 6
tinggi = 10

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Volume Bangun Geometri</title></head>
<body>"""
print """<table>
<tr>
    <th rowspan='8' width='150'> GAMBAR </th>
    <td><h3> Bangun Geometri <h3></td>
</tr>
<tr>
    <td>Nama Bangun</td>
    <td>:</td>
    <td>Piramid</td>
</tr>
<tr>
    <td>Dimensi (2D/3D)</td>
    <td>:</td>
    <td>3d</td>
</tr>
<tr>
    <td>Rumus Luas</td>
    <td>:</td>
    <td>(sa**2*t)/3</td>
</tr>
<tr>
    <td>Sisi Alas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(sisialas)
print """<tr>
    <td>Tinggi</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(tinggi)
print """<tr>
    <td>Luas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(hitung(sisialas,tinggi))
print"""
</table>"""

print"</body></html>"
