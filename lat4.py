class Siswa:
   smk = "SMKN 4 Tasikmalaya"

   def __init__(self,nama,kelas):
     self.nama = nama
     self.kelas =kelas

   def belajar(self):
    print(f"{self.nama} sedang belajar")

s1 = Siswa("amel","X PPLG 1")
print(s1.nama)
print(s1.kelas)
print(s1.smk)