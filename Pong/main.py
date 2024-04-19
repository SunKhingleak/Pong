import pygame, sys
from game import *
from Screen import *

# Initialize pygame
pygame.init()

# Draw the display surface
width = 1280
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python Pong")
score_font = pygame.font.Font('Pong/Fonts/Pixeboy-z8XGD.ttf', 100)

# Control in-game framerate
clock = pygame.time.Clock()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

ball = Ball()
paddles = Paddles()
screens = Screen()

while True:
    # Grab all pygame events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if screens.game:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddles.paddle1_speed = -8
                if event.key == pygame.K_s:
                    paddles.paddle1_speed = 8
                if event.key == pygame.K_UP:
                    paddles.paddle2_speed = -8
                if event.key == pygame.K_DOWN:
                    paddles.paddle2_speed = 8
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s]:
                    paddles.paddle1_speed = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    paddles.paddle2_speed = 0

    if screens.menu:
        screens.Menu(screen)
        paddles.draw_paddles(screen)

    if screens.game:
        # Draw in-game objects
        screen.fill('black')

        ball.draw_ball(screen)
        paddles.draw_paddles(screen)

        ball.move_ball()
        paddles.move_paddle1()
        paddles.move_paddle2()

    if ball.player1_point == 5:
        if not screens.Game_Over('Player One', screen):
            ball.restart()

    if ball.player2_point == 5:
        if not screens.Game_Over('Player Two', screen):
            ball.restart()


    if not screens.menu:
        player1_score = score_font.render(str(ball.player1_point), False, 'white')
        player2_score = score_font.render(str(ball.player2_point), False, 'white')
        screen.blit(player1_score, (width / 4, 20))
        screen.blit(player2_score, (3 * width / 4, 20))

    # Update the display
    pygame.display.update()
    clock.tick(60)