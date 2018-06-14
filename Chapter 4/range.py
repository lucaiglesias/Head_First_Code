#How to work with range

#create the sequence 0,1,2,3,4
print(list(range(5)))

#creates a sequence starting at 5 and going up to 10, so 5,6,7,8,9
print(list(range(5, 10)))

#Creates a sequence starting at 3 and going up to 10, but counting by step 2. 3, 5, 7, 9
print(list(range(0, 8, 2)))

#creates a sequence starting at 10 and goind down to 0 but by steps of -1. 10,9,8,7,6,5,4,3,2,1
print(list(range(10, 0, -1)))

#creates a sequence starting at -10 counting to 2. -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1
print(list(range(-10, 2)))