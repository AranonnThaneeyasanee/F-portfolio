from ast import Return
from unittest import result


print('กรุณาป้อนข้ออมูลเพื่อlogin')
email=input( 'ป้อน email ของท่าน : ' ) #inputdata 
pw=input('ป้อนรหัสผ่านของท่าน : ')
print('กรุณาตรวจสอบอีเมลเเละรหัสผ่านของท่าน')
print(email)
print(pw)
submit=input('ป้อนยืนยันตรงช่องนี้ :')
print('กรุณาป้อนข้อมูลเหล่านี้')
height=input("ป้อนความสูงของท่าน :") #inputdata
weight=input("ป้อนน้ำหนักของท่าน : ")

#process
result=int(weight)*31

#output
print("แคลโลลี่ที่ท่านต้องใช้ในแต่ละวัน = " + str(result))
