import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
	for event in pygame.event.get(): #get all events
		if event.type == pygame.QUIT: #stop running if event is quit
			running = False

	screen.fill("blue") # set bg to blue
	pygame.display.flip() #render

pygame.quit()
