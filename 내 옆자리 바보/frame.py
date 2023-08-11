import pygame

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set.caption("[하찮은 게임]")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#pygame 종료
pygame.quit()