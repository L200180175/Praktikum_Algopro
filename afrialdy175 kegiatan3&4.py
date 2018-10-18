Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> ##kegiatan 3
>>> Nama = 'Afrialdy Asyura Buana'
>>> NIM = 'L200180175'
>>> X = '1' + NIM[7:] # variabel X menyimpan data 1 dan 3 digit terakhir dari NIM saya
>>> a = int(X) # variabel A menyimpan konversi string variabel X ke integer
>>> b = len(Nama) # variabel B menyimpan konversi Variabel X dengan cara menghitung jumlah huruf yang ada didalam kata Nama
>>> type(a) # menyeleksi objek di variabel a
<class 'int'>
>>> type(b) # menyeleksi objek di variabel b
<class 'int'>
>>> a/b # membagi variabel a dengan variabel b
55.95238095238095
>>> a//b # membagi variabel a dengan variabel b lalu dibulatkan menjadi puluhan
55
>>> 10*(a-999) # mengalikan 10 dengan variabel a yang dikurangi dengan 999
1760
>>> b**2 # mengkuadratkan variabel b
441
>>> a%b # menghitung hasil sisa pembagian a dengan b
20
>>> c = 12.5
>>> type(c) # menyeleksi objek di variabel c
<class 'float'>
>>>  a/c # membagi variabel a dengan variabel c
SyntaxError: unexpected indent
>>> a/c # membagi variabel a dengan variabel c
94.0
>>> a//c # membagi variabel a dengan variabel c lalu dibulatkan menjadi puluhan
94.0
>>> a%c # membagi hasil sisa pembagian a dengan c
0.0
>>> c>b # mengecek apakah variabel c lebih besar daripada b
False
>>> type(c > b) # menyeleksi objek apakah variabel c lebih besar daripada b
<class 'bool'>
>>> a > b and b > c # mengecek apakah a lebih besar b dan b lebih besar c merupakan boolean atau decision
True
>>> a > 1100 or b < 10 # mengecek a lebih besar 1100 atau b lebih kecil dari 10 merupakan boolean atau decision
True
>>> 
>>> ##kegiatan 4
>>> Nama = 'Afrialdy Asyura Buana'
>>> NIM = 175
>>> Tinggi = 1.70
>>> Berat = 57
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku) # Memeriksa tipe data dari Aku adalah tuple, karena ditulis dengan kurung biasa dan elemen list tidak dapat diubah
<class 'tuple'>
>>> Aku[0] # Menampilkan tahun lahir karena pada Aku indeks ke 0 adalah data dari TahunLahir
2000
>>> a = NIM%4;Aku[a] # Karena sisa hasil bagi dari NIM = 175 dan 4 adalah 175 maka Aku[a] sama dengan Aku[70] yang menampilkan indeks ke 175 adalah data dari NIM
175
>>> type(Aku[a]) # Memeriksa tipe data dari Aku indeks ke 175 adalah integer, 175 adalah bilangan bulat
<class 'int'>
>>> Aku[a:4] # a = 175 maka Aku[175:4] adalah menampilkan indeks 175 hingga indeks 4
(175,)
>>> type(Aku[4]) # Memeriksa tipe data dari Aku indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Afrialdy Asyura Buana’
<class 'str'>
>>> Aku[0]='ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    Aku[0]='ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal
TypeError: 'tuple' object does not support item assignment
>>> type(Data) # Memeriksa tipe data dari Aku adalah list, karena ditulis dengan kurung siku dan elemen list dapat diubah
<class 'list'>
>>> type(Data[4]) # Memeriksa tipe data dari Data indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Afrialdy Asyura Buana’
<class 'str'>
>>> Data[4][5] # Menampilkan huruf ke 5 dari sebuah Data indeks 4
'l'
>>> Data[4][a:6] # Menampilkan slicing dari indeks 3 sampai indeks 5 dari sebuah Data indeks 4
'ial'
>>> Data[0]='ok';Data # Karena elemen list, indeks 0 dapat diubah menjadi string ‘ok’ dan indeks data menjadi ['ok', 57, 1.7, 175, 'Afrialdy Asyura Buana']
['ok', 57, 1.7, 175, 'Afrialdy Asyura Buana']
>>> Data[-a] # Menampilkan indeks 175 dari belakang karena a = 175 maka Data[-175]
1.7
>>> range(a) # Range untuk membuat list baru 0 – 3 karena dengan data a adalah 175
range(0, 3)
>>> 
