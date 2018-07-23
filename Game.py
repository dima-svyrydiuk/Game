from enemy import *
import pygame
import random
import time

pygame.init()


window = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Test_Game")

l = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
l2 = [1400, 1450, 1500, 1550, 1600, 1650, 1700]

miscia_styku = [
 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
 100, 101, 102, 103, 104, 105, 106, 107,
 108, 109, 110, 111, 112, 113, 114, 115, 
 116, 117, 118, 119, 120, 121, 122, 123,
 124, 125, 126, 127, 128, 129, 130, 131,
 132, 133, 134, 135, 136, 137, 138, 139,
 140, 141, 142, 143, 144, 145, 146, 147,
 148, 149, 150
 ]


#Zminni objektiv na monitori
x_rect = 1200 # cordynaty pershoho kubika
x_rect2 = 1600 # cordynaty druhoho kubika
y_rect = 300 # cordynaty hravcia
x = 300 # cordynaty knopok
y = 215 # cordynaty knopok
heigth = 50 # vysota knopky
width = 200 # shyryna knopky
health = 100 # zdorovia
score = 0
speed = 8 # shvydkist' z jakoju ruchajietsia pereshkoda
jump_count = 10 # zminna dl'a pryzhka
pic_x = 2000
pic_y = 288

#Col'ory
white = (255, 255, 255)
green = (66, 190, 61)
green2 = (26, 142, 22)
black = (0, 0, 0)
gray = (66, 70, 61)

#Pictres
picture = pygame.image.load('small_health.jpg')		

#Shryfty
big_text = pygame.font.Font('a_assuan_titulstrdst_bold.ttf', 70) # Velykyj text
large_text = pygame.font.Font('a_assuan_titulstrdst_bold.ttf', 40) # Serednij text
small_text = pygame.font.Font('a_assuan_titulstrdst_bold.ttf', 20) # Malyj text

#Znachennia boolean
var_health = True
action = None
game_over = False
runing = False
vasia = True #zminna dl'a funkcii health
vasia1 = True #zminna dl'a score
vasia2 = True #zminna dl'a funkcii score_count (dl'a druhoji pereshkody)
bg = True
rivni = False
pause_menu = False
is_jump = False
run = True
hovno = Score(100)

def draw_score():
		napys1 = small_text.render("Score:", True, black)
		record = small_text.render(repr(score), True, black)

		window.blit(napys1, (680, 10))
		window.blit(record, (755, 10))

def draw_bg():
	#Line
	pygame.draw.line(window, black, (0, 353), (800, 353), 3)

	#Druha pereshkoda
	pygame.draw.rect(window, green, (x_rect2, 300, 50, 50), 0)

	#Hravec
	pygame.draw.rect(window, gray, (98, y_rect - 2, 54, 54), 3)
	pygame.draw.rect(window, black, (100, y_rect, 50, 50), 0)

	#Pershsa pereshkoda 
	pygame.draw.rect(window, black, (x_rect, 300, 50, 50), 0)

	#Health
	pygame.draw.rect(window, black, (10, 10, 103, 11), 2)
	pygame.draw.rect(window, green, (12, 12, health, 8), 0)

	draw_zdorovia(health)
	draw_score()

def pause_button(x, y):
	global pause_menu
	pygame.draw.rect(window, black, (x, y, 8, 30))
	pygame.draw.rect(window, black, (x + 15, y, 8, 30))

	mouse = pygame.mouse.get_pos()
	pressed = pygame.mouse.get_pressed()
	if mouse[0] > x and mouse[1] > y and mouse[0] < x + 23 and mouse[1] < y + 30:
		pygame.draw.rect(window, black, (x - 2, y - 2, 10, 32))
		pygame.draw.rect(window, black, (x + 15, y - 2, 10, 32))

		if pressed[0] == 1:
			pause_menu = True

#def draw_score():
#	napys1 = small_text.render("Score:", True, black)
#	record = small_text.render(repr(score), True, black)
#
#	window.blit(napys1, (680, 10))
#	window.blit(record, (755, 10))

def start_variable():
	global score, speed, rivni, runing, bg, x_rect, x_rect2, vasia, game_over, health
	score = 0
	vasia = True
	speed = 8
	health = 100
	runing = True
	game_over = False
	x_rect = 1200
	x_rect2 = 1600

def draw_zdorovia(zdorovia):
	napys = small_text.render(repr(zdorovia), True, black)

	window.blit(napys, (115, 6))

def button(button_name, x, y, width, heigth, ic, ac, text_color, action):
	global score, speed, rivni, runing, bg, x_rect, x_rect2
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	text = large_text.render(button_name, True, text_color)

	if mouse[0] > x and mouse[1] > y and mouse[0] < x + width and mouse[1] < y + heigth:
		pygame.draw.rect(window, ac, (x, y, width, heigth), 0)
		window.blit(text, (x + 30, y + 8))
		if click[0] == 1:
			if action == "play":
				start_variable()
				runing = True
			elif action == "quit":
				quit()
			elif action == "restart":
				start_variable()
				#runing = True
			elif action == "level":
				rivni = True
			elif action == "back":
				bg = True	
			elif action == "level1":
				start_variable()
			elif action == "level2":
				score = 0
				runing = True
				speed = 14
				health = 100
				x_rect = 1200
				x_rect2 = 1600
			elif action == "resume":
				runing = True
				
	else:	
		pygame.draw.rect(window, ic, (x, y, width, heigth), 0)
		window.blit(text, (x + 35, y + 10))

