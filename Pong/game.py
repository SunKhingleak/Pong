import pygame, random

pygame.init()

width = 1280
height = 800
ball = pygame.Rect(0, 0, 40, 40)
paddle1 = pygame.Rect(0, 0, 20, 150)
paddle2 = pygame.Rect(0, 0, 20, 150)

class Ball():
    def __init__(self):
        ball.center = (width / 2, height / 2)
        self.player1_point = 0
        self.player2_point = 0
        self.ball_speedx = 10
        self.ball_speedy = 10
        
    def draw_ball(self, screen):
        pygame.draw.ellipse(screen, 'white', ball)
        
    def move_ball(self):
        ball.x +=  self.ball_speedx
        ball.y += self.ball_speedy

        if ball.bottom >= height or ball.top <= 0:
            self.ball_speedy *= -1

        if ball.right >= width:
            ball.center = (width / 2, height / 2)
            self.ball_speedx *= random.choice([1, -1])
            self.ball_speedy *= random.choice([1, -1])
            self.player1_point += 1

        if ball.left <= 0:
            ball.center = (width / 2, height / 2)
            self.ball_speedx *= random.choice([1, -1])
            self.ball_speedy *= random.choice([1, -1])
            self.player2_point += 1

        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            self.ball_speedx *= -1

    def restart(self):
        self.player1_point = 0
        self.player2_point = 0

class Paddles():
    def __init__(self):
        paddle1.centery = height / 2
        paddle2.midright = (width, height / 2)
        self.paddle1_speed = 0
        self.paddle2_speed = 0

    def draw_paddles(self, screen):
        pygame.draw.rect(screen, 'white', paddle1)
        pygame.draw.rect(screen, 'white', paddle2)

    def move_paddle1(self):
        paddle1.y += self.paddle1_speed

        if paddle1.bottom >= height:
            paddle1.bottom = height

        if paddle1.top <= 0:
            paddle1.top = 0

    def move_paddle2(self):
        paddle2.y += self.paddle2_speed

        if paddle2.bottom >= height:
            paddle2.bottom = height
        
        if paddle2.top <= 0:
            paddle2.top = 0