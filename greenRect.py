import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My First Game Screen")

WHITE = (255, 255, 255)
KINGFISHER = (0, 100, 145)

font = pygame.font.SysFont(None, 28)

text = font.render("This is a rectangle with my favorite color! 😊", True, (0, 0, 0))

rect_width, rect_height = 200, 100
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.rect(screen, KINGFISHER, rectangle)

    text_rect = text.get_rect(center=(WIDTH // 2, rect_y + rect_height + 40))
    screen.blit(text, text_rect)

    pygame.display.update()

