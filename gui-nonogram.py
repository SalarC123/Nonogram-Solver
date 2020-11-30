# Make classes later                                        TODO

import pygame
import random

def game():
    '''
    DESCRIPTION OF GAME 
    '''
    pygame.init()
    width, height = (1000,1000)
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Nonogram')
    clock = pygame.time.Clock()
    screen.fill((255,255,255))
    background_surface = pygame.image.load('images/sudokuboard.jpg').convert()
    background_surface = pygame.transform.scale(background_surface, (1000,800))
    corbel_font = pygame.font.SysFont('Corbel',int(width / 5))
    text = corbel_font.render('NONOGRAM',True, (0,0,0))
    
    while True:

        # blit parameters: surface that should be put on screen, where to put it
        screen.blit(background_surface, (0,200))
        screen.blit(text, (int(width/15),int(height/25)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        clock.tick(30)
        pygame.display.update()


if __name__ == '__main__':
    game()