#creating a new function to make a bunch of different questions and take all the answers
def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question) #get the answer of the question
    #if the user hits return with no answer it takes the default answer
    if(answer == ''):
        answer = default 
    print('You chose', answer)
    

hair = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')