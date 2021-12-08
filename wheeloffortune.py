#def hello(): #group code that gets executed multiple times
    #print('Howdy!')
    #print('Howdy!!')
    #print('Howdy!!!')

#hello()
#hello()
#hello()

#def hello(name):
#    print('Hello, ' + name)

#hello('Alice')
#hello('Bob')

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decided'
    elif answerNumber == 3:
        return 'Reply hazy. Try again'
    elif answerNumber == 4:
        return 'Ask again later'
    elif answerNumber == 5:
        return 'My reply is no'
    elif answerNumber == 6:
        return 'Outlook not so good'
    elif answerNumber == 7:
        return 'Doubtful'
    elif answerNumber == 8:
        return 'Press 9 for secret message'
    else:
        return 'joe mama'
r = int(input("Pick a number from 1 to 7. If you guess right, you'll get an answer: ")) 
"""if it comes to the number 7, reroll 1 to 7
    r = random.randint(1,7)

"""
# def reroll(roll):
#     if(r == 7):
#         print('We have to reroll')
#         return(roll)
# roll = r
# print(roll)
#attempt at making code

