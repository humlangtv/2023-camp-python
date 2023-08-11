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
enemy_speed = 1
to_x = 0
character_spped = 1\

clock = pygame.time.Clock()
#이벤트 루프
running = True
while running:
    dt = clock.tick(202)

    #타이머 집어 넣기
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/100
    timer = game_font.rander(str(int(total_time - elapsed_time)),True,(255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=character_spped
            elif event.key == pygame.K_RIGHT:
                to_x +=character_spped
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    character_x_pos += to_x
    #가로의 경계값 설정(캐릭터)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로의 경계값 설정(캐릭터)
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #경계값 설정 (장애물)
    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)
        

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(timer,(10,10))

    pygame.display.update()

#pygame 종료
pygame.quit()