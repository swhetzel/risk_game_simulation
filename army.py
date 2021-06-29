# class definition for army
# object oriented approach
# lpa2a@virginia.edu

import numpy as np

class Army():

    def lose_division(self):
        ''' this function inflicts a casualty on an army'''
        self.divisions -= 1

    def roll(self):
        ''' this functions makes the rolls for an army, assumes the maximum number of dice are rolled, returns an array'''

        # determine number to roll
        if self.attacker:
            if self.divisions >=4: n = 3
            elif self.divisions >=3: n = 2 
            elif self.divisions >=2: n = 1
            else: self.__del__()
        else:
            if self.divisions >=2: n=2
            elif self.divisions >=1: n=1
            else: self.__del__()

        return(np.random.randint(7,size=n))

    def __init__(self,attacker=True,divisions=10):
        ''' initialization of army, sets attacker status and initial number of divisions'''
        self.divisions = divisions   # number of divisions in the army
        self.attacker = attacker     # True for attacker, False for defender
        print("  ---> Army created: id = {}, size = {}, attacker = {}.".format(self,self.divisions,self.attacker))