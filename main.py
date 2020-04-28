def matrix_gen():
      while True:
            try:
                  N = int(input('Size of Matrix: '))
                  if N>=2 and N<10:
                        matrix = pd.DataFrame(np.random.randint(2,size=(N,N)),columns=list(range(1,N+1)),index=list(range(1,N+1)))
                        while matrix.any(axis=None):
                              return matrix
                              break
                        else: 
                              matrix = pd.DataFrame(np.random.randint(2,size=(N,N)),columns=list(range(1,N+1)),index=list(range(1,N+1)))
                  else: print('Size of Matrix must be within 2 to 10.')
            except: print('Enter an integer within 2 to 10 to start a game.')

def game_process(matrix,steps_log,round_count):

      try:
            corr = input('Which button to click? (input as x,y or x y) ')
            x = int(corr[0])
            y = int(corr[2])
            for location in [[x,y],[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                  try:
                        matrix.at[location[0],location[1]] = (matrix.at[location[0],location[1]]+1)%2
                  except:
                        continue
            steps_log.append(corr)
            round_count += 1
            return matrix, steps_log, round_count
      except:
            print('Wrong format, please try again.')
      
import numpy as np
import pandas as pd

print('-----\nWelcome to the Elimination Game!\nEnter an integer N from 2 to 9, to start the game by generating a N*N matrix.')
print('The goal is to turn all the buttons into 0s.')
print('During Game, enter the coordinates (x,y) to click on a button, such as enter \'1,2\' or \'1 2\'.')

steps_log=[]
round_count=0

matrix = matrix_gen()
print(matrix)

while matrix.any(axis=None):
      matrix, steps_log, round_count = game_process(matrix,steps_log,round_count)
      print(matrix)
else:
      print(matrix)
      print('You win!')
      print('You took %s steps to finish the game!' %round_count)
      print('Your steps were:')
      print(steps_log)

input('Press \'Enter\' to close the window')
