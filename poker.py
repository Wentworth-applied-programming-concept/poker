# -*- coding: utf-8 -*-
"""poker

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DyBH712VTIhKhCOX3qkaI5uwWoVbzCRj
"""

from src.core.casino import player, admin

import random

class poker:
    def __init__(self):
        self.player = player()
        self.admin = admin()

        run = False
        while not run:
            userID = input("Enter your player ID: ")
            pword = input("Enter your password: ")

            if self.player.checkLogin(userID, pword):
                run = True
                self.uid = userID
            else:
                print("Login invalid, please try again")

        while run:
            userInput = input("Would you like to play (y/n): ")

            if userInput == 'y':
                self.admin.addWinnings(self.uid, -100)
                money = self.playGame()
                self.admin.addWinnings(self.uid, money)
                self.admin.addGame('Slots', self.uid, money)
                print(f"You earned: {money}, your balance is now {self.player.getWinnings(self.uid)}")
            else:
                quit()

    def playGame(self):
      playerbet = 100
      playerinput = ''
      values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
      suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
      playerscores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
      dealerscores = [0,0,0,0,0,0,0,0,0,0,0,0,0]

      playercard1 = [ random.randint(0, 12) , random.randint(0,3) ]
      playercard2 = [ random.randint(0, 12) , random.randint(0,3) ] 

      dealercard1 = [ random.randint(0, 12) , random.randint(0,3) ]
      dealercard2 = [ random.randint(0, 12) , random.randint(0,3) ] 

      print('You have a ' + values[playercard1[0]] + ' of ' + suites[playercard1[1]])
      print('and a ' + values[playercard2[0]] + ' of ' + suites[playercard2[1]])

      tablecard1 = [ random.randint(0, 12) , random.randint(0,3) ] 
      tablecard2 = [ random.randint(0, 12) , random.randint(0,3) ]
      tablecard3 = [ random.randint(0, 12) , random.randint(0,3) ]

      #adding up the cards that the player or dealer have which have the same value
      for x in range(0,len(values)):
        if (values[playercard1[0]] == values[x]): 
            playerscores[x] += 1 
        if (values[playercard2[0]] == values[x]): 
            playerscores[x] += 1 

        if (values[dealercard1[0]] == values[x]): 
            dealerscores[x] += 1 
        if (values[dealercard2[0]] == values[x]): 
            dealerscores[x] += 1 
      
        if (values[tablecard1[0]] == values[x]): 
            playerscores[x] += 1 
            dealerscores[x] += 1 
        if (values[tablecard2[0]] == values[x]): 
            playerscores[x] += 1 
            dealerscores[x] += 1 
        if (values[tablecard3[0]] == values[x]): 
            playerscores[x] += 1
            dealerscores[x] += 1  
            
      
      #this lists out how many of each value card the player and dealer have
      print(playerscores)
      print(dealerscores)
      
      #playerinput = input('Add aditional bet number or f to fold')
      #if (playerinput != 'f'):
      #  playerbet += int(playerinput)
      #  print('The first table card is a ' + values[tablecard1[0]] + ' of ' + suites[tablecard1[1]])
      #  playerinput = input('Add aditional bet number or f to fold')
      #  if (playerinput != 'f'):
      #    playerbet += int(playerinput)
      #    print('The second table card is a ' + values[tablecard2[0]] + ' of ' + suites[tablecard2[1]])
      #    playerinput = input('Add aditional bet number or f to fold')
      #    if (playerinput != 'f'):
      #      playerbet += int(playerinput)
      #      print('The third table card is a ' + values[tablecard3[0]] + ' of ' + suites[tablecard3[1]])
      #      playerinput = input('Add aditional bet number or f to fold')
      #    if (playerinput != 'f'):
      #      playerbet += int(playerinput)
      
      kind = 4 
      #This loop is to find out who has the highest number of the same type of card
      while (kind > 1): #kind starts at 4 of a kind
        for x in range(len(values)-1,0,-1): #starts from ace because they are worth the most
          if (playerscores[x] == kind and dealerscores[x] != kind):
            print('The player has ' + str(kind) + ' ' +  values[x] + '\'s')
            return 5000
          if (dealerscores[x] == kind and playerscores[x] != kind):
            print('The dealer has ' + str(kind) + ' ' +  values[x] + '\'s')
            return 0
        kind -= 1

if __name__ == '__main__':
    poker()