import random
end = ''

#first we need to creat a array (or in python languagem list)
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54]

#then, we will use the loop function to keep the code running
while end != 'n':
    solution = 10
#Enter the value of solution, if solution do not exist keep in loop
    while (solution< 0 or solution > 9 ):
        solution = int(input("Type number of solution "))

#pick value and look position in array, then print the value in the array
    score = scores[solution]
    print ("Solution #", solution, "produce", score, "bubbles.")
    end = input ("Another solution? y/n ")