while run:
	pygame.time.delay(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()	
	window.fill(white)
	#window.blit(text, (100, 100))

	if keys[pygame.K_q]:
		#vasia1 = False
		vasia = True
		speed = 8
		runing = True

	#RUNING
	if runing:
		game_over = False

		if keys[pygame.K_ESCAPE]:
			quit()

		keys = pygame.key.get_pressed()
		rivni = False
		bg = False
		pause_menu = False
		x_rect -= speed
		x_rect2 -= speed
		pic_x -= speed

		if keys[pygame.K_p]:
			#Pause button 
			pygame.draw.rect(window, black, (498, 8, 12, 34))
			pygame.draw.rect(window, black, (513, 8, 12, 34))
			#time.sleep(0.2)
			pause_menu = True

		#Testovy kvadrat
		#pygame.draw.rect(window, green, (350, 200, 50, 50), 0)

		#Line
		pygame.draw.line(window, black, (0, 353), (800, 353), 3)

		#Druha pereshkoda
		pygame.draw.rect(window, green, (x_rect2, 300, 50, 50), 0)

		#Hravec
		pygame.draw.rect(window, gray, (98, y_rect - 2, 54, 54), 3)
		pygame.draw.rect(window, black, (100, y_rect, 50, 50), 0)

		#Pershsa pereshkoda 
		pygame.draw.rect(window, black, (x_rect, 300, 50, 50), 0)

		#Health
		pygame.draw.rect(window, black, (10, 10, 103, 11), 2)
		pygame.draw.rect(window, green, (12, 12, health, 8), 0)

		#Pause_Button
		pygame.draw.rect(window, black, (500, 10, 8, 30))
		pygame.draw.rect(window, black, (515, 10, 8, 30))

		draw_zdorovia(health)
		pause_button(500, 10)

		#if x_rect < -50:
			#cordinate = random.choice(l)
			#x_rect += 1200
			#vasia = True

		if x_rect2 < -50:
			cordinate = random.choice(l)
			x_rect = cordinate
			cordinate2 = random.choice(l2)
			x_rect2 = cordinate2
			vasia = True
			vasia2 = True
			var_health = True

		if keys[pygame.K_SPACE]:
			is_jump = True

		if is_jump:
			if jump_count >= -10:
				neg = 1
				if jump_count < 0:
					neg = -1
				y_rect -= (jump_count**2) * 0.5 * neg
				jump_count -= 1
			else:
				is_jump = False
				jump_count = 10

		if x_rect in miscia_styku and y_rect > 250:
			if vasia:
				health -= 25
				vasia = False

		if x_rect2 in miscia_styku and y_rect > 250:
			if vasia2:
				health -= 25
				vasia2 = False


		if health <= 0:
			runing = False
			game_over = True


		#if pic_x < 150:
		#	if var_health:
		#		health += 25
		#		var_health = False

	if pause_menu:
		runing = False

		draw_bg()

		button("RESUME", 300, 150, 200, 50, green, green2, black, "resume")

	if game_over:
		runing = False

		draw_bg()

		text = big_text.render("GAME OVER", True, black)
		window.blit(text,(206, 214))
		button("RESTART", 250, 267, 250, 50, green, green2, black, "restart")
		button("QUIT", 275, 325, 200, 50, green, green2, black, "quit")
		button("LEVEL", 280, 390, 200, 50, green, green2, black, "level")
		if keys[pygame.K_q]:
			health = 100
			runing = True
			x_rect = 1200
			x_rect2 = 1600
			score = 0
		elif keys[pygame.K_ESCAPE]:
			quit() 		


	if bg:
		draw_bg()
		rivni = False
		if keys[pygame.K_ESCAPE]:
			quit()

		button("START", 300, 150, 200, 50, green, green2, black, "play")
		button("QUIT", 300, 255, 200, 50, green, green2, black, "quit")
		button("LEVEL", 300, 360, 200, 50, green, green2, black, "level")

	if rivni:
		game_over = False
		bg = False
		button("BACK", -25, -5, 180, 50, white, white, black, "back")
		button("LEVEL 1", 200, 200, 200, 50, green, green2, white, "level1")
		button("LEVEL 2", 425, 200, 200, 50, green, green2, white, "level2")

	f = "runing = " + repr(runing) + "|| game_over = " + repr(game_over) + "|| bg = " + repr(bg) + "|| rivni = " + repr(rivni) + "|| pause_menu = " + repr(pause_menu)  
		#s = "y_rect=" + repr(y_rect) + "||" + "x_rect=" + repr(x_rect) + "||" + "x_rect2=" + repr(x_rect2) + "||" + "health=" + repr(health)
		#print(score // 6)
	#s = "x_rec = " + repr(x_rect) + "|| " + "x_rect2 = " + repr(x_rect2) + "||" + repr(score)
	#p = "vasia = " + repr(vasia) + "||" + "vasia1 = " + repr(vasia1) + "||" + "vasia2 = " + repr(vasia2)
	print(f)
	pygame.display.update()
pygame.quit()