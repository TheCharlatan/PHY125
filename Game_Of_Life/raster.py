from pylab import *
import copy
import random


class Raster:

  def __init__(self, x=5, y=5):
    self.dim_x = x
    self.dim_y = y
    self.grid = zeros((self.dim_x,self.dim_y)).astype('int')
    self.temp  = []
    self.alive = 0
    self.round_alive =  [0]*1000
    self.population_buffer = range(1000)
    self.iteration = 0
    self.pop_flag = 0
    for i in self.round_alive:
      i = 0
    self.live_quadrant = [0]*4

  def out(self, grid): #Print out the raster
    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
      for row in grid]))

  def populate(self,x,y): #Inserts alive cell in position x,y
    self.grid[x-1][y-1] = 1
    self.alive += 1

  def detect_filled(self, x, y): #Counts number of alive cells around x,y
    self.counter = 0
    for i in (-1,0,1):
      for j in (-1,0,1):
        if self.temp[(x+i)%self.dim_x][(y+j)%self.dim_y] == 1: # Use % to wrap around the board for the edge cases
          self.counter = self.counter + 1
    if self.temp[x][y] == 1: #If the cell is already occupied, do not count itself
      self.counter = self.counter - 1
      self.pop_flag = 1
    return self.counter

  def kill(self, x, y): #Kills cell in x,y
    self.grid[x][y] = 0
    if self.pop_flag:
      if x < self.dim_x / 2 and y < self.dim_y/2:   #Top left
        self.live_quadrant[0] -= 1
      if x >  self.dim_x / 2 and y < self.dim_y/2:  #Top right
        self.live_quadrant[1] -= 1
      if x < self.dim_x / 2 and y > self.dim_y/2:   #Bottom left
        self.live_quadrant[2] -= 1
      if x > self.dim_x / 2 and y > self.dim_y/2:   #Bottom right
        self.live_quadrant[3] -= 1
      self.alive -= 1
      self.pop_flag = 0

  def spawn(self, x, y):
    self.grid[x][y] = 1
    if not self.pop_flag:                        #Quadrant range from life to right, then from top to bottom
      if x < self.dim_x / 2 and y < self.dim_y/2: #Top left
        self.live_quadrant[0] += 1
      if x >  self.dim_x / 2 and y < self.dim_y/2: #Top right
        self.live_quadrant[1] += 1
      if x < self.dim_x / 2 and y > self.dim_y/2: #Bottom left
        self.live_quadrant[2] += 1
      if x > self.dim_x / 2 and y > self.dim_y/2: #Bottom right
        self.live_quadrant[3] += 1
      self. alive += 1
    self.pop_flag = 0

  def run(self): #Runs one game iteration
    self.temp = copy.copy(self.grid)
    for i in range(0,self.dim_x):
      for j in range(0,self.dim_y):
        score = self.detect_filled(i,j)
        #print(score)
        if score > 3:
          self.kill(i, j)
        elif score < 2:
          self.kill(i, j)
        elif score == 3:
          self.spawn(i, j)
        elif score == 2 and self.temp[i][j] == 1:
          self.spawn(i, j)
    #Now follows a block to present the live population data
    if self.iteration < 1000:
      self.round_alive[self.iteration] = self.alive
    else:
      for i in range(0,999):
        self.round_alive[i] = self.round_alive[i+1]
    self.round_alive[999] = self.alive
    self.iteration += 1


  def random_spawn(self, probability):
    for i in range(0,self.dim_x):
      for j in range(0,self.dim_y):
        if randint(0,probability+1) == probability:
          self.grid[i][j] = 1
          self.alive += 1

  def pop_form(self, name, x, y):
    if name == 'Glider':
      self.populate(x,y)
      self.populate(x+1,y+1)
      self.populate(x+1,y+2)
      self.populate(x+2,y)
      self.populate(x+2,y+1)
    if name == 'Block':
      self.grid[x:x+2,y:y+2] = 1
      self.alive += 5
    if name == 'Blinker':
      self.grid[x,y:y+3] = 1
      self.alive += 3
    if name == 'Toad':
      self.grid[x,y] = 1
      self.grid[x+1,y+3] = 1
      self.grid[x:x+2,y+1:y+3] = 1
      self.alive += 5

























































