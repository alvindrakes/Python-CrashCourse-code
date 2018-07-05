# 7.8 deli

sandwich_orders = ['chicken', 'tuna', 'mayo', 'eggs']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I have made " + current_sandwich )

    finished_sandwich.append(current_sandwich)

print("\nAll the sandwiches that I have made are: ")
for sandwich in finished_sandwich:
    print(sandwich)