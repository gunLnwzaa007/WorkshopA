#ตรวจสอบค่า PH ของนํ้าปะปาจากจังหวัดต่างๆ โดยรับชื่อจังหวัด 
#และค่า PH ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ โดยหากค่า PH เป็น 7-8 แสดงข้อความ "Result is Normal" 
#หากค่า PH มากกว่า 8 ให้แสดงข้อความ "Result is Acid" หากค่า PH น้อยกว่า 7 ให้แสดงข้อความ "Result is Alkali"

def A(P, PV):
    if PV >= 7 and PV <= 8:
        R = "Result is Normal"
    elif PV > 8:
        R = "Result is Acid"
    else:
        R = "Result is Alkali"

    print(f"Province: {P}")
    print(f"pH Value: {PV}")
    print(f"Result: {R}")

print("=================================")
print("========= ตรวจสอบค่า PH ==========")
print("=================================")
name = input("ใส่ชื่อจังหวัด : ")
pv = float(input("ค่า pH : "))

A(name, pv)
print("=================================")
