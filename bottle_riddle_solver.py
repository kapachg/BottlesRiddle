# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:04:08 2018

@author: GuyKa
"""

import itertools

number_of_truths = {2:1,1:1,0:1}    # key = number of true statements, value = number of corresponding bottles
bottles = {
            1 : ('not 1','is 2'),
            2 : ('not 1','is 3'),
            3 : ('not 3','is 1')
}

"""   More complexisity
number_of_truths = {2:2,1:2,0:1}    
bottles = { 
            1: ('not 3','not 2'), 
            2: ('is 1','not 1') , 
            3: ('not 1', 'is 4'),
            4: ('not 5','is 4'),
            5: ('not 2','is 1')      
}
"""

allegedly = 0
cannot_be = []

def phrase(text,rule):
    n = 'not'
    i = 'is'

    arg = [0,0]
    op = [0,0]

    global cannot_be
    global allegedly
    cant_be = cannot_be
    
    if (rule == 0) : 
        (n,i) = (i,n)    
    
    for s in range(2):
        arg[s] = int(text[s].split()[1])
        op[s] = text[s].split()[0]
    
    ans = False
    for mode in range(2):    
        if (rule == 1 and mode == 0): op[1] = 'not' if op[1] == 'is' else 'is'        
        if (rule == 1 and mode == 1): (n,i) = (i,n)
        for s in range(2):

            if (op[s] == i):
                if (op[s-1] == i and arg[1] != arg[0]):
                    ans=False
                    break
                if (not allegedly):     
                    allegedly = arg[s]
                    ans=True
                if (allegedly != arg[s]):
                    ans=False
                    break
                else:
                    ans=True
            if (op[s] == n):            
                if (rule == 1): cant_be.append(arg[s])
                else: cannot_be.append(arg[s])
                ans=True
        else:
            if allegedly in cant_be:
                ans=False
            elif allegedly in cannot_be:
                ans=False
            else:
                cannot_be = cant_be
                return ans
    return ans 

def phrase_rules():
    rule = []
    for i in range(number_of_truths[2]):
        rule.append(2)    
    for i in range(number_of_truths[0]):
        rule.append(0)    
    for i in range(number_of_truths[1]):
        rule.append(1)
    return tuple(rule)           
        
def assign_bottles():         
    global cannot_be
    global allegedly
    rules = phrase_rules();
    sequences = itertools.permutations(bottles.keys())
     
    for sequence in sequences:

        allegedly = 0
        cannot_be = []

        for bottle,rule in zip(sequence,rules):
             if not phrase(bottles[bottle],rule) : break
        else:                          
            ans = {}
            for i in range(1,1+len(sequence)):
                ans[i] = (f'{bottles[i]}, number of truths = {rules[sequence.index(i)]}')
            return (allegedly,sequence,rules,ans)

        
z = assign_bottles()
print(f'The correct answer is {z[0]}.')
print(f'Detailed list of bottles is {z[-1]}.')
print(f'The sequence {z[1]} matches the rulling {z[2]}')
