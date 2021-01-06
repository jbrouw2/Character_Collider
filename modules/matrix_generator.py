"""

Generates character matrix 

Uses parameters to create matrix M for export

"""

#import sys
import random
from modules.domain_variables import domain_names

#num_arguments = len(sys.argv)
#if num_arguments != 7:
#    print('Please run script with 7 numbers...')
#    print('1: Number of TOTAL characters')
#    print('Number of characters HIGH in the following traits:')
#    print('\t2: Honesty-Humility', '\t3: Emotionality', '\t4: eXtraversion', '\t5: Agreeableness', '\t6: Conscientiousness', '\t7: Openness', sep='\n')
#
#NUM_CHARACTERS = int(sys.argv[0])
#HIGH_SCALES = [int(arg) for arg in sys.argv[1:]]

# Force HIGH_SCALES values n to be 0 <= n <= NUM_CHARACTERS
def checkHighScales(HIGH_SCALES, NUM_CHARACTERS):
    for i, n in enumerate(HIGH_SCALES):
        if n < 0:
            HIGH_SCALES[i] = 0
        if n > NUM_CHARACTERS:
            HIGH_SCALES[i] = NUM_CHARACTERS

# Set `N` cells to 1 in column `col` of matrix M
def nHighRand(M, col, NUM_HIGH):
    row_max = len(M)
    row_index_list = [i for i in range(row_max)]
    row_index_sample = random.sample(row_index_list, NUM_HIGH)
    for row in row_index_sample:
        M[row][col] = 1


def createCharacterMatrix(NUM_CHARACTERS, HIGH_SCALES):
    checkHighScales(HIGH_SCALES, NUM_CHARACTERS)
    M = [[0,0,0,0,0,0] for n in range(NUM_CHARACTERS)]
    for col_idx, NUM_HIGH in enumerate(HIGH_SCALES):
        nHighRand(M, col_idx, NUM_HIGH)
    return M

def inputCharacterMatrix():
    NUM_CHARACTERS = 0
    HIGH_SCALES = [-1 for i in range(6)]
    while NUM_CHARACTERS < 2 or NUM_CHARACTERS > 10: 
        NUM_CHARACTERS = int(input("Enter the number of characters you want (2-10): "))
    print("For each personality domain, enter the number of characters you want to be HIGH in that domain")
    print("Your value must be between 0 and {}".format(NUM_CHARACTERS))
    for i in range(6):
        while HIGH_SCALES[i] < 0 or HIGH_SCALES[i] > NUM_CHARACTERS:
            HIGH_SCALES[i] = int(input("{}: ".format(domain_names[i])))
    print('')
    return NUM_CHARACTERS, HIGH_SCALES