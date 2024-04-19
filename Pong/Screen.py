import pygame, sys
from game import *

pygame.init()
ball = Ball()
width = 1280
height = 800

font = pygame.font.Font('Pong/Fonts/Pixeboy-z8XGD.ttf', 60)
winner_font = pygame.font.Font('Pong/Fonts/Pixeboy-z8XGD.ttf', 100)
pong_font = pygame.font.Font('Pong/Fonts/Pixeboy-z8XGD.ttf', 300)
start_rect = pygame.Rect(0, 0, 150, 50)
start_rect.center = (width / 2, height // 1.7)
quit_rect = pygame.Rect(0, 0, 150, 50)
quit_rect.center = (width / 2, height // 1.4)
play_again_rect = pygame.Rect(0, 0, 300, 50)
play_again_rect.center = (width / 2, height // 1.5)
main_menu_rect = pygame.Rect(0, 0, 300, 50)
main_menu_rect.center = (width / 2, height // 1.2)

class Screen():
    def __init__(self):
        self.menu = True
        self.game = False
        self.game_over = False

    def Menu(self, screen):
        screen.fill('black')
        pos = pygame.mouse.get_pos()
    
        if start_rect.collidepoint(pos):
            pygame.draw.rect(screen, 'white', start_rect)
            start_button = font.render('Play', False, 'black')
            if pygame.mouse.get_pressed()[0] and self.menu:
                self.menu = False
                self.game = True

        else: 
            pygame.draw.rect(screen, 'black', start_rect)
            start_button = font.render('Play', False, 'white')

        if quit_rect.collidepoint(pos):
            pygame.draw.rect(screen, 'white', quit_rect)
            quit_button = font.render('Quit', False, 'black')
            if pygame.mouse.get_pressed()[0]:
                sys.exit()
        else:
            pygame.draw.rect(screen, 'black', quit_rect)
            quit_button = font.render('Quit', False, 'white')

        screen.blit(start_button, start_button.get_rect(centerx = start_rect.centerx, centery = start_rect.centery))
        screen.blit(quit_button, quit_button.get_rect(centerx = quit_rect.centerx, centery = quit_rect.centery))
        pong_logo = pong_font.render('P O N G', True, 'white')
        pong_rect = pong_logo.get_rect()
        pong_rect.center = (width / 2, height / 4)
        screen.blit(pong_logo, pong_rect)

    
    def Game_Over(self, winner, screen):
        self.game = False
        self.winner = winner
        winner_text = winner_font.render(f'{self.winner} Wins', False, 'white')
        winner_rect = winner_text.get_rect()
        winner_rect.center = (width / 2, height / 2)
        screen.blit(winner_text, winner_rect)

        pos = pygame.mouse.get_pos()

        if play_again_rect.collidepoint(pos):
            pygame.draw.rect(screen, 'white', play_again_rect)
            play_again_button = font.render('Play Again', False, 'black')
            if pygame.mouse.get_pressed()[0] and not self.game:
                self.game = True
                return False
            
        else:
            pygame.draw.rect(screen, 'black', play_again_rect)
            play_again_button = font.render('Play  Again', False, 'white')

        if main_menu_rect.collidepoint(pos):
            pygame.draw.rect(screen, 'white', main_menu_rect)
            main_menu_button = font.render('Main Menu', False, 'black')
            if pygame.mouse.get_pressed()[0] and not self.game:
                self.menu = True
                return False

        else:
            pygame.draw.rect(screen, 'black', main_menu_rect)
            main_menu_button = font.render('Main Menu', False, 'white')

        screen.blit(play_again_button, play_again_button.get_rect(centerx = play_again_rect.centerx, centery = play_again_rect.centery))
        screen.blit(main_menu_button, main_menu_button.get_rect(centerx = main_menu_rect.centerx, centery = main_menu_rect.centery))

        return True

            