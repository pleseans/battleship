import pygame
import random as r

board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]
pygame.init()
WIDTH, HEIGHT = 800, 400
CELL_SIZE1 = 50  # 왼쪽 격자 크기
CELL_SIZE2 = 50  # 오른쪽 격자 크기
start_point = input().split()#[0] == 가로ㅡ,[1] == 세로
end_point = input().split()#[0] == 가로ㅡ,[1] == 세로

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("battleship")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # 왼쪽 절반 격자
    for y in range(0, HEIGHT, CELL_SIZE1):
        for x in range(0, WIDTH // 2, CELL_SIZE1):
            pygame.draw.rect(screen, (0, 0, 0), (x, y, CELL_SIZE1, CELL_SIZE1), 1)

    # 오른쪽 절반 격자
    for y in range(0, HEIGHT, CELL_SIZE2):
        for x in range(WIDTH // 2, WIDTH, CELL_SIZE2):
            pygame.draw.rect(screen, (0, 0, 0), (x, y, CELL_SIZE2, CELL_SIZE2), 1)
            
    pygame.draw.line(screen, (255, 0, 0), (400, 0), (400, 600), 5)

    for i in range(1): #내 보드 설정

        start_point = list(map(int, start_point))
        end_point = list(map(int, end_point))

    if start_point[0] != end_point[0]:#가로
        for j in range(start_point[0]-1,end_point[0]):
            # board[start_point[1]-1][j] = 1
            pygame.draw.rect(screen,(0,0,255),(j*50,(start_point[1]-1)*50,49,49))
        # for row in board:
        #     print(row)
    else:#세로
        for j in range(start_point[1]-1,end_point[1]):
            # board[j][start_point[0]-1] = 1
            pygame.draw.rect(screen,(0,0,255),((start_point[0]-1)*50,j*50,49,49))
        # for row in board: 
        #     print(row)
    # print("==========내꺼 최종==========")

    if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  # event.pos -> (x, y) 튜플 값 반환
            if x < 50:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if  x > 50 and x < 100:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if x > 100 and x < 150:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if x > 150 and x < 200:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if x > 200 and x < 250:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if x > 250 and x < 300:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if x > 300 and x < 350:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            if x > 350 and x < 400:
                if y < 50:
                    print("a")
                if y > 50 and y < 100:
                    pygame.draw.rect()
                if y > 100 and y < 150:
                    pygame.draw.rect()
                if y > 150 and y < 200:
                    pygame.draw.rect()
                if y > 200 and y < 250:
                    pygame.draw.rect()
                if y > 250 and y < 300:
                    pygame.draw.rect()
                if y > 300 and y < 350:
                    pygame.draw.rect()
                if y > 350 and y < 400:
                    pygame.draw.rect()
            pygame.time.delay(100)

    pygame.display.update()

pygame.quit()
