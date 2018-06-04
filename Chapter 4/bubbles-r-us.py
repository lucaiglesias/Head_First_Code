# Set the array (or list)
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

# create a variable to keep track of the current index, which we'll start at 0
i = 0

# get the length of the scores list
length = len(scores)

# loop over the itens while our index is less than the length of the list
# after the operation it print the solution, i represent our solution
# and is also used to mark the position. At the and it increment 1 to
# i and return to the beginning of the loop.
while i < length:
    print('Bubble solution #', i, 'score:', scores[i])
    i = i + 1
