import pygame
import random
from pygame import mixer

pygame.init()
# mixer.init()

fpsClock = pygame.time.Clock()
width = 600
height = 350

mixer.music.load("music.mp3")
mixer.music.play(-1)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to my pygame home!")
#Predetermined variables
sun_posX = 20
sun_posY = 20
moon_posY = 300
bg_colour = (58, 148, 181)
win_colour = (58, 148, 181)
cloud_x_1 = 150
cloud_x_2 = 175
cloud_x_3 = 200
cloud_colour = (255, 255, 255)
speed = 2
rainbow_1 = pygame.image.load("Rainbow.png")
rainbow_1 = pygame.transform.scale(rainbow_1, (500, 250))
rainbow_2 = pygame.image.load("Rainbow_75.png")
rainbow_2 = pygame.transform.scale(rainbow_2, (500, 250))
rainbow_3 = pygame.image.load("Rainbow_50.png")
rainbow_3 = pygame.transform.scale(rainbow_3, (500, 250))
rainbow_4 = pygame.image.load("Rainbow_50.png")
rainbow_4 = pygame.transform.scale(rainbow_4, (500, 250))
rainbow_5 = pygame.image.load("Rainbow_25.png")
rainbow_5 = pygame.transform.scale(rainbow_5, (500, 250))
rainbow_6 = pygame.image.load("Rainbow_0.png")
rainbow_6 = pygame.transform.scale(rainbow_6, (500, 250))
flower_1 = pygame.image.load("flower_1.png")
flower_1 = pygame.transform.scale(flower_1, (100, 50))
flower_3 = pygame.image.load("flower_3.png")
flower_3 = pygame.transform.scale(flower_3, (50, 50))
star = pygame.image.load("star.png")
tree = pygame.image.load("tree.png")
tree = pygame.transform.scale(tree, (150, 150))
star_count = random.randint(30, 50)
# Create 30 random star positions
star_pos = []
for i in range(star_count):
  star_pos.append((random.randint(0, 600), random.randint(0, 450)))

