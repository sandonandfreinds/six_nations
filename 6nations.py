import math 
import numpy as np
import utils

def main():
    deposit = 100

    a = (21,10) #wales to beat ireland
    b = (13,5) #scotland to beat england
    c = (1,40) #FRANCE TO BEAT ITALY
    d = (6,1) #falateau to score try
    e = (4,5) #less than, 46.5 points in scotland england  

    choices = [a,b,c,d,e]
    num_of_bets = len(choices)

    odds = [utils.odds_fromat(i[0],i[1])[1] for i in choices]
    probabilities = [utils.odds_fromat(i[0],i[1])[0] for i in choices]

    best_prob = 0
    bet_matrix = utils.create_bet_matrix(deposit,num_of_bets)
    
    for i in bet_matrix:
        prob = utils.break_even_prob(odds,probabilities,deposit,i)
        if prob > best_prob:
            best_prob = prob
            best_bet = (i,round(best_prob,3))
    print(best_bet)

if __name__=="__main__":
    main()