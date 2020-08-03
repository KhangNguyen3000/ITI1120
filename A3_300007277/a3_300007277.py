import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    print("Shuffling the deck...")
    deck = random.shuffle(deck)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print()


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    for i in range(75):
            print("")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    for i in range(len(original_board)):
        if i == p1 or i == p2:
            print('{0:4}'.format(original_board[i]), end=' ')
        else:
            print('{0:4}'.format(discovered[i]), end=' ')
    print()
    for i in range(len(board)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print()

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    for i in (set(l)):
        if l.count(i) <= 1 or i == "*":
            None
        else:
            c = (l.count(i)//2)*2
            playable_board = playable_board + [i]*c
    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    for i in (set(l)):
        if l.count(i) > 2:
            return False
    return True
           
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")
    d = ["*"]*len(board)
    done = False
    a = 0
    while done == False:
        b = False
        print_board(d)
        print("Enter the two distinct positions on the board that you want revealed \ni.e two integers in the range [1, "+str(len(board))+"]")
        p1 = int(input("Enter position 1: "))-1
        p2 = int(input("Enter position 2: "))-1
        if d[p1] != "*" or d[p2] != "*":
            print("One or both of yout chosen positions have already been paired")
            b = True
        if p1 == p2:
            print("You chose the same positions")
            b = True

        if b == True:
            print("Please try again. This guess did not count. Your current number of guesses is "+str(a)+".")
        else:
            a = a+1
            print_revealed(d,p1,p2,board)
            if board[p1] == board[p2]:
                d[p1] = board[p1]
                d[p2] = board[p2]
            wait_for_player()
        print()
        g = 0
        for i in range(len(d)):
            if d[i] == "*":
                g = g+1
        if g == 0:
            print("Congratulations! You completed the game with "+str(a)+" guesses. That is "+str(a-(len(board)//2))+" more than the best possible.")
            done = True
            



def ascii_maker(s):
    '''
(None) -> None
Makes an ascii
'''
    length = len("*  __"+s+"__  *")
    print("*"*length+"\n*"+(" "*(length - 2))+"*"+"\n*  __"+s+"__  *\n*"+\
          (" "*(length - 2))+"*\n"+"*"*length)
    print('')

#main
ascii_maker("Welcome to my Concentration game")
c = False
status=input("Would you like (enter 1 or 2 to indicate your choice):\n(1) me to generate a rigorous deck of cards for you\n(2) or, would you like me to read a deck from a file?\n")

while c == False:
    
    if status == "1":
        c = True
        c2 = False
        print("You chose to have a rigorous deck generated for you")
        while c2 == False:
            size  = int(input("How many cards do you want to play with? \nEnter an even number between 0 and 52: "))
            if (size%2) == 0 and size >= 0 and size <=52:
                c2 = True
                board=create_board(size)
                shuffle_deck(board)
                wait_for_player()
                if size != 0:
                    play_game(board)
                else:
                    print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye")

    elif status == "2":
        c = True
        print("You chose to load a deck of cards from a file")
        file=input("Enter the name of the file: ")
        file=file.strip()
        board=read_raw_board(file)
        board=clean_up_board(board)
        t = is_rigorous(board)
        if t == True:
            ascii_maker("This deck is now playable, is rigorous and it has "+str(len(board))+" cards.")
        else:
            ascii_maker("This deck is now playable but is not rigorous and it has "+str(len(board))+" cards.")
        wait_for_player()
        shuffle_deck(board)
        wait_for_player()
        if len(board) != 0:
            play_game(board)
        else:
            print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye")
    else:
       status = input(status+" is not existing option. Please try again. Enter 1 or 2 to indicate your choice\n")
