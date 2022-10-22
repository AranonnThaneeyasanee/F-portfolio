age=int(input("ป้อนอายุของคุณ : ")) 

if age>=15 :
    print("คำนำหน้าเป็น นาย/นางสาว")
else : 
    print("คำนำหน้าเป็นเด็กชาย/เด็กหญิง")
print("เสร็จสินกระบวนการ")

age=int(input("enter your age : ")) 
if age>=15 and age <=30 :
    print("young")
elif age>=30 and age <=50 :
    print("adult")
elif age>=50 :
    print("Aging")
else : 
    print("child")
print("end the program")

#<child
#15-20 = young
#30-50 = adult
#>50 = Aging