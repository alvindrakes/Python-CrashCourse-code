# 7.9 No pastrami


sandwich_orders = ['chicken', 'pastrami', 'tuna', 'mayo', 'pastrami', 'eggs', 'pastrami']
finished_sandwich = []

print("I AM SORRY TO ANNOUNCE THAT WE HAVE RAN OUT OF PASTRAMI\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I have made " + current_sandwich )

    finished_sandwich.append(current_sandwich)

print("\nAll the sandwiches that I have made are: ")
for sandwich in finished_sandwich:
    print(sandwich)