//Particle systems are widely used in games to create effects like fire, smoke, and explosions.

import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.lifetime = 100
        self.radius = 5

    def update(self):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)
        self.lifetime -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

particles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    particles.append(Particle(screen_width // 2, screen_height // 2))

    screen.fill((0, 0, 0))
    for particle in particles:
        particle.update()
        particle.draw(screen)
        if particle.lifetime <= 0:
            particles.remove(particle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
