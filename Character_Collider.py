"""

Creates markdown file of character personalities based on script arguments

"""

import sys
from modules.domain_variables import domains, domain_names
from modules.matrix_generator import createCharacterMatrix, inputCharacterMatrix


arguments = sys.argv[1:]
if len(arguments) == 0:
    FILE_NAME = "{}.md".format(str(input("Enter the output file name: ")))
    NUM_CHARACTERS, HIGH_SCALES = inputCharacterMatrix()
elif len(arguments) == 8:
    FILE_NAME = "{}.md".format(arguments[0])
    NUM_CHARACTERS = int(arguments[1])
    HIGH_SCALES = [int(arg) for arg in arguments[2:]]
else:
    print('Please run script with a file name and 7 numbers...')
    print('\t1: Number of TOTAL characters')
    print('Number of characters HIGH in the following traits:')
    print('\t2: Honesty-Humility', '\t3: Emotionality', '\t4: eXtraversion', '\t5: Agreeableness', '\t6: Conscientiousness', '\t7: Openness', sep='\n')
    exit()

explainString = """
- **H** - Honesty-Humility
- **E** - Emotionality
- **X** - eXtroversion
- **A** - Agreeableness
- **C** - Conscientiousness
- **O** - Openness to Experience

*Rows are characters ... Columns are personality domains.* 

*Cells mark that row's character being **high** (X) or **low** (-) in that column's personality domain*"""[1:]

tableHeader = """
|   | H | E | X | A | C | O |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|"""[1:]

def arrayToRow(array):
    rowString = "|"
    symbol = {0: " - |", 1: " x |"}
    for x in array:
        rowString += symbol[x]
    return rowString

def printMatrix(print_file, matrix):
    print("# Character Collider", file = print_file, end = "\n\n")
    print("---", file = print_file, end = "\n\n")
    print(explainString, file = print_file, end = "\n\n")
    print(tableHeader, file = print_file)
    for i, array in enumerate(matrix):
        index = "| **{}** ".format(i+1)
        print(index + arrayToRow(array), file = print_file)
    print(file = print_file)
    


NUMBER_TO_WORD = {1:'ONE', 2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6:'SIX', 7:'SEVEN', 8:'EIGHT'}

def printCharacterDomain(print_file, val, domain_idx):
    i = domain_idx
    print("## " + domain_names[i], file = print_file, end = "\n\n")
    for facet in domains[i]:
        print("#### " + facet.name, file = print_file, end = "\n\n")
        print(facet.scale[val], file = print_file, end = "\n\n")

def printCharacter(print_file, matrix, character_idx):
    NUM = NUMBER_TO_WORD[1 + character_idx]
    print("---", file = print_file, end = "\n\n")
    print("# Character", NUM, file = print_file, end = "\n\n")
    for i, domain_value in enumerate(matrix[character_idx]):
        printCharacterDomain(print_file, domain_value, i)

def printCast(print_file, matrix):
    for i in range(len(matrix)):
        printCharacter(print_file, matrix, i)


with open(FILE_NAME, "w") as print_file:
    matrix = createCharacterMatrix(NUM_CHARACTERS, HIGH_SCALES)
    printMatrix(print_file, matrix)
    printCast(print_file, matrix)
    print("Awesome!")
    print("{} is your Character Collision file".format(FILE_NAME))
    print("You can convert it to PDF at: www.markdowntopdf.com/")
