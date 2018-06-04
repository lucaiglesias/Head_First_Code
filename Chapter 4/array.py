#Working with arrays in Python (or lists)

#creating a array
smoothies = ['coconut', 'strawberry', 'banana', 'pinaple', 'acai berry']

#acess a list item
favorite = smoothies[2]
print ("My favorite flavor is", favorite)

#updating a value in the list
smoothies[3] = 'tropical'
print ("We're having the flavors", smoothies)

#size of the list
lenght = len(smoothies)
print ("We have", lenght, "flavors")

#choosing the last on in the list
last = smoothies[lenght-1]
print (last)

#using python's negative indices
last = smoothies[-1]
second_last = smoothies[-2]
third_last = smoothies[-3]
print (last)
print (second_last)
print (third_last)



