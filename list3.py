item = []
price = []

for i in range(6):
    itm = input(f"Enter item ({i+1}): ")
    prc = input(f"Enter price of ({itm}) R: ")
    item.append(itm)
    price.append(prc)


def calculate_total(item, price):
    total = 0
    for p in price:
        total += float(p)
    print(f"Total cost of groceries: {total}")
    for i in range(6):
        print(f"{item[i]}: R{price[i]}")


calculate_total(item, price)
