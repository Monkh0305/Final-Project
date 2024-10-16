import pickle
import os

DATA_FILE = "car_inventory.bin"

def save_data():
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(car_inventory, f)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return []

car_inventory = load_data()

# ฟังก์ชันเพิ่มข้อมูลรถ
def add_car():
    plate = input("กรุณาใส่ทะเบียนรถ: ")
    brand = input("กรุณาใส่ยี่ห้อรถ: ")
    model = input("กรุณาใส่รุ่นรถ: ")
    car_type = input("กรุณาใส่ประเภทของรถ: ")
    # ดัก error สำหรับจำนวนรถ
    while True:
        quantity_input = input("กรุณาใส่จำนวนรถ: ")
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            if quantity < 0:
                print("จำนวนรถต้องไม่เป็นลบ กรุณากรอกใหม่.")
                continue
            break
        else:
            print("กรุณาใส่ตัวเลขสำหรับจำนวนรถ.")

    # ดัก error สำหรับปีผลิต
    while True:
        year_input = input("กรุณาใส่ปีผลิต: ")
        if year_input.isdigit():
            year = int(year_input)
            if year < 1886:
                print("ปีผลิตต้องมากกว่า 1886 กรุณากรอกใหม่.")
                continue
            break
        else:
            print("กรุณาใส่ตัวเลขสำหรับปีผลิต.")

    # ดัก error สำหรับราคา
    while True:
        price_input = input("กรุณาใส่ราคารถ (ต่อคัน): ")
        if price_input.replace('.', '', 1).isdigit():
            price = float(price_input)
            if price < 0:
                print("ราคารถต้องไม่เป็นลบ กรุณากรอกใหม่.")
                continue
            break
        else:
            print("กรุณาใส่ตัวเลขสำหรับราคารถ.")

    # แสดงข้อมูลที่กรอกให้ผู้ใช้ตรวจสอบ
    print("\nข้อมูลรถที่กรอก:")
    print(f"ทะเบียน: {plate}")
    print(f"ยี่ห้อ: {brand}")
    print(f"รุ่น: {model}")
    print(f"ประเภท: {car_type}")
    print(f"จำนวน: {quantity}")
    print(f"ปีผลิต: {year}")
    print(f"ราคา: {price}")

    # ขอการยืนยันจากผู้ใช้
    confirm = input("คุณแน่ใจว่าต้องการบันทึกข้อมูลนี้? (กด 'Y' เพื่อยืนยัน, 'N' เพื่อยกเลิก): ").strip().upper()

    if confirm == 'Y':
        car_inventory.append({
            "plate": plate,
            "brand": brand,
            "model": model,
            "car_type": car_type,
            "quantity": quantity,
            "year": year,
            "price": price
        })
        save_data()
        print("เพิ่มข้อมูลสำเร็จ!\n")
    elif confirm == 'N':
        print("ยกเลิกการบันทึกข้อมูลรถ.\n")
    else:
        print("ข้อมูลที่ป้อนไม่ถูกต้อง ยกเลิกการดำเนินการ.\n")

