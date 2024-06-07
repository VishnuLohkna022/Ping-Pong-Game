import pygame
pygame.init() # Initialize the pygame

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("PING-PONG BALL GAME")
clock = pygame.time.Clock()


# COLOURS
red = 255,0,0
green = 0,255,0
blue = 0,0,205
white = 255,255,255

# Sounds
hit_sound = pygame.mixer.Sound("paddle_hit.wav")
hit_sound2 = pygame.mixer.Sound("table_hit.wav")




def maingame():
	
	val_y1, val_y2 = 0, 0  # val_y1 is the velocity of paddle 1 which is left paddle and val_y2 is for right paddle
	pad_y1, pad_y2 = int(height/2 - 25), int(height/2 - 25) # Positions of paddles at Y-axis
	size_x, size_y = 5, 50 # size of the paddles
	ball_x, ball_y = int(width/2), 10 # Co-ordinates of the ball
	ball_val_x, ball_val_y = 5, 5 # velocity of the ball


	while True:
		for event in pygame.event.get(): # getting events
			# Quit the game on closing the screen
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			elif event.type == pygame.KEYDOWN: # If any key is pressed
				if event.key == pygame.K_ESCAPE: # if the pressed key is `esc`, close the game
					pygame.quit()
					quit()	
				elif event.key == pygame.K_UP: # if the up key is pressed
					val_y2 = -5 # decrease the pad2(right paddle) velocity by 5
				elif event.key == pygame.K_DOWN: # if the down key is pressed
					val_y2 = 5 # increase the pad2 velocity by 5
				
				if event.key == pygame.K_z: # if the z key is pressed
					val_y1 = -5 # decrease the pad1 velocity by 5
				elif event.key == pygame.K_x: # if the x key is pressed
					val_y1 = 5 # increase the pad1 velocity by 5
			
			elif event.type == pygame.KEYUP: # if any key is released
				if event.key == pygame.K_UP or pygame.K_DOWN: # if up or down key is released
					val_y2 = 0 # assign zero to the pad2 velocity
				if event.key == pygame.K_z or pygame.K_x: # if z or x key is released
					val_y1 = 0 # assign zero to the pad1 velocity
			


		# add the velocities in y coordinate axis of pad1 and pad2
		pad_y1 += val_y1
		pad_y2 += val_y2
		
			
		
		# Don't let the paddles go off the screen
		if pad_y1 <= 0:
			pad_y1 = 0
		elif pad_y1 >= (height-size_y):
			pad_y1 = (height-size_y)
		if pad_y2 <= 0:
			pad_y2 = 0
		elif pad_y2 >= (height-size_y):
			pad_y2 = (height-size_y)		
		
		
		
		screen.fill(white)
		
		# PADDLES
		paddle1 = pygame.draw.rect(screen, blue, [0, pad_y1, size_x, size_y])
		paddle2 = pygame.draw.rect(screen, blue, [width-size_x, pad_y2, size_x, size_y])
		
		# BALL
		ball_center = (ball_x, ball_y)
		ball_x += ball_val_x
		ball_y += ball_val_y
		ball = pygame.draw.circle(screen, red, ball_center, 5) # 5 is the radius of the ball(circle)
		
		
		# If Missed Ball Then Out
		if ball.right <= 0: # If the ball leaves the screen from the left side
			break
		elif ball.left >= width: # If the ball leaves the screen from the right side
			break

		# If Ball Collides with Pads Then Change Pos
		if paddle2.colliderect(ball): # If the ball collides with the right paddle
			hit_sound.play() # play the hit sound
			ball_val_x = -5 # decrease the ball velocity at x-axis
		elif paddle1.colliderect(ball): # If the ball collides with the left paddle
			hit_sound.play()
			ball_val_x = 5 # increase the ball velocity at x-axis
			
		
		# If Ball Hits The (Top,Bottom,Top Left,Bottom Left,Top Right,Bottom Right) Screen Then Change Pos
		# Top and Bottom
		if ball.bottom >= height:
			hit_sound2.play()
			ball_val_y = -5
		elif ball.top <= 0:
			hit_sound2.play()
			ball_val_y = 5
		# Corners
		if ball.topleft == (0,0):
			hit_sound2.play()
			ball_val_x = 5
			ball_val_y = 5	
		elif ball.topright == (width,0):
			hit_sound2.play()
			ball_val_x = -5
			ball_val_y = 5	
		elif ball.bottomleft == (0,height):
			hit_sound2.play()
			ball_val_x = 5
			ball_val_y = -5	
		elif ball.topleft == (width,height):
			hit_sound2.play()			
			ball_val_x = -5
			ball_val_y = -5	

		
		clock.tick(50) # Limit the fps to 50
		pygame.display.update() # update the screen
		
maingame()

pygame.quit() # uninitialize the pygame
quit()


