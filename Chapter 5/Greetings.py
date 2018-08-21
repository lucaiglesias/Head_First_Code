#it's possible use global variables in functions
greeting = 'Greetings'

def greet(name, message):
    #global greeting #to call the variable not just the value
    greeting
    greeting = 'Hi'#if i change the value without the line abouve it will change just in the function
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)


