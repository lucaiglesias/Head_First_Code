#Create a function that call the dog's name and weight. Check the weight to see which bark it will take

print('Get thoese dogs ready')

#Creating the function
def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')

#Invoking the fuction
bark('Codie', 40)
bark('Sparky', 9)
bark('Jackson', 12)
bark('Fido', 65)

print ("Okay, we're all done")