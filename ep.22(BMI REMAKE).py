from unittest import result


print('ยินต้อนรับเข้าสู่โปรเเกรมคำนวณ BMI')

#input
height = int(input("ป้อนส่วนสูงของท่านที่นี่ (เมตร): "))
weight = int(input("ป้อนน้ำหนักของท่านที่นี่  (กิโลกรัม) : "))

#process
height/=100
bmi=weight/((height)**2)

#output
print('bmiของท่านคือ =',bmi )
if bmi<=18 and bmi>=0 :
    result = "ต่ำกว่าเกณฑ์"
elif bmi>=18.5 and bmi<=22.9 :
    result ="สมส่วน"
elif bmi>=23.0 and bmi<=24.9 :
    result ="น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.9 :
    result = "โรคอ้วนลำดับที่1"
elif bmi<=0 :
    result = "ไม่สามารถคำนวนค่าได้"
else :
    result = "โรคอ้วนระดับอันตราย" 

print("ทำนายว่าท่าน =" , result)
