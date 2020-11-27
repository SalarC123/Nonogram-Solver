import pprint

_ = 0

board = [
    [_,_,_,1,0,1],
    [_,_,_,0,1,0],
    [_,_,_,1,0,1],
    [1,0,1,0,0,0],
    [0,1,0,0,0,0],
    [1,0,1,0,0,0]
]

playboard = [
    board[3][3:],
    board[4][3:],
    board[5][3:]
]

def answer_key_board():

    c1_counts = [board[0][3],board[1][3], board[2][3]]
    c2_counts = [board[0][4],board[1][4], board[2][4]]
    c3_counts = [board[0][5],board[1][5], board[2][5]]
    r1_counts = board[3][:3]
    r2_counts = board[4][:3]
    r3_counts = board[5][:3]    

    for count, i in enumerate(c1_counts):
        if i:
            playboard[count][0] = '.'

    for count, i in enumerate(c2_counts):
        if i:
            playboard[count][1] = '.'

    for count, i in enumerate(c3_counts):
        if i:
            playboard[count][2] = '.'

    return playboard

your_board = playboard
answer_board = answer_key_board() 

print(your_board)
print(answer_board)

# while your_board != answer_board:
#     rowguess = int(input('which row has a black box: '))
#     columnguess = int(input('which column has a black box'))
#     if answer_board[rowguess][columnguess] == '.':
#         your_board[rowguess][columnguess] = '.' 
#         print('CORRECT')
#         print(your_board)
#     else:
#         print("WRONG")
#         print(your_board)