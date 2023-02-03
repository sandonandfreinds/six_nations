import re
import numpy as np

def odds_fromat(numer, denom):
    prob = (denom)/(numer+denom)
    odds = numer/denom
    return prob, odds

def create_axis(deposit):
    while True:
        yield np.linspace(0,deposit,100)

def create_axes(deposit, numOfBets):
    i = 0
    x = create_axis(deposit)
    axes = []
    while i < numOfBets:
        axes.append(next(x))
        i+=1
    return axes

def create_space(axes):
    xi = [None]*len(axes)
    z = 0
    xi = np.meshgrid(*axes)
    for i in xi:
        z = z+i
    return z

def create_bet_matrix(deposit, numOfBets):
    axis = create_axis(deposit)
    x = next(axis)
    l = create_axes(deposit,numOfBets)
    z = create_space(l)
    matrix = []
    result = np.where(z==deposit)
    for i in range(0,len(result[0])):
        matrix.append([round(x[j[i]],2) for j in result])
    return matrix

def break_even_prob(odds,probs,deposit,bets):
    prob = 0
    k = 0
    returns = [(odds[i]*bets[i]+bets[i]) for i in range(0,len(odds))]
    for i in range(0,len(bets)):
        if returns[i] >= deposit:
            prob = prob + probs[i]
        for j in range(k,len(bets)):
            if i != j and ((returns[i] + returns[j]) >= deposit):
                prob = prob + probs[i]*probs[j]
                k = k+1
    return prob

def look_up_odds_checcker():
    pass