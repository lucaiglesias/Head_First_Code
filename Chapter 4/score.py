import random
end = ''

#first we need to creat a array (or in python languagem 'list)
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54]

#then, we will use the loop function to keep the code running
while end != 'n':
#Enter the value of solution
    solution = input("Type number of solution ")
    solutionnum = int(solution)
    #If solution do not exist enter in a loop
    while (solutionnum < 0 or solutionnum > 9 ):
        solution = input("Type number of solution ")
        solutionnum = int(solution)
#pick value and look position in array, then print the value in the array
    score = scores[solutionnum]
    print ("Solution #", solutionnum, "produce", score, "bubbles.")
    end = input ("Type another? y/n ")