# ฟังก์ชันแสดงข้อมูลทั้งหมด
def show_all_cars():
    total_price_all = 0
    if not car_inventory:
        print("ไม่มีข้อมูลรถในคลัง\n")
    else:
        print("=" * 120)
        print(f"{'ทะเบียน':<12} {'ยี่ห้อ':<16} {'รุ่น':<15} {'ประเภท':<14} {'ปีผลิต':<12} {'จำนวน':<13} {'ราคา(ต่อคัน)':<22} {'ราคารวมทั้งหมด':<15}")
        print("-" * 120)
        for car in car_inventory:
            price_str = f"{car['price']:,.2f}"  # แปลงราคาต่อคันเป็นสตริง
            total_price = car['price'] * car['quantity']  # คำนวณราคารวมต่อรายการ
            total_price_str = f"{total_price:,.2f}"
            total_price_all += total_price  # สะสมราคารวมทั้งหมดของรถยนต์
            print(f"{car['plate']:<10} {car['brand']:<13} {car['model']:<14} {car['car_type']:<14} 
            {car['year']:<12} {car['quantity']:<2} {price_str:>18} บาท {total_price_str:>18} บาท")
        print("=" * 120)
        total_price_all_str = f"{total_price_all:,.2f}"
        print("ราคารถยนต์ทั้งหมดรวม ", total_price_all_str, "บาท")
        print("\n")



# ฟังก์ชันค้นหาข้อมูลรถ
def search_car():
    search_plate = input("กรุณาใส่ทะเบียนรถที่ต้องการค้นหา: ")
    for car in car_inventory:
        if car['plate'] == search_plate:
            total_price_all = 0
            price_str = f"{car['price']:,.2f}"  # แปลงราคาต่อคันเป็นสตริง
            total_price = car['price'] * car['quantity']  # คำนวณราคารวมต่อรายการ
            total_price_str = f"{total_price:,.2f}"
            total_price_all += total_price  # สะสมราคารวมทั้งหมดของรถยนต์
            print(f"พบข้อมูลรถทะเบียน {search_plate}:")
            print("=" * 110)
            print(f"{'ยี่ห้อ':<16} {'รุ่น':<15} {'ประเภท':<14} {'ปีผลิต':<12} {'จำนวน':<13} {'ราคา(ต่อคัน)':<22} {'ราคารวมทั้งหมด':<15}")
            print("=" * 110)
            print(f"{car['brand']:<12} {car['model']:<14} {car['car_type']:<14} {car['year']:<12} {car['quantity']:<2} {price_str:>18} บาท {total_price_str:>18} บาท")
            print("-" * 110)
            return
    print(f"ไม่พบข้อมูลรถทะเบียน {search_plate}\n")

# ฟังก์ชันอัปเดตข้อมูลรถ
def update_car():
    update_plate = input("กรุณาใส่ทะเบียนรถที่ต้องการอัปเดต: ")
    for car in car_inventory:
        if car['plate'] == update_plate:
            print(f"ข้อมูลปัจจุบันของรถทะเบียน {update_plate}:")
            print(f"ยี่ห้อ: {car['brand']}, รุ่น: {car['model']}, ประเภท: {car['car_type']}, จำนวน: {car['quantity']}, ปีผลิต: {car['year']}, ราคา: {car['price']}")

            new_brand = input(f"กรุณาใส่ยี่ห้อใหม่ (ปัจจุบัน: {car['brand']}): ") or car['brand']
            new_model = input(f"กรุณาใส่รุ่นใหม่ (ปัจจุบัน: {car['model']}): ") or car['model']
            new_car_type = input(f"กรุณาใส่ประเภทใหม่ (ปัจจุบัน: {car['car_type']}): ") or car['car_type']

            new_quantity_input = input(f"กรุณาใส่จำนวนใหม่ (ปัจจุบัน: {car['quantity']}): ")
            new_quantity = int(new_quantity_input) if new_quantity_input else car['quantity']

            new_year_input = input(f"กรุณาใส่ปีผลิตใหม่ (ปัจจุบัน: {car['year']}): ")
            new_year = int(new_year_input) if new_year_input else car['year']

            new_price_input = input(f"กรุณาใส่ราคาต่อคันใหม่ (ปัจจุบัน: {car['price']}): ")
            new_price = float(new_price_input) if new_price_input else car['price']

            print("\nข้อมูลที่กรอก:")
            print(f"ยี่ห้อ: {new_brand}, รุ่น: {new_model}, ประเภท: {new_car_type}, จำนวน: {new_quantity}, ปีผลิต: {new_year}, ราคา: {new_price} บาท")

            confirm = input("คุณแน่ใจว่าต้องการอัปเดตข้อมูลนี้? (กด 'Y' เพื่อยืนยัน, 'N' เพื่อยกเลิก): ").strip().upper()

            if confirm == 'Y':
                car['brand'] = new_brand
                car['model'] = new_model
                car['car_type'] = new_car_type
                car['quantity'] = new_quantity
                car['year'] = new_year
                car['price'] = new_price
                save_data()
                print("อัปเดตข้อมูลสำเร็จ!\n")
                return
            elif confirm == 'N':
                print("ยกเลิกการอัปเดตข้อมูลรถ.\n")
                return
            else:
                print("ข้อมูลที่ป้อนไม่ถูกต้อง ยกเลิกการดำเนินการ.\n")
                return
    print(f"ไม่พบข้อมูลรถทะเบียน {update_plate}\n")

# ฟังก์ชันลบข้อมูลรถ
def delete_car():
    delete_plate = input("กรุณาใส่ทะเบียนรถที่ต้องการลบ: ")
    for car in car_inventory:
        if car['plate'] == delete_plate:
            print(f"ข้อมูลที่จะลบ: {car}")
            confirm = input("คุณแน่ใจว่าต้องการลบข้อมูลนี้? (กด 'Y' เพื่อยืนยัน, 'N' เพื่อยกเลิก): ").strip().upper()

            if confirm == 'Y':
                car_inventory.remove(car)
                save_data()
                print(f"ลบข้อมูลรถทะเบียน {delete_plate} สำเร็จ!\n")
                show_all_cars()  # เรียกใช้ฟังก์ชันเพื่อแสดงข้อมูลรถทั้งหมดหลังจากลบ
                return
            elif confirm == 'N':
                print("ยกเลิกการลบข้อมูลรถ.\n")
                return
            else:
                print("ข้อมูลที่ป้อนไม่ถูกต้อง ยกเลิกการดำเนินการ.\n")
                return
    else:
        print(f"ไม่พบข้อมูลรถทะเบียน {delete_plate}\n")

# ฟังก์ชันสร้างรายงาน
def generate_report():
    if not car_inventory:
        print("ไม่มีข้อมูลรถในคลังสำหรับสร้างรายงาน\n")
    else:
        confirm = input("คุณแน่ใจว่าต้องการสร้างรายงาน? (กด 'Y' เพื่อยืนยัน, 'N' เพื่อยกเลิก): ").strip().upper()

        if confirm == 'Y':
            car_types = {}
            total_cars = 0
            total_value = 0  # ค่ารวมทั้งหมด

            for car in car_inventory:
                if car['car_type'] not in car_types:
                    car_types[car['car_type']] = []
                car_types[car['car_type']].append(car)
                total_cars += car['quantity']
                total_value += car['quantity'] * car['price']  # คำนวณค่ารวมทั้งหมด

            with open("car_report.txt", "w", encoding="utf-8") as f:
                f.write("                                รายงานแยกประเภทรถยนต์                            \n")
                f.write(f"จำนวนประเภทรถทั้งหมด: {len(car_types)}\n")
                f.write(f"จำนวนรถยนต์ทั้งหมด: {total_cars}\n")
                f.write(f"มูลค่ารวมทั้งหมด: {total_value:,.2f} บาท\n")
                for car_type, cars in car_types.items():
                    total_quantity = sum(car['quantity'] for car in cars)
                    total_type_value = sum(car['quantity'] * car['price'] for car in cars)  # คำนวณค่ารวมของแต่ละประเภท
                    f.write(f"\nประเภทรถ: {car_type}\n")
                    f.write(f"จำนวนรถยนต์: {total_quantity}\n")
                    f.write(f"มูลค่ารวมของประเภทนี้: {total_type_value:,.2f} บาท\n")
                    f.write(f"+{'-'*12}+{'-'*11}+{'-'*9}+{'-'*10}+{'-'*8}+{'-'*15}+{'-'*18}+\n")
                    f.write(f"| {'ทะเบียน':<11} | {'ยี่ห้อ':<12} | {'รุ่น':<9} | {'ปีผลิต':<9} | {'จำนวน':<6} | {'ราคา(ต่อคัน)':<15} | {'ราคารวมทั้งหมด':<19}|\n")
                    f.write(f"+{'-'*12}+{'-'*11}+{'-'*9}+{'-'*10}+{'-'*8}+{'-'*15}+{'-'*18}+\n")
                    for car in cars:
                        total_car_value = car['quantity'] * car['price']
                        f.write(f"| {car['plate']:<10} | {car['brand']:<9} | {car['model']:<7} | {car['year']:<8} | {car['quantity']:<6} | {car['price']:>13,.2f} | {total_car_value:>17,.2f}|\n")
                    f.write(f"+{'-'*12}+{'-'*11}+{'-'*9}+{'-'*10}+{'-'*8}+{'-'*15}+{'-'*18}+\n")

            print("รายงานถูกสร้างและบันทึกในไฟล์ 'car_report.txt'\n")
        elif confirm == 'N':
            print("ยกเลิกการสร้างรายงาน.\n")
        else:
            print("ข้อมูลที่ป้อนไม่ถูกต้อง ยกเลิกการดำเนินการ.\n")



# ฟังก์ชันหลัก
def main():
    while True:
        print("\n===== ระบบจัดการรถยนต์ =====")
        print("1. เพิ่มข้อมูลรถ")
        print("2. แสดงข้อมูลรถทั้งหมด")
        print("3. ค้นหาข้อมูลรถ")
        print("4. อัปเดตข้อมูลรถ")
        print("5. ลบข้อมูลรถ")
        print("6. สร้างรายงาน")
        print("0. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกทำรายการ: ").strip()
        if choice == '1':
            add_car()
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")
        elif choice == '2':
            show_all_cars()
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")
        elif choice == '3':
            search_car()
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")
        elif choice == '4':
            update_car()
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")
        elif choice == '5':
            delete_car()
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")
        elif choice == '6':
            generate_report()
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")
        elif choice == '0':
            print("ออกจากโปรแกรม...")
            break
        else:
            print("รายการไม่ถูกต้อง กรุณาลองใหม่\n")
            input("กด Enter เพื่อกลับไปยังเมนูหลัก...")

if __name__ == "__main__":
    main()
