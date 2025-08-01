groceries = ["apples", "juice", "milk", "dates", "eggs", "bread"]
groceries = ["apples_200g_R12", "juice_1L_R23", "milk_", "dates_20g_R6", "eggs_18pack_R32", "bread_100g_13"]
groceries.sort()

def calculate_total(groceries):
    total = 0
    for item in groceries:
       price = float(item.split("-R")[1])
    total += price 
    return total

total = calculate_total(groceries)
print(f"Total cost of groceries: ", len(groceries))
print("groceries list:", groceries)
if total > 500:
    print("Total price: R", total)
else:
    print("Total price: R", total )

