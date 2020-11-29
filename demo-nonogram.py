import pprint
import random
import copy

_ = 0                     #TODO #FIXME use something else

board = [                       #TODO FIXME 9x9
    [_,_,_,0,0,0],
    [_,_,_,0,0,0],
    [_,_,_,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

# creates a board with only the area where you enter answers
playboard = [[board[row][col] for row in range(len(board)) if row >= len(board)//2] for col in range(len(board)) if col >= len(board)//2]



def generate_answer_board():
    '''
    
    '''
    newplayboard = copy.deepcopy(playboard)

    for row in range(len(newplayboard)):
        for col in range(len(newplayboard)):
            if random.choice([True,False]):
                newplayboard[row][col] = '.'        # TODO FIXME Use something else
    
    return newplayboard



def generate_answer_counts_with_board(answer_board):
    '''
    
    '''
    boardcopy = copy.deepcopy(board)

    # ROW counts
    for row in range(len(answer_board)):
        in_a_row = 0
        for count, col in enumerate(answer_board[row]):
            if col:
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
            if j[row]:
                in_a_row += 1
                # if you reach the end of the column
                if count == len(answer_board) - 1:
                    boardcopy[count][len(answer_board) + row] = in_a_row
            else:
                boardcopy[count][len(answer_board) + row] = in_a_row
                in_a_row = 0
        
    return boardcopy



def play():
    '''
    
    '''
    answer_board = generate_answer_board() 
    your_board = generate_answer_counts_with_board(answer_board)
    
    while your_board != answer_board:
        rowguess = int(input('which row has a black box: '))
        columnguess = int(input('which column has a black box: '))
        if answer_board[rowguess][columnguess] == '.':                # TODO FIXME Use something else
            your_board[rowguess][columnguess] = '.'                   # TODO FIXME Use something else
            print('CORRECT')
            print(your_board)
        else:
            print("WRONG")
            print(your_board)
    print('FINISHED')




# ans = generate_answer_board()
# pprint.pprint(ans, width = 25)
# pprint.pprint(generate_answer_counts(ans))