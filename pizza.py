pizzas = ['Meat Lovers', 'Buffalo chicken', 'Pepperoni and Sausage']

for pizza in pizzas:
    print(f"{pizza.title()} is a good pizza")
print("\n Pizza is so delicious.")


my_pizza = ['Meat Lovers', 'Buffalo chicken', 'Pepperoni and Sausage']
friend_pizza = my_pizza [:]

my_pizza.append('Chicken Bacon Ranch')
friend_pizza.append('Hawaiian')

print("My favorite pizzas are: ")
for pizza in my_pizza:
    print(pizza)

print("My friends favorite pizzas are: ")
for fpizza in friend_pizza: 
    print(fpizza)