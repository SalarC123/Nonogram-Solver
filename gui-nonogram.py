# Make classes later                                        TODO
'''https://www.youtube.com/watch?v=yniQ15A7MLk'''          #TODO

import pygame
import random
from command_line_nonogram.nonogram import generate_answer_counts_with_board, generate_answer_board
from command_line_nonogram.nonogram import board, playboard, filler

def game():
    '''
    DESCRIPTION OF GAME 
    '''
    # Initializations of variables used within the mainloop
    pygame.init()

    width, height = (1000,1000)
    board_width, board_height = (830, 660)

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Nonogram')
    clock = pygame.time.Clock()
    screen.fill((255,255,255))

    background_surface = pygame.image.load('images/sudokuboard.jpg').convert()
    background_surface = pygame.transform.scale(background_surface, (board_width,board_height))
    corbel_font = pygame.font.SysFont('Corbel',int(width / 5))
    text = corbel_font.render('NONOGRAM',True, (0,0,0))

    answer_board = generate_answer_board(playboard)
    empty_with_answer_counts = generate_answer_counts_with_board(board, answer_board)

    def mark_square(dimensions):
        '''

        '''
        pygame.draw.rect(background_surface,(0,0,0),dimensions)
    
    while True:

        # blit parameters: surface that should be put on screen, where to put it
        screen.blit(background_surface, (170,340))
        screen.blit(text, (int(width/15),int(height/25)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                box_length = board_width // 9
                box_height = board_height // 9

                clicked_row = int((mouseX - 170) // box_length)
                clicked_column = int((mouseY - 340) // box_height)

                x = box_length * clicked_row
                y = box_height * clicked_column
                clicked_box_dimensions = (x, y, x + box_length, y + box_height)

                # Skips the click if it is outside the board
                if clicked_row < 0 or clicked_column < 0:
                    continue
                
                mark_square(clicked_box_dimensions)

        clock.tick(30)
        pygame.display.update()

if __name__ == '__main__':
    game()