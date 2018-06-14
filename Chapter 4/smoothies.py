#Test "for"

# creating a array
smoothies = ['coconut', 'strawberry', 'banana', 'pinaple', 'acai berry']

length = len(smoothies)

for smoothie in smoothies:
    output = 'We serve ' + smoothie
    print(output)

for i in range (length):
    print('Smoothie #', i, smoothies[i])