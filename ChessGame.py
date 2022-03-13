import pygame
import sys

class Knight(pygame.sprite.Sprite):
    def __init__(self, team, startX, startY):
        self.x = startX
        self.y = startY
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Knight.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Knight.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))
class Pawn(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        pass

class Bishop(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        pass

class Rook(pygame.sprite.Sprite):
    def __init__(self):
        pass

class Queen(pygame.sprite.Sprite):
    def __init__(self):
        pass


class King(pygame.sprite.Sprite):
    def __init__(self):
        pass


#Initializes the game
pygame.init()

#Size of the pygame window/screen
WIDTH = 1024
HEIGHT = 1024
SQUARE_SIZE = 128


#Chess board backround
backround = pygame.image.load("Images/ChessBoard.jpg")
backround = pygame.transform.scale(backround, (WIDTH,HEIGHT))
whiteQueen = pygame.image.load("Images/White_Queen.png")

#Setting up the screen dimesions and "object"
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#While true the game will run
running = True
#piecePostion = 

def InitializeBoardPieces():
    blackKnight1 = Knight("black", SQUARE_SIZE,0)
    blackKnight2 = Knight("black", 6 * SQUARE_SIZE,0)
    whiteKnight1 = Knight("white", SQUARE_SIZE, 7 * SQUARE_SIZE)
    whiteKnight2 = Knight("white", 6 * SQUARE_SIZE, 7 * SQUARE_SIZE)




#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(backround, (0,0))
    InitializeBoardPieces()
    
    # Flip the display
    pygame.display.update()
    
pygame.quit()