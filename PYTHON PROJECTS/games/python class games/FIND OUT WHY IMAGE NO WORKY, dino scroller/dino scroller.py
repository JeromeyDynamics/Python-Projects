import pygame
from pygame.locals import QUIT

pygame.init()

width = 800
length = 400

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('Dinosaur Run!')

#background
background_img = pygame.image.load('bg.png')
background_x = 0
background_speed = 2

#Create list with dinosaur images
dinosaur_imgs = [
  pygame.image.load('dino0.png'),
  pygame.image.load('dino1.png'),
  pygame.image.load('dino2.png')
]

#load in cactus image
cactus_img = pygame.transform.scale(pygame.image.load('cactus.png'), (20,30))



dinosaur_x = 80
dinosaur_y = 130
cactus_x = 350
cactus_y = 190
cactus_speed = 2

#animation variable
dinosaur_frame = 0 #which frame of the dino is displayed
dinosaur_anim_speed = 0.1
dinosaur_last_update = 0

#jumping variables
is_jumping = False
jump_velocity = -23
jump_height = 200
current_jump_height = 0

#score variable
score = 0
font = pygame.font.Font('freesansbold.ttf', 30)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            if not is_jumping:
              is_jumping = True

    #scroll the background
    background_x -= background_speed
    if background_x <= -background_img.get_width():
      background_x = 0 

    #move the cactus
    cactus_x -=cactus_speed
    if cactus_x <= -cactus_img.get_width():
      cactus_x = width
      score+=1
    

    #animate the dinosaur
    current_time = pygame.time.get_ticks() #current time
    if current_time-dinosaur_last_update>dinosaur_anim_speed*1000:
      dinosaur_frame = (dinosaur_frame+1)%len(dinosaur_imgs)
      dinosaur_last_update = current_time

    #perform the jump
    if is_jumping:
      dinosaur_y += jump_velocity
      jump_velocity += 1

      if dinosaur_y>=130:
        is_jumping = False
        dinosaur_y = 130
        jump_velocity = -23

    #check for collision
    cactus_rect = cactus_img.get_rect(topleft= (cactus_x+25, cactus_y+25))
    dinosaur_rect = dinosaur_imgs[dinosaur_frame].get_rect(topleft= (dinosaur_x, dinosaur_y))
    if dinosaur_rect.colliderect(cactus_rect):
      running = False
      

  #boolean= True or False
  
#display the sprites
    #display the background
    screen.blit(background_img, (background_x, 0))
    screen.blit(background_img, (background_x + background_img.get_width(),0))

    #display the dinosaur
    screen.blit(dinosaur_imgs[dinosaur_frame], (dinosaur_x, dinosaur_y))

    #display the cactus
    screen.blit(cactus_img, (cactus_x, cactus_y))

    #display the score
    score_text = font.render("score: "+ str(score), True, (0,0,0))
    screen.blit(score_text, (10,10))

    pygame.display.flip()