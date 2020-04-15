from random import seed
from random import randint
from datetime import datetime

def throw(dice):
    seed(datetime.now())
    roll = []
    for _ in range(dice):
        roll.append(randint(1,6))
    return roll
        
#returns all potential scores and number of dice left. 0 if fail
def calculateScore(dice):
    returnList = [0]
    dicecount = [0,0,0,0,0,0,0]
    Flush = True
    for i in range(len(dice)):
        if dice[i] == 1:
            dice[i] = 0
            bla = list(calculateScore(dice))
            returnList.append(tuple((100+max(bla[0]), 1+bla[1])))
            dice[i] = 1
        if dice[i] == 5:
            dice[i] = 0
            bla = list(calculateScore(dice))
            returnList.append(tuple((50+max(bla[0]), 1+bla[1] )))
            dice[i] = 5
        dicecount[dice[i]] = dicecount[dice[i]]+1
    for i in range(len(dicecount)):
        if dicecount[i] != 1 and i != 0:
            Flush = False
        if dicecount[i] >= 3:
            if i == 0:
                continue
            if i == 1:
                bla = list(calculateScore([0 if x == 1 else x for x in dice]))
                returnList.append(tuple(1000*2**(dicecount[i]-3)+max(bla[0]), dicecount[i]+bla[1]))
            else: 
                list(calculateScore([0 if x == 1 else x for x in dice]))
                returnList.append(tuple((i*100*2**(dicecount[i]-3)+max(bla[0]), dicecount[i]+bla[1])))    
        if Flush == True:
            returnList.append(tuple((2000,6)))
    return returnList


print(throw(50))






