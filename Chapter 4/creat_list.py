#creat a lis from scratch

menu = []
menu.append('Burguer')
menu.append('Sushi')

print(menu)

#delete item in list
del menu[0]
print(menu)

#Put together another list with "menu"
menu.extend(['BBQ', 'Tacos'])
print(menu)

#or...
menu = menu +['BBQ', 'Tacos']
print(menu)

#insert item in list in define position
menu.insert(1, 'Stir Fry')
print(menu)