# type Coversion
x=10
y=9.9999
z="สวัสดี"
h="40" #streคือการนำ " "
#บวกเลข
result = x+int(h)
print(type(x))
print(type(y))
print(type(z))
print(result)
print("ผลลัพธ์ของข้อที่หนึ่งคือ = " + str(result))
result = str(x)+h #เเปลงx=intเป็นstr #str
print(type(result))
result = x+int(h) #เเปลงh=strเป็นint #int
print(type(result))
result = x+int(h)
print(result)
print(float(h)) #เเปลง str เป็น float
print(str(y)) #เเปลง float เป็น str
print(int(y)) #เเปลง float เป็น int 
print(float(x)) #เเปลง int เป็น float 
x = (float(x))
print(type(x))
result=(x+y)
print(result)
x=x+100
print(x)
print(type(x))


u=80
i=90
o=6.666
p='60'
p = (int(p))
print(type(p))