# lpa2a@virginia.edu
# an object oriented program to test the risk game simulation
# 2021-06-29

# set up logging
import logging
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG,format=FORMAT)

# imports and parameters
import army
ARMY_SIZE = 10


# function to assign casualties in a battle
def battle(at,de):
    ''' inputs are the attacker and defender classes, this functions computes casualties, assume max dice are rolled '''
    a = sorted(at.roll())
    d = sorted(de.roll())
    while(len(d)>0 and len(a)>0):
        if d.pop() >= a.pop(): at.lose_division()
        else: de.lose_division()
    print("RESULT --> Attacker {} v {} Defender".format(at.divisions,de.divisions))


def main():
    ''' main function for simulation, creates army classes for attacker and defender, while loop for conducting battles, outputs result'''
    print("\n <--- Welcome to Risk Simulation! --->")

    # create armies
    at = army.Army(attacker=True,divisions=ARMY_SIZE)
    de = army.Army(attacker=False,divisions=ARMY_SIZE)

    # combat loop
    print("\n <---       Mortal Kombat!        --->")
    while(at.divisions>1 and de.divisions>0): battle(at,de)

    # print results
    print("\n<--- RESULT --->")
    if de.divisions<1: print("Attacker Wins")
    else: print("Defender Wins")

if __name__ == '__main__':
    main()