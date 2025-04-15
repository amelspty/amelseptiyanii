class hp:
     def __init__(self,merek,warna,type):
      self.merek = merek
      self.warna = warna
      self.type = type
     def telepon (self):
       print("telepon")
     def sms (self):
       print("kirim sms")
     def  panggilan (self):
       print("terima panggilan")
s1 =laptop("oppo","merah","android")
print(s1.merek)
print(s1.warna)
print(s1.type)
s1.telepon()
s1.sms()