# Game loop
while True:
  #sky
  screen.fill((bg_colour))
  for event in pygame.event.get():
    if pygame.event == pygame.QUIT:
      pygame.quit()

  #Stars
  if sun_posY > 350:
    for i in range(star_count):
      scaling = 22
      star = pygame.transform.scale(star, (scaling, scaling))
      screen.blit(star, (star_pos[i][0], star_pos[i][1]))
      

  #Sun
  pygame.draw.circle(screen, (255, 191, 0), (sun_posX, sun_posY), 35)
  sun_posY += 4
  sun_posX += 7
  if 100 <= sun_posY < 125:
    bg_colour = (218, 160, 109)
  elif 125 <= sun_posY < 150:
    bg_colour = (233, 116, 81)
  elif 150 <= sun_posY < 175:
    bg_colour = (204, 85, 0)
  elif 175 <= sun_posY < 200:
    bg_colour = (192, 64, 0)
  elif 200 <= sun_posY < 225:
    bg_colour = (169, 92, 104)
  elif 225 <= sun_posY < 250:
    bg_colour = (122, 70, 78)
    cloud_colour = (168, 168, 168)
  elif 250 <= sun_posY < 275:
    bg_colour = (97, 56, 62)
    cloud_colour = (140, 139, 139)
  elif 275 <= sun_posY < 300:
    bg_colour = (33, 18, 20)
    cloud_colour = (120, 119, 119)
  elif 300 <= sun_posY < 325:
    bg_colour = (28, 25, 25)
    cloud_colour = (87, 87, 87)
  #Windows night
  if sun_posY > 300:
    win_colour = (216, 222, 106)

  #Moon
  if sun_posY > 350:
    pygame.draw.circle(screen, (255, 255, 255), (70, moon_posY), 35)
    pygame.draw.circle(screen, (28, 25, 25), (85, moon_posY), 35)
    if moon_posY > 50:
      moon_posY -= 5

  #Fence
  fence_x = 20
  pygame.draw.rect(screen, (111, 78, 55), (0, 275, 600, 20))
  for i in range(20):
    pygame.draw.rect(screen, (111, 78, 55), (fence_x, 260, 25, 50))
    fence_x += 50
  #Flowers
  screen.blit(flower_1, (500, 249))
  screen.blit(flower_3, (450, 249))
  #Rainbow
  if 100 <= sun_posY < 125:
    rainbow = screen.blit(rainbow_2, (-40, 80))
  elif 125 <= sun_posY < 150:
    rainbow = screen.blit(rainbow_3, (-40, 80))
  elif 150 <= sun_posY < 175:
    rainbow = screen.blit(rainbow_4, (-40, 80))
  elif 175 <= sun_posY < 200:
    rainbow = screen.blit(rainbow_5, (-40, 80))
  elif sun_posY >= 200:
    rainbow = screen.blit(rainbow_6, (-40, 80))
  else:
    screen.blit(rainbow_1, (-40, 80))

  #Tree
  screen.blit(tree, (0, 160))
  #Cloud
  pygame.draw.circle(screen, (cloud_colour), (cloud_x_1, 75), 30)
  pygame.draw.circle(screen, (cloud_colour), (cloud_x_2, 60), 30)
  pygame.draw.circle(screen, (cloud_colour), (cloud_x_3, 75), 30)
  pygame.draw.circle(screen, (cloud_colour), (cloud_x_2, 85), 30)
  cloud_x_3 += 4
  cloud_x_2 += 4
  cloud_x_1 += 4

  #Right side cloud bound
  if cloud_x_3 > 700 and cloud_x_2 > 660 and cloud_x_1 > 630:
    cloud_x_3 = -15
    cloud_x_2 = -45
    cloud_x_1 = -75
    pygame.draw.circle(screen, (cloud_colour), (cloud_x_1, 75), 30)
    pygame.draw.circle(screen, (cloud_colour), (cloud_x_2, 60), 30)
    pygame.draw.circle(screen, (cloud_colour), (cloud_x_3, 75), 30)
    pygame.draw.circle(screen, (cloud_colour), (cloud_x_2, 85), 30)
    cloud_x_3 += 4
    cloud_x_2 += 4
    cloud_x_1 += 4
  #Home Base
  pygame.draw.rect(screen, (110, 38, 14), (200, 140, 200, 400))

  #Brick Outline
  outline_y = 150
  outline_x = 205
  for i in range(7):
    pygame.draw.line(screen, (0, 0, 0), (outline_x, 142), (outline_x, 350))
    outline_x += 32
    for i in range(10):
      pygame.draw.line(screen, (0, 0, 0), (200, outline_y), (399, outline_y))
      outline_y += 40

  #Windows
  pygame.draw.rect(screen, (win_colour), (225, 185, 50, 50))
  pygame.draw.rect(screen, (win_colour), (325, 185, 50, 50))
  #Roof
  pygame.draw.rect(screen, (128, 128, 128), (330, 50, 25, 50))
  pygame.draw.rect(screen, (112, 112, 112), (322, 40, 40, 15))
  pygame.draw.polygon(screen, (168, 168, 168),
                      ((185, 140), (295, 60), (415, 140)))
  pygame.draw.circle(screen, (255, 255, 255), (300, 110), 27)
  pygame.draw.circle(screen, (win_colour), (300, 110), 25)
  pygame.draw.line(screen, (255, 255, 255), (275, 110), (325, 110), 2)
  pygame.draw.line(screen, (255, 255, 255), (299, 85), (299, 135), 2)

  #Smoke
  pygame.draw.line(screen, (59, 58, 58), (350, 20), (350, 4))
  pygame.draw.line(screen, (59, 58, 58), (340, 35), (340, 9))
  pygame.draw.line(screen, (59, 58, 58), (330, 27), (330, 7))

  #Rain
  if sun_posY > 350:
    for i in range(30):
      pygame.draw.circle(screen, (3, 59, 148),
                         (random.randint(0, 600), random.randint(0, 600)),
                         random.randint(1, 4))
  #Grass
  pygame.draw.rect(screen, (43, 117, 63), (0, 300, 200, 50))
  pygame.draw.rect(screen, (43, 117, 63), (400, 300, 200, 50))

  #Border 1 - For windows
  pygame.draw.line(screen, (255, 255, 255), (225, 184), (274, 184), 2)
  pygame.draw.line(screen, (255, 255, 255), (274, 184), (274, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (225, 234), (274, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (225, 184), (225, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (250, 184), (250, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (225, 210), (274, 210), 2)

  #Border 2 - For windows
  pygame.draw.line(screen, (255, 255, 255), (325, 184), (374, 184), 2)
  pygame.draw.line(screen, (255, 255, 255), (374, 184), (374, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (325, 234), (374, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (325, 184), (325, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (350, 184), (350, 234), 2)
  pygame.draw.line(screen, (255, 255, 255), (325, 210), (374, 210), 2)

  #Door
  pygame.draw.circle(screen, (255, 255, 255), (300, 285), 25)
  pygame.draw.circle(screen, (win_colour), (300, 285), 23)
  pygame.draw.rect(screen, (139, 69, 19), (275, 285, 50, 70))
  pygame.draw.line(screen, (255, 255, 255), (299, 260), (299, 284), 2)
  pygame.draw.circle(screen, (92, 64, 51), (315, 327), 4)

  fpsClock.tick(15)
  pygame.display.update()
