from nonogram import board, playboard, generate_answer_board, generate_answer_counts_with_board
from nonogram import row_counts, column_counts, column_boxes, row_boxes
from nonogram import filler
import pprint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, top = None):
        self.top = Node(top)

    def push(self, num):
        new = Node(num)
        new.next = self.top
        self.top = new

    def pop(self):
        if not self.top:
            return
        elif not self.top.next:
            self.top = None
        else:
            self.top.value = self.top.next.value
            self.top.next = self.top.next.next

    def peek(self):
        return self.top.value

    def __repr__(self):
        lst = []
        current = self.top
        while current:
            lst.extend([current.value,'-->'])
            current = current.next
        lst.append(None)
        return f'{lst}'

def box_is_valid(box_row, box_col, choice, playboard):
    '''

    '''
    if len(correct_playboard) in row_counts(correct_playboard, ____) or len(correct_playboard) in column_counts(board_with_answer_counts, ____)
                # stack.push(count)
                # count += 1
                # place dot 
    elif not sum(row_counts(board_with_answer_counts, ____)) or not sum(column_counts(board_with_answer_counts, ____)):
                # stack.push(count)
                # count += 1
                # do not place dot
    elif row_boxes(correct_playboard, ____).count(filler) == sum(row_counts(board_with_answer_counts, ____)) or column_boxes(correct_playboard, ____).count(filler) == sum(column_counts(correct_playboard, ____)):
                # stack.push(count)
                # count += 1
                # do not place dot
    return  True

def search_algorithm(board_with_answer_counts):
    '''
    
    '''

    # ADD CHECK FOR IF YOURE ON LAST BLOCK
    # ADD CHECK FOR IF STACK.PEEK() BECOMES GREATER THAN 8
    # RECURSIVE CHECK

    stack = Stack(0)

    # starts out empty, algorithm will change this into the correct board
    correct_playboard = [
        [board_with_answer_counts[row][col] for row in range(len(board_with_answer_counts)) 
            if row >= len(board_with_answer_counts)//2] 
                for col in range(len(board_with_answer_counts)) 
                    if col >= len(board_with_answer_counts)//2
                    ]
    
    count = 1
    # It's squared because there are length**2 amount of squares on the board
    squares_on_board = len(correct_playboard)**2

    return correct_playboard


print(search_algorithm(generate_answer_counts_with_board(board, generate_answer_board(playboard))))