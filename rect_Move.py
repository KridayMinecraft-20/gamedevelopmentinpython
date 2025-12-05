import pygame
pygame.init()

width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rectangle Movement")

rect_x, rect_y = 300, 200
rect_width, rect_height = 50, 50
speed = 5

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed

    rect_x = max(0, min(rect_x, width - rect_width))
    rect_y = max(0, min(rect_y, height - rect_height))

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

pygame.quit()

