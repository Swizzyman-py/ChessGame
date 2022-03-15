import pygame
import sys


class piece():
    def __init__(self, team, array=None):
        self.x = array[0]
        self.y = array[1]
        self.team = team
        


class Knight(piece):
    def __init__(self, team, array):
        super().__init__(team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Knight.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Knight.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))
        
class Pawn(piece):
    def __init__(self, team, array):
        super().__init__(team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Pawn.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Pawn.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))
class Bishop(piece):
    def __init__(self, team, array):
        super().__init__(team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Bishop.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Bishop.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))
class Rook(piece):
    def __init__(self, team, array):
        super().__init__(team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Rook.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Rook.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))
class Queen(piece):
    def __init__(self, team, array):
        super().__init__(team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Queen.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Queen.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))


class King(piece):
    def __init__(self, team, array):
        super().__init__(team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_King.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_King.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        screen.blit(self.pic, (self.x, self.y))


#Initializes the game
pygame.init()

#Size of the pygame window/screen
WIDTH = 1024
HEIGHT = 1024
SQUARE_SIZE = 128


#Chess board backround
backround = pygame.image.load("Images/ChessBoard.png")
backround = pygame.transform.scale(backround, (WIDTH,HEIGHT))


#Setting up the screen dimesions and "object"
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#While true the game will run
running = True
#piecePostion = 

def InitializeBoardPieces():
    blackKnight1 = Knight("black", [SQUARE_SIZE,0])
    blackKnight2 = Knight("black", (6 * SQUARE_SIZE,0))
    blackRook1 = Rook("black", (0,0))
    blackRook2 = Rook("black", (7 * SQUARE_SIZE,0))
    blackBishop1 = Bishop("black", (2 * SQUARE_SIZE,0))
    blackBishop2 = Bishop("black", (5 * SQUARE_SIZE,0))
    blackQueen = Queen("black", (3 * SQUARE_SIZE, 0))
    blackKing = King("black", (4 * SQUARE_SIZE, 0))
    blackPawn1 = Pawn("black", (0, SQUARE_SIZE))
    blackPawn2 = Pawn("black", (1 * SQUARE_SIZE, SQUARE_SIZE))
    blackPawn3 = Pawn("black", (2 * SQUARE_SIZE, SQUARE_SIZE))
    blackPawn4 = Pawn("black", (3 * SQUARE_SIZE, SQUARE_SIZE))
    blackPawn5 = Pawn("black", (4 * SQUARE_SIZE, SQUARE_SIZE))
    blackPawn6 = Pawn("black", (5 * SQUARE_SIZE, SQUARE_SIZE))
    blackPawn7 = Pawn("black", (6 * SQUARE_SIZE, SQUARE_SIZE))
    blackPawn8 = Pawn("black", (7 * SQUARE_SIZE, SQUARE_SIZE))
    


    
    whiteRook1 = Rook("white", (0,7 * SQUARE_SIZE))
    whiteRook2 = Rook("white", (7 * SQUARE_SIZE,7 * SQUARE_SIZE))
    whiteKnight1 = Knight("white", (SQUARE_SIZE, 7 * SQUARE_SIZE))
    whiteKnight2 = Knight("white", (6 * SQUARE_SIZE, 7 * SQUARE_SIZE))
    whiteBishop1 = Bishop("white", (2 * SQUARE_SIZE, 7 * SQUARE_SIZE))
    whiteBishop2 = Bishop("white", (5 * SQUARE_SIZE, 7 * SQUARE_SIZE))
    whiteQueen = Queen("white", (3 * SQUARE_SIZE, 7 * SQUARE_SIZE))
    whiteKing = King("white", (4 * SQUARE_SIZE, 7 * SQUARE_SIZE))
    whitePawn1 = Pawn("white", (0, 6 * SQUARE_SIZE))
    whitePawn2 = Pawn("white", (1 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    whitePawn3 = Pawn("white", (2 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    whitePawn4 = Pawn("white", (3 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    whitePawn5 = Pawn("white", (4 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    whitePawn6 = Pawn("white", (5 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    whitePawn7 = Pawn("white", (6 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    whitePawn8 = Pawn("white", (7 * SQUARE_SIZE, 6 * SQUARE_SIZE))
   




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