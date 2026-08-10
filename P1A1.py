def generate_bill():
    DISCOUNT_THRESHOLD = 3000
    DISCOUNT_RATE = 0.10

    customer_name = input("Enter customer name: ")

    total_amount = 0.0
    products = []

    for i in range(1, 4):
        name = input(f"Enter name of product {i}: ")

        while True:
            try:
                price = float(input(f"Enter price of {name} (Rs.): "))
                if price >= 0:
                    break
                print("Price cannot be negative.")
            except ValueError:
                print("Invalid price.")

        total_amount += price
        products.append((name, price))

    discount = total_amount * DISCOUNT_RATE if total_amount > DISCOUNT_THRESHOLD else 0.0
    final_amount = total_amount - discount

    print("\n" + "=" * 40)
    print("           SMART SHOPPING BILL")
    print("=" * 40)
    print(f"Customer Name : {customer_name}")
    print("-" * 40)
    print(f"{'Product':<20}{'Price (Rs.)':>20}")
    print("-" * 40)

    for name, price in products:
        print(f"{name:<20}{price:>20.2f}")

    print("-" * 40)
    print(f"{'Total Amount':<20}{total_amount:>20.2f}")
    print(f"{'Discount':<20}{discount:>20.2f}")
    print(f"{'Final Payable':<20}{final_amount:>20.2f}")
    print("=" * 40)


if __name__ == "__main__":
    generate_bill()