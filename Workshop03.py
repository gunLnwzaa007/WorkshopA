#คำนวณภาษี ณ ที่จ่ายของสินค้า
#โดยรับซื้อสินค้า และราคาสินค้า ทางแป้นพิมพ์ และแสดงผลภาษีที่คำนวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที่ร้อยละ 7 ของราคาสินค้า
#ขอ 3 ฟังก์ชั่น ดังนั้นต้องหาให้ได้ 3 feture

def A():
    product = float(input("กรุณากรอกราคาสินค้า: "))
    return product

def B(product):
    tax_rate = 7  
    tax = (product_price * tax_rate) / 100
    return tax

def C(tax_amount):
    print(f"ภาษีที่คำนวณได้: {tax_amount:.2f} บาท")
print("++++++++++++++++++++++")
print("++++คำนวนภาษีราคาสินค้า++")
print("++++++++++++++++++++++")
product_price = A()
print("++++++++++++++++++++++")
tax = B(product_price)
C(tax)
print("++++++++++++++++++++++")