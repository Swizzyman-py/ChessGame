import click
from numpy import square
import pygame
import sys

obj_list = []
class piece(pygame.sprite.Sprite):
    def __init__(self, name, team, array=None):
        self.x = array[0]
        self.y = array[1]
        self.team = team
        self.name = name
        self. position = self.SetPieceSquare()
        
    def PlacePic(self):
        screen.blit(self.pic, (self.x, self.y))


    def SetPieceSquare(self):
        self.square = [self.x/SQUARE_SIZE, self.y/SQUARE_SIZE]
        piecePosition[self.name] = self.square

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)


        


class Knight(piece):
    def __init__(self, name, team, array):
        super().__init__(name, team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Knight.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Knight.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        self.PlacePic()
        
        
class Pawn(piece):
    def __init__(self, name, team, array):
        super().__init__(name, team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Pawn.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Pawn.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        self.PlacePic()
class Bishop(piece):
    def __init__(self, name, team, array):
        super().__init__(name, team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Bishop.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Bishop.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        self.PlacePic()
class Rook(piece):
    def __init__(self, name, team, array):
        super().__init__(name, team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Rook.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Rook.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        self.PlacePic()

class Queen(piece):
    def __init__(self, name, team, array):
        super().__init__(name, team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_Queen.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_Queen.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        self.PlacePic()


class King(piece):
    def __init__(self, name, team, array):
        super().__init__(name, team, array)
        if(team == "black"):
            self.pic = pygame.image.load("Images/Black_King.png")
        if(team == "white"):
            self.pic = pygame.image.load("Images/White_King.png")
        self.pic = pygame.transform.scale(self.pic, (SQUARE_SIZE,SQUARE_SIZE))
        self.PlacePic()


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

#Change the name of the window
pygame.display.set_caption('Chess')

#Sets the icon of the window
icon = pygame.image.load("Images/Chess_Icon.png")
pygame.display.set_icon(icon)

#While true the game will run
running = True


#piecePostion = 
piecePosition = {}

def InitializeBoardPieces():
    #Black pieces
    blackKnight1 = Knight("blackKnight1", "black", [SQUARE_SIZE,0])
    obj_list.append(blackKnight1)
    blackKnight2 = Knight("blackKnight2","black", [6 * SQUARE_SIZE,0])
    obj_list.append(blackKnight2)
    blackRook1 = Rook("blackRook1", "black", [0,0])
    obj_list.append(blackRook1)
    blackRook2 = Rook("blackRook2", "black", [7 * SQUARE_SIZE,0])
    obj_list.append(blackRook2)
    blackBishop1 = Bishop("blackBishop1", "black", [2 * SQUARE_SIZE,0])
    obj_list.append(blackBishop1)
    blackBishop2 = Bishop("blackBishop2", "black", [5 * SQUARE_SIZE,0])
    obj_list.append(blackBishop2)
    blackQueen = Queen("blackQueen", "black", [3 * SQUARE_SIZE, 0])
    obj_list.append(blackQueen)
    blackKing = King("blackKing", "black", [4 * SQUARE_SIZE, 0])
    obj_list.append(blackKing)
    blackPawn1 = Pawn("blackPawn1", "black", [0, SQUARE_SIZE])
    blackPawn2 = Pawn("blackPawn2", "black", [1 * SQUARE_SIZE, SQUARE_SIZE])
    blackPawn3 = Pawn("blackPawn3", "black", [2 * SQUARE_SIZE, SQUARE_SIZE])
    blackPawn4 = Pawn("blackPawn4", "black", [3 * SQUARE_SIZE, SQUARE_SIZE])
    blackPawn5 = Pawn("blackPawn5", "black", [4 * SQUARE_SIZE, SQUARE_SIZE])
    blackPawn6 = Pawn("blackPawn6", "black", [5 * SQUARE_SIZE, SQUARE_SIZE])
    blackPawn7 = Pawn("blackPawn7", "black", [6 * SQUARE_SIZE, SQUARE_SIZE])
    blackPawn8 = Pawn("blackPawn8", "black", [7 * SQUARE_SIZE, SQUARE_SIZE])
    obj_list.append(blackPawn1)
    obj_list.append(blackPawn2)
    obj_list.append(blackPawn3)
    obj_list.append(blackPawn4)
    obj_list.append(blackPawn5)
    obj_list.append(blackPawn6)
    obj_list.append(blackPawn7)
    obj_list.append(blackPawn8)
    
    #White pieces
    whiteRook1 = Rook("whiteRook1", "white", [0,7 * SQUARE_SIZE])
    obj_list.append(whiteRook1)
    whiteRook2 = Rook("whiteRook2", "white", [7 * SQUARE_SIZE,7 * SQUARE_SIZE])
    obj_list.append(whiteRook2)
    whiteKnight1 = Knight("whiteKnight1", "white", [SQUARE_SIZE, 7 * SQUARE_SIZE])
    obj_list.append(whiteKnight1)
    whiteKnight2 = Knight("whiteKnight2", "white", [6 * SQUARE_SIZE, 7 * SQUARE_SIZE])
    obj_list.append(whiteKnight2)
    whiteBishop1 = Bishop("whiteBishop1", "white", [2 * SQUARE_SIZE, 7 * SQUARE_SIZE])
    obj_list.append(whiteBishop1)
    whiteBishop2 = Bishop("whiteBishop2", "white", [5 * SQUARE_SIZE, 7 * SQUARE_SIZE])
    obj_list.append(whiteBishop2)
    whiteQueen = Queen("whiteQueen", "white", [3 * SQUARE_SIZE, 7 * SQUARE_SIZE])
    obj_list.append(whiteQueen)
    whiteKing = King("whiteKing", "white", [4 * SQUARE_SIZE, 7 * SQUARE_SIZE])
    obj_list.append(whiteKing)
    whitePawn1 = Pawn("whitePawn1", "white", [0, 6 * SQUARE_SIZE])
    whitePawn2 = Pawn("whitePawn2", "white", [1 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    whitePawn3 = Pawn("whitePawn3", "white", [2 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    whitePawn4 = Pawn("whitePawn4", "white", [3 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    whitePawn5 = Pawn("whitePawn5", "white", [4 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    whitePawn6 = Pawn("whitePawn6", "white", [5 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    whitePawn7 = Pawn("whitePawn7", "white", [6 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    whitePawn8 = Pawn("whitePawn8", "white", [7 * SQUARE_SIZE, 6 * SQUARE_SIZE])
    obj_list.append(whitePawn1)
    obj_list.append(whitePawn2)
    obj_list.append(whitePawn3)
    obj_list.append(whitePawn4)
    obj_list.append(whitePawn5)
    obj_list.append(whitePawn6)
    obj_list.append(whitePawn7)
    obj_list.append(whitePawn8)

   
def ClickSquareLocation(pos):
    square = [0,0]
    if pos[0] <= 128:
        square[0] = 1
    elif pos[0] <= 256:
        square[0] = 2
    elif pos[0] <= 384:
        square[0] = 3
    elif pos[0] <= 512:
        square[0] = 4
    elif pos[0] <= 640:
        square[0] = 5
    elif pos[0] <= 768:
        square[0] = 6
    elif pos[0] <= 896:
        square[0] = 7
    elif pos[0] <= 1024:
        square[0] = 8


    if pos[1] <= 128:
        square[1] = 1
    elif pos[1] <= 256:
        square[1] = 2
    elif pos[1] <= 384:
        square[1] = 3
    elif pos[1] <= 512:
        square[1] = 4
    elif pos[1] <= 640:
        square[1] = 5
    elif pos[1] <= 768:
        square[1] = 6
    elif pos[1] <= 896:
        square[1] = 7
    elif pos[1] <= 1124:
        square[1] = 8

    return square



#Game loop
while running:

    initialize = False
    if initialize == False:
        InitializeBoardPieces()
        initialize = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for x in range(0,32):
                if(ClickSquareLocation(pos) == obj_list[x].position):
                    obj_list[x].update()
            
            


    screen.blit(backround, (0,0))

    for j in range(0,32):
        obj_list[j].PlacePic()

    
    # Flip the display
    pygame.display.update()
    
pygame.quit()