# Break into more files later

import pygame

def game():
    '''
    DESCRIPTION OF GAME 
    '''
    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('Nonogram')
    clock = pygame.time.Clock()
    background_surface = pygame.image.load('images/orange_peach_gradient.jpg').convert()
    background_surface = pygame.transform.scale(background_surface, (1000,1000))
    
    while True:
        # blit parameters: surface that should be put on screen, where to put it
        screen.blit(background_surface, (0,0))
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.update()

if __name__ == '__main__':
    game()