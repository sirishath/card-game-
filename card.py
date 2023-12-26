'''
Name: Sirisha Thapa 
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank
and a suit. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.



'''
from graphics2 import *
import time

class Card:
    '''
    Card represents one standard poker card with an image to display
    
    instance variables:
    image (Image): the Image that will be displayed for the card
    rank (int): the rank of the card (ace is 1 or 14, jack is 11, queen is 12, king is 13, joker is 0)
    suit (str): the suit of the card ('h' is hearts, 'd' is diamonds, 's' is spades, 'c' is clubs, 'j' is joker) 
    '''
    def __init__ (self,fileName):
        '''
        The image's file name will be received.Using that file name, an Image
        object needs to be created at Point(0, 0) storing it in the instance variable image.
        The instance variables rank andsuit also will be initialized extracting their values from the file name.
        Store the rank as an int (not a string)
        
        Parameters:
        fileName = name of the image file.
        '''
        
        self.image = Image(Point(0,0),fileName)
        self.suit = fileName[(len(fileName) - 1) - 4 ]
        #print(self.suit)
        rank = fileName[6:(len(fileName) - 5)]
        
        self.rank = int(rank)
        
         #print(self.rank)
    
        

        
        
    
    def getImage(self):
        '''
        it returns the image of the cards
        '''
        return self.image
        
        
    def getRank(self):
        '''
        finds the rank of the card and returns it 
        '''
        return self.rank 
        
        
    def getSuit(self):
        '''
        finds the suit of the card and returns it 
        '''
        return self.suit
    
    def draw(self,window):
        '''
        draws the image of the card on the window.
        Parameter:
        window (Graphwin) : the window for the card game.
        
        '''
        self.image.draw(window)
    
    def undraw(self):
        '''
        undraw / removes the image of the card from window
        '''
        self.image.undraw()
        
        
    def move(self,dx,dy):
        '''
        moves the card dx pixels in the horizontal direction and dy pixels in the vertical direction
        
        parameters :
        dx =  moves the image to left or right.
        dy = moves the image up or down.
        '''
        self.image.move(dx,dy)
        
        
    def containsPoint(self,point):
        '''
        returns True if the point received as a parameter is within the bounds of the card. Otherwise,
        it returns False.
        
        Parameter:
        Point (click) = points or clicks on window by user.
        
        Returns:
        returns True or False based upon the condition.
        '''
        imgHeight = self.image.getHeight()
        imgWidth = self.image.getWidth()
        
        center = self.image.getCenter()
        
        width_left  = center.getX() - imgWidth / 2
        width_right = center.getX() + imgWidth / 2
        
        height_top = center.getY() - imgHeight / 2
        height_bottom = center.getY() + imgHeight / 2
        
        if (point.getX() > width_left and point.getX() < width_right)  and (point.getY() > height_top and point.getY() < height_bottom):
            
            return True
        else:
            
            return False
        
            
    def __str__(self):
        
        '''
        it shows string representation of the code but with the values of that object's instance variables.
        Returns:
        it returns a string representation of the following form:
        suit = h, rank = 13, center = Point(100, 50).
        '''
        
        
        return f"suit = {self.suit}, rank = {self.rank}, center = {self.image.getCenter()}"
        
        
    
        
    
    

# test code for the Card class
def main():  
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    rank = card.getRank()
    if type(rank) is int:
        print('Rank is an int as it should be.')
    elif type(rank) is str:
        print('ERROR. Rank should be an int. Yours is a string!')
    else:
        print('ERROR. Rank should be an int.')
        
    # move card to center of window and display it
    card.move(250,250)
    card.draw(window)
    
    # click on card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click on card should move it 200 pixels right
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 0)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Diamonds card
    fileName = 'cards/2d.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    
    # move card to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        