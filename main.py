# Author: Nathan Power
# Date Start: 14/01/2020
# Project: TicTacToe Online


# External Libraries
import time
import random
import flask

# TicTacToe Libraries
#import TicTacToeBot as tb

print("<<<<< TicTacToeGame.py >>>>>")

# Create the game class, this is where everything on the board happens
class Game:
  def __init__(self):
    self.board = [1,2,3,4,5,6,7,8,9] # Create the entire board
    #self.winPositions =  ([0,1,2], [3,4,5], [6,7,8], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9])
    self.turn = "" # Turn, either X or O
    self.turnNumber = 0 # Turn number count to keep track of who's turn it is


  def generateBoard(self): # Show the board to the screen
    print('     1 ', ' 2 ', ' 3 ') # placement guide for the player
    print(f'1  | {self.board[0]} | {self.board[1]} | {self.board[2]} |') # Print row 1
    print(f'2  | {self.board[3]} | {self.board[4]} | {self.board[5]} |') # Print row 2
    print(f'3  | {self.board[6]} | {self.board[7]} | {self.board[8]} |') # Print row 3


  def checkBoard(self):
    return self.board


  def changeTurn(self):
    if (self.turnNumber % 2) == 0: # Checking the current turn
      print("X") # Print who's turn it is (Debugging)
      self.turn = "X" # Make the current player X
    else:
      print("O") # Print who's turn it is (Debugging)
      self.turn = "O" # Make the current player O
    self.turnNumber += 1 # Change turn
    print(f'It is turn: {self.turnNumber}')
    return self.turnNumber, self.turn # Return the current turn number and current player


  def checkTurn(self):
    return self.turn


  def askForPosition(self):
    pass


  def place(self, position):
    self.position = position
    #self.placement = int(input(f"{self.turn}'s Turn: ")) - 1 # Promt the player for their placement	
    try:
      if isinstance(self.board[self.position], int): # If the player's picked place is a number, place it, if not, promt again
        self.board[self.position] = self.turn # Place the piece (I guess it is called a piece)
        return self.turn # This will return the piece that was placed and the place it was placed in...
      else: # Else
        print("NOT VALID PLACEMENT") # Say no
        game.place(self.askForPosition()) # Try again
    except ValueError: 
      print("Woops Value Error, try again") # If there is a ValueError
      game.place(self.askForPosition()) # Try again
    except:
      print("something else went wrong, please try again") # Any other error that I don't care about
      game.place(self.askForPosition()) # Try again
		

  def checkWin(self, *args):
    player = self.checkTurn()
    # Board 0,1,2
    # Board 3,4,5
    # Board 6,7,8

    #for win in self.winPositions: # For all the positions in winPositions
    if self.board[0] == self.board[1] == self.board[2] == player: # If at least one has all locations filled with the same player
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[3] == self.board[4] == self.board[5] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[6] == self.board[7] == self.board[8] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[0] == self.board[4] == self.board[8] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[2] == self.board[4] == self.board[6] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[0] == self.board[3] == self.board[6] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[1] == self.board[4] == self.board[7] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    elif self.board[2] == self.board[5] == self.board[8] == player:
      self.generateBoard() # Show the board
      return "Winner" # Declare winner
    else:
      print("No winner")
      return False # Next turn


class Bot:
  def __init__(self):
    dif_easy = False
    dif_hard = False


  def lookAtBoard(self):
    print("Got Board")
    game.checkBoard()
    game.place


###### End of Class ######

game = Game()
bot = Bot()


def determineGameMode():
  choice = str(input("Which would you like to play? \n Player VS Player  (Enter pvp) \n Player VS Bot (Enter pvb) \n -> ")).upper()
  if choice == 'PVP':
    print('PVP')
    playPVP()
  else:
    print("PVB")
    playPVB()


def askForPosition(chosenPosition):
  return chosenPosition


def playPVP():
  gameOn = True # Keep playing
  while gameOn: # While the game is still on
    game.generateBoard() # Show the board
    game.changeTurn() # Change turn
    game.place(askForPosition(int(input(f"Player {game.turn}, choose your position: ")) - 1)) # Promt for player placement
    if game.checkWin("Winner"): # If checkWin returns True
      print(f'\n{game.turn} WINNER') # Delcare winner
      playAgain = input("Play Again? (Y/N) ").upper() # Ask to play again
      if playAgain == "Y": # If player says yes
        game.board = [1,2,3,4,5,6,7,8,9] # Reset board
        game.turn = "" # Reset current turn
        game.turnNumber = 0 # Reset turn counter

        determineGameMode()
        print("\n### NEW GAME ###\n")
      else:
        gameOn = False
        break # Break out of loop and quit


def playPVB():
  gameOn = True
  while gameOn:
    game.generateBoard()
    game.changeTurn()
    if game.turn == 'X':
      print("PLAYER TURN")
      game.place(askForPosition(int(input(f"Player {game.turn}, choose your position: ")) - 1))
      if game.checkWin():
        print(f'\n{game.turn} WINNER') # Delcare winner
        playAgain = input("Play Again? (Y/N) ").upper() # Ask to play again
        if playAgain == "Y": # If player says yes
          game.board = [1,2,3,4,5,6,7,8,9] # Reset board
          game.turn = "" # Reset current turn
          game.turnNumber = 0 # Reset turn counter
          determineGameMode() 
          print("\n### NEW GAME ###\n")
        else:
          gameOn = False
          break # Break out of loop and quit
    elif game.turn == "O":
      print("BOT TURN")
      #bot.lookAtBoard()
      #print("Looked at board")
      if askForPosition == 1:
        game.place(askForPosition(2))
        if game.checkWin():
          print(f'\n{game.turn} WINNER') # Delcare winner
          playAgain = input("Play Again? (Y/N) ").upper() # Ask to play again
          if playAgain == "Y": # If player says yes
            game.board = [1,2,3,4,5,6,7,8,9] # Reset board
            game.turn = "" # Reset current turn
            game.turnNumber = 0 # Reset turn counter
            determineGameMode()
            print("\n### NEW GAME ###\n")
          else:
            gameOn = False
            break # Break out of loop and quit
        
  

determineGameMode()

print("Thanks for Playing!") 
time.sleep(1) #Let player read message
quit() #Quit the application
