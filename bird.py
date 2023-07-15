import pygame
import sys

# Pygame Configuration
pygame.init()
SCREENWIDTH, SCREENHEIGHT = 400, 600
FPS = 30
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Load Images
BACKGROUND = pygame.image.load('sprites/background-day.png')
BIRD_DOWN = pygame.image.load('sprites/yellowbird-downflap.png')
BIRD_MID = pygame.image.load('sprites/yellowbird-midflap.png')
BIRD_UP = pygame.image.load('sprites/yellowbird-upflap.png')
PIPE = pygame.image.load('sprites/pipe-green.png')

# Bird Configuration
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BIRD_MID
        self.rect = self.image.get_rect(center = (SCREENWIDTH//2, SCREENHEIGHT//2))
        self.movement = 0

    def flap(self):
        self.movement = -5

    def update(self):
        self.movement += 0.25
        self.rect.centery += self.movement

# Pipe Configuration
class Pipe(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = PIPE
        self.rect = self.image.get_rect(midtop = position)

    def update(self):
        self.rect.centerx -= 5

def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.flap()

        screen.blit(BACKGROUND, (0, 0))

        bird.update()
        screen.blit(bird.image, bird.rect)

        if pygame.sprite.spritecollideany(bird, pipes):
            break

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
