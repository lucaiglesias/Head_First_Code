#Test "for"

# creating a array
smoothies = ['coconut', 'strawberry', 'banana', 'pinaple', 'acai berry']
has_coconut = [True, False, False, True, False]


#read size of list
length = len(smoothies)

#Creates the sequence 0,1,2,3,4
#range(5)

#print the item of the list in sequence 
for smoothie in smoothies:
    output = 'We serve ' + smoothie
    print(output)

#print the item of the list selected by the range
for i in range (length):
    print('Smoothie #', i, smoothies[i])

for i in length:
    if has_coconut[i]:
        print(smoothies[i], 'contains coconut')