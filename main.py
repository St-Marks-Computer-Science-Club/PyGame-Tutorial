# imports the pygame library
import pygame

# initializes pygame
pygame.init()

# maintain a variable that specifies whether or not the game is running
running = True

# create the game window, assign it to a variable to modify if needed in the future
# the two numbers inside are the size of the window
window = pygame.display.set_mode((600, 400))

# set the title of the game window
pygame.display.set_caption('My first pygame')

# create a variable
color = "red"

# this is the main game loop it runs while the variable running is true
while running:

    # this gets all the events that user does to interact with the screen and loops through them
	for event in pygame.event.get():
        # if the user presses the x at the top of the screen, set running to false which means that the loop will exit
		if event.type == pygame.QUIT:
			running = False

        # detect any key presses
		if event.type == pygame.KEYDOWN:

            # detects a specific key is pressed
            # check keys.txt to see the variables for all the different keys
			if event.key == pygame.K_a:
				print("a key pressed")
			if event.key == pygame.K_w:
				print("w key pressed")

	
    # set the window color to the variable color which is red
	window.fill(color)

	# draw a rectangle
    # in the function the first thing is the window which we add it too, next is the color, third is the cordinates (first two), then the width and height(last two)
	pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100])

	# draw a circle
    # in the function the first thing is the window which we add it too, next is the color, third is the cordinates, then you have the radius 
	pygame.draw.circle(window, (0, 255, 0), [300, 300], 100)

	

	# update all changes made to the display
	pygame.display.update()
