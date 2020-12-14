import pprint
import random
import copy

_ = 0        
filler = 'X'

board = [                                                           
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [_,_,_,_,_,_,_,_,_,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

# creates a board with only the area where you enter answers
playboard = [
    [board[row][col] for row in range(len(board)) 
        if row >= len(board)//2] 
            for col in range(len(board)) 
                if col >= len(board)//2
]



def generate_answer_board(playboard):                                
    '''
    Generates random board and returns the 
    "play" area with the answers filled in
    '''
    newplayboard = copy.deepcopy(playboard)

    for row in range(len(newplayboard)):
        for col in range(len(newplayboard)):
            if random.choice([True,False]):
                newplayboard[row][col] = filler                       
    
    return newplayboard


def generate_answer_counts_with_board(board, answer_board):
    '''
    Creates "counts" based on the answer key board
    and returns an entire board with an empty play area. 
    Only the "counts" are labeled in here
    '''
    boardcopy = copy.deepcopy(board)

    # ROW counts
    for row in range(len(answer_board)):
        in_a_row = 0
        for count, col in enumerate(answer_board[row]):
            if col == filler:                                                 
                in_a_row += 1
                # if you reach the end of the row
                if count ==  len(answer_board) - 1:
                    boardcopy[len(answer_board)+row][count] = in_a_row
            else:
                boardcopy[len(answer_board)+row][count] = in_a_row
                in_a_row = 0
            

    #COLUMN counts
    for row in range(len(answer_board)):
        in_a_row = 0
        for count, j in enumerate(answer_board):
            if j[row] == filler:                                              
                in_a_row += 1
                # if you reach the end of the column
                if count == len(answer_board) - 1:
                    boardcopy[count][len(answer_board) + row] = in_a_row
            else:
                boardcopy[count][len(answer_board) + row] = in_a_row
                in_a_row = 0
        
    return boardcopy


def row_counts(board, row):
    '''
    returns a list of the numbers 
    that describe the row provided
    '''
    playboard_length = len(board) // 2
    return [board[playboard_length + row][i] for i in range(playboard_length) if board[playboard_length + row][i]]


def column_counts(board, column):
    '''
    returns a list of the numbers 
    that describe the column provided
    '''
    playboard_length = len(board) // 2
    return [board[i][playboard_length + column] for i in range(playboard_length) if board[i][playboard_length + column]]


def row_boxes(playboard, row):
    '''
    returns a list of the values in the 
    other boxes in the row provided
    '''
    return playboard[row]


def column_boxes(playboard, column):
    '''
    returns a list of the values in the 
    other boxes in the column provided
    '''
    playboard_length = len(playboard)
    return [playboard[i][column] for i in range(playboard_length)]


def play():
    '''
    Generates random board for testing in the terminal
    '''
    answer_board = generate_answer_board(playboard) 
    your_board = generate_answer_counts_with_board(board, answer_board)
    your_board_play_area = [[your_board[row][col] for row in range(len(your_board)) if row >= len(your_board)//2] for col in range(len(your_board)) if col >= len(your_board)//2]
    
    while your_board_play_area != answer_board:
        pprint.pprint(your_board)
        rowguess = int(input('which row has a black box: '))
        columnguess = int(input('which column has a black box: '))
        if answer_board[rowguess][columnguess] == filler:                        
            your_board[rowguess + len(answer_board)][columnguess + len(answer_board)] = filler
            your_board_play_area[rowguess][columnguess] = filler
            print('CORRECT')
        else:
            print("WRONG")
    print('YOU WON')

if __name__ == '__main__':
    play()