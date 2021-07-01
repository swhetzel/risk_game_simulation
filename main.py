# lpa2a@virginia.edu
# an object oriented program to test the risk game simulation
# 2021-06-29

# set up logging
import logging
# logging.basicConfig(level=logging.DEBUG) # to see debugging log message
logging.basicConfig(level=logging.INFO) # to see debugging log message

# imports and parameters
import army
MIN_ARMY_SIZE = 5
MAX_ARMY_SIZE = 50
PRECISION = 1000 # 1000 takes me about 3 minutes to run


# function to assign casualties in a battle
def battle(at,de):
    ''' inputs are the attacker and defender classes, this functions computes casualties, assume max dice are rolled '''
    a = sorted(at.roll())
    d = sorted(de.roll())
    while(len(d)>0 and len(a)>0):
        if d.pop() >= a.pop(): at.lose_division()
        else: de.lose_division()
    logging.debug("RESULT --> Attacker {} v {} Defender".format(at.divisions,de.divisions))


def main():
    ''' main function for simulation, creates army classes for attacker and defender, while loop for conducting battles, outputs result'''
    logging.debug(" <--- Welcome to Risk Simulation! --->")

    armySizes = list(range(MIN_ARMY_SIZE,MAX_ARMY_SIZE+1))
    attackerWinPercentages = []

    for armySize in armySizes: # magic numbers

        attackerWins = 0

        for i in range(PRECISION):

            # create armies
            at = army.Army(attacker=True,divisions=armySize)
            de = army.Army(attacker=False,divisions=armySize)

            # combat loop
            logging.debug(" <---       Mortal Kombat!        --->")
            while(at.divisions>1 and de.divisions>0): battle(at,de)

            # logging results
            if de.divisions<1: 
                logging.debug("<--- RESULT --->Attacker Wins")
                attackerWins+=1
            else: 
                logging.debug("<--- RESULT --->Defender Wins")

        attackerWinPercentages.append(100.*attackerWins/PRECISION)

    print(attackerWinPercentages)



if __name__ == '__main__':
    main()