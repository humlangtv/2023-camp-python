import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set.caption("[하찮은 게임]")

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\저스트필\\Desktop\\하찮은 그림\\해변.png")

#캐릭터 불러오기
character = pygame.image.lode("C:\\Users\\저스트필\\Desktop\\하찮은 그림\\하찮은 그림.png")
character_size = character.get_rect().size
character_width = character_size(0)
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

#장애물 불러오기
enemy = pygame.image.load("C:\\Users\\저스트필\\Desktop\\하찮은 그림\\김태훈 똥.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_hehgt = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 20

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    pygame.display.update()

#pygame 종료
pygame.quit()