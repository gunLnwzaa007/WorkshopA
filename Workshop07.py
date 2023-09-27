#Game Bingo โดยให้ผู้ใช้ป้อนตัวเลขที่ต้องการทายทางแป้นพิมพ์ 
#แล้วให้โปรแกรมตรวจสอบว่าตรงกับที่โปรแกรมกฎหนดไว้หรือไม่ในที่นี้คือ 25 หากไม่ตรงให้แสดงข้อความว่า "Not 
#Correct !!!." ทางหน้าจอ หากตรงให้แสดงข้อความว่า "Correct, You are the winner" 
#ขอ 3 ฟังก์ชั่น ดังนั้นต้องหาให้ได้ 3 feture

import random

def A():
    return 25  

def B(user, number):
    return user == number

def C():
    number = A()
    print("ยินดีต้อนรับสู่ Game bingo นะไอสาส!!!!")

    while True:
        user = int(input("ใส่เลข : "))

        if user == 25:
            print("เหมือนเก่งอ่ะแต่ก็ถูก!!!")
            break

        if B(user, number):
            print("Correct, You are the winner")
            break
        else:
            print("เดาไม่ถูกไอโง่!!!")
print("================/\===============")
print("===============/  \==============")
print("=======/\=====/    \=============")
print("======/  \===/      \============")
print("=====/    \=/        \===========")
C()
print("=================================")