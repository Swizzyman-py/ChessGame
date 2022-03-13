import pygame
import sys

class piece(pygame.sprite.Sprite):
    def __init__(self):
        self.alive = True



class Knight(pygame.sprite.Sprite):
    def __init__(self):
        super(piece, self).__init__()

class Pawn(pygame.sprite.Sprite):
    def __init__(self):
        super(piece, self).__init__()

class Bishop(pygame.sprite.Sprite):
    def __init__(self):
        super(piece, self).__init__()

class Rook(pygame.sprite.Sprite):
    def __init__(self):
        super(piece, self).__init__()

class Queen(pygame.sprite.Sprite):
    def __init__(self):
        super(piece, self).__init__()


class King(pygame.sprite.Sprite):
    def __init__(self):
        super(piece, self).__init__()


#Initializes the game
pygame.init()

#Size of the pygame window/screen
WIDTH = 1024
HEIGHT = 1024

#Common colors that I wont ever use..
WHITE =(255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN =(0,255,0)
YELLOW = (0,0,255)

#Chess board backround
backround = pygame.image.load("ChessBoard.jpg")
backround = pygame.transform.scale(backround, (WIDTH,HEIGHT))
whiteQueen = pygame.image.load("White_Queen.png")

#Setting up the screen dimesions and "object"
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#While true the game will run
running = True

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(backround, (0,0))
    screen.blit(whiteQueen, (100,100))

    # Flip the display
    pygame.display.update()

pygame.quit()