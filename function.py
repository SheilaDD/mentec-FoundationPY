def add(a, b):
    return a + b


results = add(5, 3)
print(f"The result of addition is: {results}")


def net_salary_calculator(gross_salary, tax_rate):
    return gross_salary - (gross_salary * tax_rate)


net_salary = net_salary_calculator(5000, 0.15)
print(f"The net salary is: {net_salary}")


def habit_tracker(task, time):
    for i in range(time):
        print(f"Tracking habit: {task} for {i + 1} day(s)")


task = input("Enter the habit you want to track: ")
repeats = int(input("Enter the number of days to track the habit: "))
habit_tracker(task, repeats)


def calculate_savings(income, expenses):
    return income - expenses


income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

savings = calculate_savings(income, expenses)
print(f"Your monthly savings are: {savings}")

budget = float(input("How much are you earning per month? "))
expenses = float(input("How much are you spending per month? "))


def add(a, b):
    return a - b


my_savings = add(budget, expenses)
print(f"Your savings for the month are: {my_savings}")
if my_savings >= 0:
    print("You are saving money!")
else:
    print("You are overspending!")
