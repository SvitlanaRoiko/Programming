# Дані магазину
products = {
    "1": {"name": "Булочка з маком",        "price": 25.50,  "stock": 10},
    "2": {"name": "Чай",      "price": 57.90,  "stock": 5},
    "3": {"name": "Яблука (кг)", "price": 38.75,  "stock": 8},
    "4": {"name": "Кава",        "price": 120.00, "stock": 3},
}

ADMIN_PASSWORD = "admin123"
cart = []

# Функції
format_price = lambda price: f"{price:.2f}грн"
cart_total = lambda: sum(product["price"] for product in cart)


def show_catalog():
    print("\n--- КАТАЛОГ ---")
    for product_id, product in products.items():
        print(f"{product_id}. {product['name']} - {format_price(product['price'])} (залишок: {product['stock']})")


def show_cart():
    print("\n--- КОШИК ---")
    if not cart:
        print("Кошик порожній")
        return
    for index, product in enumerate(cart, 1):
        print(f"{index}. {product['name']} - {format_price(product['price'])}")
    print(f"Разом: {format_price(cart_total())}")


def add_to_cart():
    show_catalog()
    choice = input("Номер товару: ")
    if choice in products and products[choice]["stock"] > 0:
        selected = products[choice]
        cart.append({"name": selected["name"], "price": selected["price"]})
        selected["stock"] -= 1
        print(f" {selected['name']} додано в кошик")
    else:
        print("Товару немає або він закінчився")


def remove_from_cart():
    show_cart()
    if not cart:
        return
    try:
        number = int(input("Номер товару для видалення: "))
        removed = cart.pop(number - 1)
        # повертаємо товар на склад
        for product in products.values():
            if product["name"] == removed["name"]:
                product["stock"] += 1
        print(f"0"
              f" {removed['name']} видалено з кошика")
    except (ValueError, IndexError):
        print("Неправильний номер")


def buy():
    show_cart()
    if not cart:
        return
    print(f"До сплати: {format_price(cart_total())}")
    if input("Підтвердити покупку? (т/н): ").lower() == "т":
        cart.clear()
        print("Дякуємо за покупку!")


def admin_panel():
    if input("Пароль: ") != ADMIN_PASSWORD:
        print("Невірний пароль")
        return
    print("\n--- ЗАЛИШКИ НА СКЛАДІ ---")
    for product in products.values():
        print(f"{product['name']}: {product['stock']} шт.")


def menu():
    actions = {
        "1": show_catalog,
        "2": add_to_cart,
        "3": remove_from_cart,
        "4": show_cart,
        "5": buy,
        "6": admin_panel,
    }
    while True:
        print("\n=== МАГАЗИН ===")
        print("1. Каталог  2. В кошик  3. З кошика")
        print("4. Кошик    5. Купити   6. Адмін   0. Вихід")
        choice = input("> ")
        if choice == "0":
            break
        action = actions.get(choice, lambda: print("Немає такого пункту"))
        action()


if __name__ == "__main__":
    menu()
