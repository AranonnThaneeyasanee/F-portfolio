#โปรเเกรมค่า bmi 

from turtle import window_height
print('ยินต้อนรับเข้าสู่โปรเเกรมคำนวณ BMI')

#input
height = int(input("ป้อนส่วนสูงของท่านที่นี่ (เมตร): "))
weight = int(input("ป้อนน้ำหนักของท่านที่นี่  (กิโลกรัม) : "))

#process
height/=100
bmi=weight/((height)**2)

#output
print('bmiของท่านคือ',bmi)

