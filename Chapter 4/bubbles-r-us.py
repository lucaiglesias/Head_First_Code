# Set the array (or list)
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25, 
         .25, .25, .27, .25, .26, .29]

# create a variable to keep track of the current index, which we'll start at 0
#i = 0
high_score = 0

# get the length of the scores list
length = len(scores)

# loop over the itens while our index is less than the length of the list
# after the operation it print the solution, i represent our solution
# and is also used to mark the position. At the and it increment 1 to
# i and return to the beginning of the loop.
#while i < length:

for i in range(length):
    #print all the solutions and scores
    print('Bubble solution #'+ str(i), 'score:', scores[i])
    #select the highest score
    if scores[i]>high_score:
        high_score = scores[i]

print('Bubbles tests:', length)
print('Highest bubble score:', high_score)

#check which solutions has the highest score and put in a list
best_solutions=[]
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)
print('Solutions with the highest score:', best_solutions)

#Compare the lowest cost of product with the highest score product and separete the product with lowest cost and highest score
#cost = 100.0
#most_effective = 0
# for i  in range(length):
#     if scores[i] == high_score and costs[i] < cost:
#         most_effective = i
#         cost = costs[i]
# print('Solution', most_effective,
#       'is the most effective with a cost of', costs[most_effective])   

#most efficiency way
cost = 100.0
most_effective = 0
len_best = len(best_solutions)
for i in range(len_best):
    index = best_solutions[i]
    if cost>costs[index]:
        most_effective = index
        cost = costs[index]
print('Solution', most_effective,
      'is the most effective with a cost of', costs[most_effective])  