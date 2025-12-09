bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#can use .title for capitilzation of list item
#using -1 always gives the last item in a list (bicycles[-1])
print(bicycles[2])
print(bicycles[-1])

#using individual values from a list
message = f"My first bicycle was a {bicycles[1].title()}"
print(message)

#modifying lists 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#append lists 
motorcycles.append('ducati')
print(motorcycles)

#you can append a blank list to fill it wth list elements 

#can insert elements into list
motorcycles.insert(0, 'kawasaki')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

#using the .pop method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'The first motorcyle I owned was a {first_owned.title()}')
print(motorcycles)

#can use motorcycles.remove('ducati') to remove an item from a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
