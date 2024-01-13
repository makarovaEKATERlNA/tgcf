from random import randint, choice
import pygame

pygame.init()

W, H = 500, 500
FPS = 30

black = (0, 0, 0)
white = (255, 255, 255)

win = pygame.display.set_mode((W, H))
# Загрузка изображений
rocket_img = pygame.image.load("rocket.png")
rocket_img = pygame.transform.scale(rocket_img, (50, 100))
# Cоздание списка с картинками
stones_img = [pygame.image.load(f"rock{i}.png") for i in range(0, 3)]
stones_img = [pygame.transform.scale(elem, (50, 50)) for elem in stones_img]

clock = pygame.time.Clock()

# Создание класса для игрока
class Rocket(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = rocket_img
        self.rect = rocket_img.get_rect()
        self.rect.y = H * 0.8
        self.rect.x = W * 0.4

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

player_group = pygame.sprite.Group()
player = Rocket()
player_group.add(player)

class Star():
    def __init__(self):
        self.x = randint(0, W)
        self.y = randint(0, H)
        self.rad = 1
        self.speed = randint(1, 3)

    def draw(self):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.rad)

    def move(self):
        self.y += self.speed
        if self.y >= H:
            self.y = 0

stars = [Star() for i in range(0, 50)]
