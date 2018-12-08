import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server sudah siap"
perintah = ''
sa=0
t=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'tinggi':
                t = int(data[1])
                respon = "tinggi dicatat"
                komm.send(respon)
            elif perintah == 'sisi alas':
                sa = int(data[1])
                respon = "sisi alas dicatat"
                komm.send(respon)
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            V = float (sa**2 * t)/3
            respon = "Volume piramid dengan sisi alas {} dan tinggi {} adalah {}".format(sa,t,V)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
