# Order.py - مدیریت سفارش‌ها
from Menu import menu

# لیستی از دیکشنری‌ها؛ هر سفارش: {"name": ..., "price": ..., "count": ...}
orders = []


def add_order():
    name = input("نام محصول: ").strip().lower()

    if name not in menu:
        print("این محصول در منو وجود ندارد.")
        return

    try:
        count = int(input("تعداد: "))
    except ValueError:
        print("تعداد باید یک عدد صحیح باشد.")
        return

    if count <= 0:
        print("تعداد باید بزرگ‌تر از صفر باشد.")
        return

    orders.append({"name": name, "price": menu[name], "count": count})
    print(f"{count} عدد {name} ثبت شد.")


def show_orders():
    if len(orders) == 0:
        print("هنوز سفارشی ثبت نشده است.")
        return

    print("\n------ سفارش‌ها ------")
    for order in orders:
        print(f"محصول: {order['name']} | قیمت: {order['price']} تومان | تعداد: {order['count']}")
