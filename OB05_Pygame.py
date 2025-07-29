import pygame
pygame.init()
import time

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image1 = pygame.image.load("Змея.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("стакан.png")
image_rect2 = image2.get_rect()

run =  True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Блок для управления картинок мышью
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX-100
            image_rect1.y = mouseY-90

    if image_rect1.colliderect(image_rect2):
        print("Зачем пихаешься")
        time.sleep(1)

#Блок для управления изображения курсором
    # speed = 1
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect1.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect1.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect1.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect1.y += speed

    screen.fill((92, 163, 99))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip() #команда по обновлению экрана, нужна для димнамического обновления экрана

pygame.quit()

