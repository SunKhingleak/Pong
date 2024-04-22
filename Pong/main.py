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

# Initialize classes
ball = Ball()
paddles = Paddles()
screens = Screen()

while True:
    # Grab all pygame events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for game inputs
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

    # Draw the menu screen
    if screens.menu:
        screens.Menu(screen)
        paddles.draw_paddles(screen)

    # Draw the game screen
    if screens.game:
        # Remove menu screen
        screen.fill('black')

        # Draw in-game objects
        ball.draw_ball(screen)
        paddles.draw_paddles(screen)

        # Move the ball and paddles
        ball.move_ball()
        paddles.move_paddle1()
        paddles.move_paddle2()

    # Check for win conditions
    if ball.player1_point == 3:
        # Reset the game if Game_Over returns False else keep drawing the gameover menu
        if not screens.Game_Over('Player One', screen):
            ball.restart()
    if ball.player2_point == 3:
        if not screens.Game_Over('Player Two', screen):
            ball.restart()

    # Update the scores if it's not the menu screen
    if not screens.menu:
        player1_score = score_font.render(str(ball.player1_point), False, 'white')
        player2_score = score_font.render(str(ball.player2_point), False, 'white')
        screen.blit(player1_score, (width / 4, 20))
        screen.blit(player2_score, (3 * width / 4, 20))

    # Update the display
    pygame.display.update()
    clock.tick(60)