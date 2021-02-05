#**********************************
# *  Name  : Jack Schneiderhan
# * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
# *        : yes
#**********************************

'''
4-Dice Pig

Adapted from Java to Python by Justin Barish,  11/2018
Modified nov '19 by Toby Dalton

~ ~ ~

To exercise your looping ability, we're going to be filling in a bunch
of blanks. yay!

Pig is a game where players take turns rolling dice.
Traditionally, it's only 2, but this is a variant.

The goal is to have their total score reach a certain # of points.
Players take turns earning points by rolling dice.
Each roll adds that sum onto a round score, which my or may not be added
to their total score, dictated as below:

A person's turn lasts until they want to stop rolling or roll some 1s.

If at any point during the player's turn they roll one 1:
their round ends and their round score is added to their total score.

If they roll two 1s:
they lose all points for the round, and their turn is over.

Three 1s:
they lose all of their points in the game, and their turn is over.

If they recieve the luck of four 1s (four-eyed snake ::S):
they immediately lose the game.

Whenever the player decide to stop their turn, their round points are 
added to their total points.

When a player's total points reach 100 (controllable below), they win.
'''
import random

POINTS_TO_WIN = 100
AI_ROUND_TARGET = 20
score1 = 0
score2 = 0

'''
This Homework has 2 parts:

Part 1 (100 pts): Complete the game for two human players.
That is, fill in all of the methods below

Part 2 (15 pts Extra Credit):
Add in an "AI" as the second player, so you will play against the computer.
The AI takes the place of player 2, and will continue rolling until
it reaches its AI_ROUND_TARGET. NOTE: You *will* need to change some of the
function paramaters (I.E. pass in additional values) and other parts of
functions.
'''

#**   
#**   General Game Stuff
#**

def main():
  '''This is the main function for the pig game'''
  welcome()
  while True:
    playGame()
    if not wantsPlayAgain():
      print('Bye!')
      return

def playGame():
  '''Play one game of pig
  Alternates between players, and at the end of a player's turn, 
  prints the overall game score for both players'''

  player = 1
  scores = initScores()
  while not gameOver(scores):
    print()
    print('Current Scores:')
    printScore(scores)
    getMove(scores, player)
    player = 2
    if(gameOver(scores)):
      break
    printScore(scores)
    getMove(scores,player)
    player = 1
  

def initScores():
  '''initialize the scores to 0'''
  score1 = 0
  score2 = 0
  return [score1, score2]

def gameOver(scores):
  '''checks if the game is over
  game is over when either player reaches >= POINTS_TO_WIN.
  [ or 4 ones are rolled :3]
  Prints the win message for the player who won
  If no one won, just returns false'''
  if (scores[0] >= POINTS_TO_WIN):#orwhenplayer2rolls4ones
    printWinMessage(1, scores)
    return True
  elif(scores[1] >= POINTS_TO_WIN):#orwhenplayer1rolls4ones
    printWinMessage(2, scores)
    return True
  return False

def getMove(scores, player):
  '''gets a player's move.
  Before every move, prints the current round score and the game score for the player
  Checks if the player wants to continue, and if they do, rolls dice and appropriately changes scores
  '''
  printPlayerMessage(player)
  roundScore = 0
  while True:
    printCurrentPlayerScore(scores, player, roundScore)
    
    if(not wantsRollAgain(player)):
      if(player == 1):
        scores[0] += roundScore
      elif(player == 2):
        scores[1] += roundScore
      break

    roll = rollDice()
    showRoll(roll)
    if(roll.count(1) == 4):
      print("Rolled four 1s... Game over")
      if(player == 1):
        scores[1] = 101
        scores[0] = 0
      elif(player == 2):
        scores[0] = 101
        score[1] = 0
      break
    elif(roll.count(1) == 3):
      print("Rolled three 1s. Score reset!")
      if(player == 1):
        scores[0] = 0
      elif(player == 2):
        scores[1] = 0
      break
    elif(roll.count(1) == 2): 
      print("Rolled two 1s! Round ended, no score added")
      break
    elif(roll.count(1) == 1): 
      print("Rolled one 1! Round ended, score added")
      if(player == 1):
        scores[0] += roundScore
      elif(player == 2):
        scores[1] += roundScore
      break
    else:
      roundScore += sum(roll)
      

def rollDie():
  '''rolls a single die (wow)'''
  return random.randint(1,6)

def rollDice():
  '''grabs the roll for four dice'''
  L = []
  for i in range(4):
    L.append(rollDie())
  return L

#**   
#**   Checking if we want to [X] again
#**

def wantsContinue(response):
  '''Checks if the response a user gives indicates they want to continue.
  assume the user has to give a Y to mean yes and N to mean no'''
  ans = response
  while(not(ans == "Y" or ans == "N")):
    print("Invalid Input! Please select Y for yes and N for no:")
    ans = input()
  if(ans == "Y"):
    return True
  elif(ans == "N"):
    return False
  
def wantsPlayAgain():
  '''Asks a player if they want to play the game again (use wantsContinue()!)'''
  print()
  print("Would you like to play the game again? (Y for yes and N for no):")
  ans = input()
  return wantsContinue(ans)

def wantsRollAgain(player):
  '''Asks a player if they want to roll again
  For Part 2, also handle the Computer's decision'''
  print("Would you like to roll? (Y for yes and N for no):")
  ans = input()
  return wantsContinue(ans)

#**   
#**   Printing Things
#**

def welcome():
  '''Prints the welcome message for the game.
  We might also print the rules for the game and any other
  information that the user might need to know.'''
  print('Welcome to Pig!')

def printScore(scores):
  '''prints the current game score for each player'''
  print('Player 1: ', end = '')
  print(scores[0], end = '')
  print(' & Player 2: ', end = '')
  print(scores[1], end = '')
  
def printWinMessage(winningPlayer, scores):
  print()
  print('***********************Player ' + str(winningPlayer) + ' Won!************************')
  print('***********************Final Score:*************************')
  printScore(scores)

# TODO
def showRoll(roll):
  ''' prints out the roll'''
  print(roll)

def printPlayerMessage(player):
  print()
  print('--------------------------------------------------------------')
  print('-------------------Player ' + str(player) + '\'s turn----------------------------')
  print('--------------------------------------------------------------')
  print()

def printCurrentPlayerScore(scores, player, roundScore):
  '''print the score for a specific player. Prints their round score 
  and their overall game score not including their current round score'''
  oScore = 0
  if(player == 1):
    oScore = scores[0]
  elif(player == 2):
    oScore = scores[1]
  print("Player " + str(player) + " has a round score of " + str(roundScore) + " and an overall score of " + str(oScore))

if __name__ == '__main__':
  main()






  
