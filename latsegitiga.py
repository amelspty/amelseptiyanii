class segitiga :
   def __init__(self,alas,tinggi):
     self.alas = alas
     self.tinggi = tinggi 
   def hitung_luas(self):
     luas = 0.5*self.alas*self.tinggi
     print("luas alas segitiga,luas" , luas)

s1 = segitiga (20 , 10)
s1.hitung_luas()
     



