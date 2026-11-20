# Billing.py - محاسبه هزینه و صدور فاکتور
from Order import orders


def calculate_total():
    total = 0
    for order in orders:
        total += order["price"] * order["count"]
    return total


def calculate_discount(total):
    if total > 1000000:
        return int(total * 10 / 100)
    return 0


def print_invoice():
    if len(orders) == 0:
        print("سفارشی برای صدور فاکتور وجود ندارد.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final = total - discount

    print("\n========== فاکتور ==========")
    for order in orders:
        print(f"{order['name']} × {order['count']}")
    print("----------------------------")
    print(f"مبلغ کل: {total} تومان")
    print(f"تخفیف: {discount} تومان")
    print(f"مبلغ قابل پرداخت: {final} تومان")
    print("============================")
