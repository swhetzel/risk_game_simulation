# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:56:05 2021

@author: whetz
"""
import numpy as np
import pandas as pd

# Dice rolling simulator for offense and defense
def get_die_roll(side, armies):
    """returns a set of dice results for a given side"""
    dice = 0
    
    if side == "attacker":
        if armies > 2:
            dice = 3
        else:
            dice = armies
    elif side == "defender":
        if armies > 1:
            dice = 2
        else:
            dice = armies
    results = []
    results = np.random.randint(1,7,dice).tolist()
    results.sort(reverse=True)
    return results


def compare_results(att_results, def_results):
    """Compares attacker and defender results. Returns a list of bools, True for each attacker win, False for each defender win."""
    return [a > d for a, d in zip(att_results, def_results)]

# subtract from either attacker or defender
def battle_results(n):
    """Returns the simulated result of an entire battle between equal armies"""
    att_armies = n
    def_armies = n
    while att_armies > 0 and def_armies > 0:
        att_results = get_die_roll("attacker", att_armies)
        def_results = get_die_roll("defender", def_armies)
        results = compare_results(att_results, def_results)
        
        for val in results:
            if att_armies == 0 or def_armies == 0:
                break
            if val:
                def_armies -= 1
            else:
                att_armies -= 1
    
        flag = False
        if flag:
            print("Attacker rolls: ", att_results)
            print("Defender rolls: ", def_results)
            print("Attacker armies: ", att_armies)
            print("Defender Armies: ", def_armies)
            print("")
            
        result = ''

        if att_armies == 0 or def_armies == 0:
            if att_armies == 0:
                result = "Defender Wins"            
            if def_armies == 0:
                result = "Attacker Wins"
            if flag:
                print(result+ '\n\n')
            return result

# Iterate and plot
iterations = 1000
results_dict = {}

for n in range(5,51):
    result_counts = [0,0]
    
    for i in range(iterations+1):
        result = battle_results(n)
        if result == "Attacker Wins":
            result_counts[0] += 1
        elif result == "Defender Wins":
            result_counts[1] += 1
    
    results_dict[n] = result_counts

# print(results_dict)    

attacker_wins = []
armies_list = []
for key, value in results_dict.items():
    attacker_wins.append(value[0]/iterations)
    armies_list.append(key)
# print(armies_list)
# print(attacker_wins)

df = pd.DataFrame({'armies':armies_list, "attacker win prob":attacker_wins})
df.plot.bar(x='armies',y='attacker win prob')
