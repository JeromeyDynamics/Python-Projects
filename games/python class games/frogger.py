import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAYER_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
PLAYER_SIZE = 20
OBSTACLE_SIZE = 20
OBSTACLE_SPEED = 5
FPS = 60

background_img = pygame.image.load(r'C:\Users\Omega\Downloads\1000_F_372119862_yS6f4QH9wu0Wt5qvm5SO5WUO91VTc29Q.jpg')


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger Game")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SIZE
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SIZE
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PLAYER_SIZE
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SIZE

class Lane(pygame.sprite.Sprite):
    def __init__(self, y, speed):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, OBSTACLE_SIZE))
        self.image.fill((100, 100, 100))  # Grey color for lane
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.speed < 0 and self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
        self.image.fill(OBSTACLE_COLOR)
        self.rect = self.image.get_rect()
        self.lane = lane
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = self.lane.rect.centery

    def update(self):
        self.rect.x += self.lane.speed
        if self.lane.speed > 0 and self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.lane.speed < 0 and self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
            
def main():
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    lanes = []
    obstacles = pygame.sprite.Group()

    # Create lanes and obstacles
    for i in range(5):  # Number of lanes
        lane_y = (i + 1) * (SCREEN_HEIGHT // 6)
        lane_speed = random.choice([-1, 1]) * OBSTACLE_SPEED
        lane = Lane(lane_y, lane_speed)
        lanes.append(lane)
        all_sprites.add(lane)

        for _ in range(3):  # Number of obstacles per lane
            obstacle = Obstacle(lane)
            obstacles.add(obstacle)
            all_sprites.add(obstacle)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        # Check for collisions
        if pygame.sprite.spritecollide(player, obstacles, False):
            # Handle collision (e.g., game over, reset player position)
            player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE)

        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)
        
        #animations
        screen.blit(background_img, (0,0))

if __name__ == "__main__":
    main()