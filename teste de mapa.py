import pygame
import os
WIDTH = 768
HEIGHT = 576
FPS = 60

class Player(object):

    def __init__(self, pos):
        players.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

    # Move the rect
        self.rect.x += dx
        self.rect.y += dy

    # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = platform.rect.top

class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class Platform(object):
    
    def __init__(self, pos):
        platforms.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

current_level = 1

pygame.init()

pygame.display.set_caption("Teste de nível")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
walls = []
platforms = []
players = []

if current_level == 1:

    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W                      W",
    "W                      W",
    "W                      W",
    "W                      W",
    "W                      W",
    "W                      W",
    "W                      W",
    "W                      W",
    "W                      W",
    "W               PP     W",
    "W                      W",
    "W   PPP                W",
    "W                      W",
    "W             PPPP     W",
    "W    J                 W",
    "W                      W",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    ]

    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "P":
                Platform((x, y))
            if col == "J":
                Player((x, y))
            x += 32
        y += 32
        x = 0
    
running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for player in players:
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
    for platform in platforms:
        pygame.draw.rect(screen, (0, 255, 255), platform.rect)
    pygame.display.flip()

