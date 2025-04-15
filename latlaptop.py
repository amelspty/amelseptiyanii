class laptop:
     def __init__(self,merek,warna,type):
      self.merek = merek
      self.warna = warna
      self.type = type
     def hidupkan (self):
       print("laptop sedang dihidupkan")
     def matikan (self):
       print("laptop sedang dimatikan")
s1 =laptop("hp","hitam","bisnis")
print(s1.merek)
print(s1.warna)
print(s1.type)
s1.hidupkan()
s1.matikan()

