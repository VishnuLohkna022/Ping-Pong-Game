import pygame
pygame.init()

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
	
	val_y1, val_y2 = 0, 0
	pad_y1, pad_y2 = int(height/2 - 25), int(height/2 - 25)
	size_x, size_y = 5, 50
	ball_x, ball_y = int(width/2), 10
	ball_val_x, ball_val_y = 5, 5


	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()	
				elif event.key == pygame.K_UP:
					val_y2 = -5
				elif event.key == pygame.K_DOWN:
					val_y2 = 5
				
				if event.key == pygame.K_z:
					val_y1 = -5
				elif event.key == pygame.K_x:
					val_y1 = 5		
			
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or pygame.K_DOWN:
					val_y2 = 0
				if event.key == pygame.K_z or pygame.K_x:
					val_y1 = 0	
			


		
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
		ball = pygame.draw.circle(screen, red, ball_center, 5)
		
		
		# If Missed Ball Then Out
		if ball.right <= 0:
			break
		elif ball.left >= width:
			break

		# If Ball Collides with Pads Then Change Pos
		if paddle2.colliderect(ball):
			hit_sound.play()
			ball_val_x = -5
		elif paddle1.colliderect(ball):
			hit_sound.play()
			ball_val_x = 5
			
		
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

		
		clock.tick(50)
		pygame.display.update()
		
maingame()

pygame.quit()
quit()


