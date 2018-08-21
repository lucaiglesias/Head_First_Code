#it's possible use global variables in functions
greeting = 'Greetings'

def greet(name, message):
    #global greeting #to call the variable not just the value
    greeting#if i put this line here whitout the line abouve it will create a error 'UnboundLocalError' that means python don't understand if this is a local or a global variable
    greeting = 'Hi'#if i change the value without the line "global -name of variable-" it will change just in the function
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)


