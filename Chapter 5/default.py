#it's possible to create functions with default values if it not put by the user.

#always list your required parameters first to not miss it.
def greet (name, emoticon, message='You rule!'):
    print ('Hi', name+'.', message, emoticon)

#This is not gonna work because it miss the second parameter
#greet('John')

#This is gonna work because the third parameter has a default value
greet('Jennifer', 'How are you today?')

#It's possible to use arguments with keywords, it don't need to worry about the order this time
greet(message='Where have you been?', name='Jill', emoticon=':)')

#It's possible mix positional and keywords arguments
greet('Betty', message = 'Yo!', emoticon=':)')