#คำนวณค่าคอมมิชชั่นของพนักงานขาย โดยป้อนรหัสพนักงาน ชื่อ
#พนักงาน และจำนวนเงินซึ่งเป็นยอดขายของพนักงาน จากผู้ใช้ทางแป้นพิมพ์ และคำนวณค่าคอมมิชชั่น จาก
#เงื่อนไข ดังนี้
 #ขายของได้ไม่เกิน 1000 บาท ค่าคอมมิชชั่น เป็น 0.0 บาท
 #ขายของได้ตั้งแต่ 1001 ถึง 2000 บาท ค่าคอมมิชชั่นคิด 1% จากยอดขาย
 #ขายของได้ตั้งแต่ 2001 ถึง 3000 บาท ค่าคอมมิชชั่นคิด 3% จากยอดขาย
 #ขายของได้ตั้งแต่ 3001 บาท ขึ้นไป ค่าคอมมิชชั่นคิด 5% จากยอดขาย

def A(SA):
    if SA <= 1000:
        C = 0.0
    elif SA <= 2000:
        C = SA * 0.01
    elif SA <= 3000:
        C = SA * 0.03
    else:
        C = SA * 0.05
    
    return C

def B(id, name, C):
    print("รหัสพนักงาน :", id)
    print("ชื่อพนักงาน :", name)
    print("ยอดขาย :", SA)
    print("ค่าคอมมิชชั่น :", C)
print("=================================")
print("======= คำนวณค่าคอมมิชชั่น ========")
print("=================================")
id = input("ใส่รหัสพนักงาน : ")
name = input("ใส่ชื่อพนักงาน : ")
SA = float(input("ใส่ยอดขาย : "))

C = A(SA)
B(id, name, C)
print("=================================")
