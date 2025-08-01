sneakers = ["Nike", "Adidas", "Puma", "Reebok", "New Balance"]
for sneakers in sneakers:
    print(sneakers)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    print(day)


def contacts(names):
    for name in names:
        print(name)


contacts(["Alice", "Bob", "Charlie", "Diana"])

groceries = ["Apples", "Bananas", "Carrots", "Dates", "Eggs", "Fish"]
groceries.append("Grapes")
groceries.remove("Carrots")
print("total groceries:", len(groceries))
print("Updated grocery list:", groceries)
