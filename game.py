# VERSION 0.1
# Author: Paul Kukowski (https://github.com/g0dnerd)
# License: see LICENSE file


import pygame
from pygame.locals import *
from random import randrange

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169, 169, 169)

X_SIZE = 500
Y_SIZE = 500
OFFSET = 10

pygame.init()

# Set the width and height of the screen [width, height]
size = (X_SIZE, Y_SIZE)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False
time_elapsed = 0
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
# Initialize the grid
gridWidth, gridHeight = int((X_SIZE / OFFSET)), int((Y_SIZE / OFFSET));
grid = [[0 for x in range(gridWidth)] for y in range(gridHeight)]


# Fill the grid with a random amount (between 120 and 150) of live cells
# startAmount = randrange(160, 190)

#for i in range(startAmount):
#	j = randrange(0, gridWidth)
#	k = randrange(0, gridHeight)
#	grid[j][k] = 1

#----- 3-period PULSAR
grid[4][2] = 1
grid[5][2] = 1
grid[6][2] = 1
grid[10][2] = 1
grid[11][2] = 1
grid[12][2] = 1

grid[2][4] = 1
grid[7][4] = 1
grid[9][4] = 1
grid[14][4] = 1

grid[2][5] = 1
grid[7][5] = 1
grid[9][5] = 1
grid[14][5] = 1

grid[2][6] = 1
grid[7][6] = 1
grid[9][6] = 1
grid[14][6] = 1

grid[4][7] = 1
grid[5][7] = 1
grid[6][7] = 1
grid[10][7] = 1
grid[11][7] = 1
grid[12][7] = 1

grid[4][9] = 1
grid[5][9] = 1
grid[6][9] = 1
grid[10][9] = 1
grid[11][9] = 1
grid[12][9] = 1

grid[2][10] = 1
grid[7][10] = 1
grid[9][10] = 1
grid[14][10] = 1

grid[2][11] = 1
grid[7][11] = 1
grid[9][11] = 1
grid[14][11] = 1

grid[2][12] = 1
grid[7][12] = 1
grid[9][12] = 1
grid[14][12] = 1

grid[4][14] = 1
grid[5][14] = 1
grid[6][14] = 1
grid[10][14] = 1
grid[11][14] = 1
grid[12][14] = 1

liveSpaces = list()
killSpaces = list()

# print(grid)


#--- Outputs the number of alive neighbors for a given cell
def get_live_neighbors(grid, x, y):
	neighbors = 0
	try:
		if grid[x+1][y+1] == 1:
			neighbors += 1
	except:
		pass
	try:
		if grid[x-1][y-1] == 1:
			neighbors += 1
	except:
		pass
	try:
		if grid[x-1][y+1] == 1:
			neighbors += 1
	except:
		pass
	try:
		if grid[x+1][y-1] == 1:
			neighbors += 1
	except:
		pass
	try:
		if grid[x+1][y] == 1:
			neighbors += 1
	except:
		pass
	try:
		if grid[x][y+1] == 1:
			neighbors += 1
	except:
		pass
	try:
		if grid[x-1][y] == 1:
			neighbors +=1
	except:
		pass
	try:
		if grid[x][y-1] == 1:
			neighbors += 1
	except:
		pass

	return neighbors


while not done:

	dt = clock.tick()
	time_elapsed += dt

	space = False
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Screen clearing
	screen.fill(WHITE)

    # Draw the grid
	drawOffset = OFFSET
	while drawOffset < X_SIZE:
		pygame.draw.line(screen, GREY,[drawOffset, 0], [drawOffset, Y_SIZE])
		pygame.draw.line(screen, GREY,[0, drawOffset], [X_SIZE, drawOffset])
		drawOffset = drawOffset + 10

	# Fill the grid with live cells
	for i in range(gridWidth):
		for j in range(gridHeight):
			if grid[i][j] == 1:
				pygame.draw.rect(screen, BLACK,(10*i+1, 10*j+1, 8, 8))


	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Detect spacebar presses
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				space = True

	#--- Advance to the next generation after .75 seconds
	if time_elapsed > 750:
		for i in range(gridWidth):
			for j in range(gridHeight):
				neighbors = get_live_neighbors(grid, i, j)
				
				# Implement Life's transition rules
				if grid[i][j] == 1:
					if neighbors < 2:
						app = (i,j)
						killSpaces.append(app)
					if neighbors > 3:
						app = (i,j)
						killSpaces.append(app)
				else:
					if neighbors == 3:
						app = (i,j)
						liveSpaces.append(app)

		# --- Update the grid for the next generation
		for x,y in killSpaces:
			grid[x][y] = 0
		for x,y in liveSpaces:
			grid[x][y] = 1

		killSpaces.clear()
		liveSpaces.clear()
		time_elapsed = 0

	# --- Pauses the loop on spacebar press, continues on the second press
	if space:
		space = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						space = True
			if space:
				break

	# --- If spacebar has been pressed, advance to the next generation
	# if space:
	#	for i in range(gridWidth):
	#		for j in range(gridHeight):
	#			neighbors = get_live_neighbors(grid, i, j)
	#			
				# Implement Life's transition rules
	#			if grid[i][j] == 1:
	#				if neighbors < 2:
	#					app = (i,j)
	#					killSpaces.append(app)
	#				if neighbors > 3:
	#					app = (i,j)
	#					killSpaces.append(app)
	#			else:
	#				if neighbors == 3:
	#					app = (i,j)
	#					liveSpaces.append(app)

	# --- Update the grid for the next generation
	#	for x,y in killSpaces:
	#		grid[x][y] = 0
	#	for x,y in liveSpaces:
	#		grid[x][y] = 1

	#	killSpaces.clear()
	#	liveSpaces.clear()
 
# Close the window and quit.
pygame.quit()