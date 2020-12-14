import pygame
import copy
import random
import time
import pprint
from command_line_nonogram.nonogram import generate_answer_counts_with_board, generate_answer_board
from command_line_nonogram.nonogram import board, playboard, filler
from command_line_nonogram.nonogram import row_counts, column_counts

def game():
    '''
    DESCRIPTION OF GAME 
    '''
    # Initializations of variables used within the mainloop
    pygame.init()

    black = (0,0,0)
    white = (255,255,255)
    custom_box_color = (123,123,200)
    custom_cross_color = (50,150,215)

    width, height = (1000,1000)
    board_width, board_height = (830, 660)
    board_start_x = width - board_width
    board_start_y = height - board_height

    # mouse clicks are assigned to different numbers in pygame
    left = 1
    right = 3

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Nonogram')
    clock = pygame.time.Clock()
    screen.fill(white)

    background_surface = pygame.image.load('images/sudokuboard.jpg').convert()
    background_surface = pygame.transform.scale(background_surface, (board_width,board_height))
    title_font = pygame.font.SysFont('Corbel',int(width / 5))
    num_font = pygame.font.SysFont('Arial', 30)
    cross_font = pygame.font.SysFont('Arial', 100)
    title_text = title_font.render('NONOGRAM',True, black)
    instructions_text = num_font.render('Right click to place an "X"          Press SPACE to reveal the answer', True, black)

    answer_board = generate_answer_board(playboard)
    empty_with_answer_counts = generate_answer_counts_with_board(board, answer_board)


    def draw_square(dimensions, color):
        pygame.draw.rect(background_surface, color, dimensions)

    def draw_cross(dimensions, boxlength, color):
        x = dimensions[0]
        y = dimensions[1]
        draw_square(dimensions, white)

        cross = cross_font.render('X', True, color)
        # added int(boxlength)//6 to center the cross
        background_surface.blit(cross, (x + int(boxlength//6),y))

    def change_model_board(playboard, clicked_row, clicked_column, currentcolor):
        '''

        '''
        if currentcolor == custom_box_color:
            playboard[clicked_column][clicked_row] = filler
        else:
            playboard[clicked_column][clicked_row] = 0

    def solve(answer_board, boxlength, boxheight):
        '''
        If you press space, the board 
        will be filled in automatically
        '''
        pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN, pygame.K_SPACE])
        for first_count, row in enumerate(answer_board):
            for second_count, col in enumerate(row):
                x = boxlength * second_count + 5
                y = boxheight * first_count + 5
                box_dimensions = (x, y, boxlength - 5, boxheight - 5)
                if col:
                    draw_square(box_dimensions, custom_box_color)
                else:
                    draw_cross(box_dimensions, boxlength, custom_cross_color)
        
    while True:
        # blit parameters: surface that should be put on screen, where to put it
        screen.blit(background_surface, (board_start_x, board_start_y))
        screen.blit(title_text, (int(width/15),int(height/25)))
        screen.blit(instructions_text, (int(width/15), int(height/6)))

        # placing row counts 
        for i in range(len(playboard)):
            for count, j in enumerate(row_counts(empty_with_answer_counts, i)[::-1]):
                text_surface = num_font.render(str(j), False, black)
                screen.blit(text_surface, (board_start_x - (30*count) - 20, board_start_y + (board_height//9 * i) + 30))

        # placing column counts
        for i in range(len(playboard)):
            for count, j in enumerate(column_counts(empty_with_answer_counts, i)[::-1]):
                text_surface = num_font.render(str(j), False, black)
                screen.blit(text_surface, (board_start_x + (board_width//9 * i) + 30,board_start_y - (30*count) - 20))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(answer_board, board_width//9, board_height//9)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                box_length = board_width // 9
                box_height = board_height // 9

                clicked_row = int((mouseX - board_start_x) // box_length)
                clicked_column = int((mouseY - board_start_y) // box_height)

                # added 5 pixels so that the box doesn't overlap the inner lines
                x = box_length * clicked_row + 5
                y = box_height * clicked_column + 5
                clicked_box_dimensions = (x, y, box_length - 5, box_height - 5)

                # Skips the click if it is outside the board
                if clicked_row < 0 or clicked_column < 0:
                    continue
                
                # adds black square on white box and vice versa
                if event.button == left:
                    if screen.get_at(event.pos) == white:
                        draw_square(clicked_box_dimensions, custom_box_color)
                        change_model_board(playboard, clicked_row, clicked_column, custom_box_color)
                    else:
                        draw_square(clicked_box_dimensions, white)
                        change_model_board(playboard, clicked_row, clicked_column, white)
                elif event.button == right:
                    draw_cross(clicked_box_dimensions, box_length, custom_cross_color)
                    change_model_board(playboard, clicked_row, clicked_column, white)

            if playboard == answer_board:
                wintext = title_font.render('YOU WIN!!!', True, (70,100,255))
                background_surface.blit(wintext, (10,10))
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)

        clock.tick(20)
        pygame.display.update()

if __name__ == '__main__':
    game()