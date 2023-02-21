import random
import string

def search_word(puzzle, word):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == word[0]:
                # check horizontally
                if ''.join(puzzle[i][j:j+len(word)]) == word:
                    return True
                # check vertically
                if ''.join([puzzle[k][j] for k in range(i, i+len(word))]) == word:
                    return True
    return False


def generate_puzzle():
    n=9
    puzzle = []
    for j in range(n):
        row = []
        for i in range(n):
            letter = random.choice(string.ascii_uppercase)
            row.append(letter)
        puzzle.append(row)
    return puzzle

def printing_puzzle(puzzle):
    for i in range(9):
     for j in range(9):
         print(puzzle[i][j], end=' ')
     print()
puzzle=generate_puzzle()
printing_puzzle(puzzle)
word=input('Enter the word you want to find: ')
if search_word(puzzle,word)==True:
    print('The word is present in the puzzle!')
else:
    print('The word is not present in the puzzle')
